import requests
from bs4 import BeautifulSoup
import re
import zipfile
import os
import shutil
from font_parser import ALLOWED_FONT_TYPES


FONTS_DIR = os.path.join(os.getcwd(), 'server', 'resources', 'fonts')  # debug
# FONTS_DIR = os.path.join(os.getcwd(), 'resources', 'fonts')

# List of urls to start crawling from
START_URLS = [
    # 'https://www.rnids.rs/%D1%9B%D0%B8%D1%80%D0%B8%D0%BB%D0%B8%D1%86%D0%B0-%D0%BD%D0%B0-%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82%D1%83/%D1%9B%D0%B8%D1%80%D0%B8%D0%BB%D0%B8%D1%87%D0%BA%D0%B8-%D1%84%D0%BE%D0%BD%D1%82%D0%BE%D0%B2%D0%B8-%D0%BD%D0%B0-%D0%BF%D0%BE%D0%BA%D0%BB%D0%BE%D0%BD',
    # 'https://www.tipometar.org/tipometar/Poklanjamo.html',
    # 'https://www.dafont.com',
    # 'https://www.fontspace.com/sellena-brush-font-f71257',
    'https://www.1001freefonts.com'
]

# List of prefixes of urls that point to font files
# (if you expect to stay on the same domain, you might know the prefix)
# If you don't know the prefix, set it to None
FILE_URL_PREFIXES = [
    # 'https://www.rnids.rs/sites/default/files',
    # 'https://www.tipometar.org',
    # None,
    # None,
    None
]


def download_file(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Connection error:', url)
        return []
    except requests.exceptions.InvalidURL:
        print('Invalid URL:', url)
        return []
    filename = os.path.join(FONTS_DIR, url.split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(response.content)
        return filename


def download_and_extract_zip(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Connection error:', url)
        return []
    except requests.exceptions.InvalidURL:
        print('Invalid URL:', url)
        return []
    filename = os.path.join(FONTS_DIR, url.split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(response.content)
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(FONTS_DIR)
        return zip_ref.namelist()


def crawl(url, visited_urls, file_url_prefix, depth=3):
    if depth == 0:
        return []

    font_files = []

    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Connection error:', url)
        return []
    except requests.exceptions.InvalidURL:
        print('Invalid URL:', url)
        return []

    if response.status_code != 200:
        return []
    
    if response.headers['Content-Type'] == 'application/zip':
        try:
            font_files.extend(download_and_extract_zip(url))
        except zipfile.BadZipFile:
            print('Bad zip file:', url)
        return font_files

    # #####################################################
    if re.search(r'\.(otf|ttf|woff2)$', url):
        font_files.append(download_file(url))
        return font_files
    elif re.search(r'\.zip$', url):
        print(url)
        try:
            font_files.extend(download_and_extract_zip(url))
        except zipfile.BadZipFile:
            print('Bad zip file:', url)
        return font_files

    # if response.headers['Content-Type'] != 'text/html':
    #     return []

    soup = BeautifulSoup(response.text, 'html.parser')
    base_url = '/'.join(url.split('/')[:3])
    url_guess = '/'.join(url.split('/')[:-1])
    
    urls_to_visit = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if not href.startswith('http'):
            new_url = str(url) + str(href) if href.startswith('/') else str(url) + '/' + str(href)
            if file_url_prefix is None or new_url.startswith(file_url_prefix):
                urls_to_visit.append(new_url)
            new_url = str(base_url) + str(href) if href.startswith('/') else str(base_url) + '/' + str(href)
            if file_url_prefix is None or new_url.startswith(file_url_prefix):
                urls_to_visit.append(new_url)
            new_url = str(url_guess) + str(href) if href.startswith('/') else str(url_guess) + '/' + str(href)
            if file_url_prefix is None or new_url.startswith(file_url_prefix):
                urls_to_visit.append(new_url)
        elif file_url_prefix is None or href.startswith(file_url_prefix):
            urls_to_visit.append(href)

    while urls_to_visit:
        url = urls_to_visit.pop()
        if url not in visited_urls:
            visited_urls.add(url)
            font_files.extend(crawl(url, visited_urls, file_url_prefix, depth - 1))

    return font_files


def convert_directory_names(paths):
    converted_paths = []
    for path in paths:
        if os.path.isdir(path):
            files = os.listdir(path)
            if len(files) == 0:
                continue
            files = convert_directory_names([os.path.join(path, file) for file in files])
            converted_paths.extend([os.path.join(path, file) for file in files])
        else:
            converted_paths.append(path)
    return converted_paths


def remove_dissalowed(path):
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            remove_dissalowed(os.path.join(path, file))
            if len(os.listdir(os.path.join(path, file))) == 0:
                shutil.rmtree(os.path.join(path, file))
        elif '.' not in file:
            os.remove(os.path.join(path, file))
        elif file.split('.')[-1] not in ALLOWED_FONT_TYPES:
            os.remove(os.path.join(path, file))


if __name__ == '__main__':
    visited_urls = set()
    font_files = []
    for url, file_url_prefix in zip(START_URLS, FILE_URL_PREFIXES):
        print(url, file_url_prefix)
        curr_files = crawl(url, visited_urls, file_url_prefix)
        curr_files = convert_directory_names(curr_files)
        curr_files = [file for file in curr_files if '.' in file and file.split('.')[-1] in ALLOWED_FONT_TYPES]
        font_files.extend(curr_files)
    remove_dissalowed(FONTS_DIR)
    print(font_files)
