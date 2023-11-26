import requests
import os

from fonts.font_parser import Font
#from fonts.font_matcher import match_fonts

from services.font_service import FontService

FONTS_DIR = os.path.join(os.getcwd(), 'resources', 'fonts')


def fetch_fonts(API_KEY):
    response = requests.get(f'https://webfonts.googleapis.com/v1/webfonts?sort=POPULARITY&subset=cyrillic-ext&key={API_KEY}')
    fonts_dict = response.json()
    
    for font in fonts_dict['items']:
        response = requests.get(font['files']['regular'])
        filepath = os.path.join(FONTS_DIR, font['family'] + '.ttf')
        with open(filepath, 'wb') as f:
            f.write(response.content)


def save_fonts(font_service: FontService):
    for filename in os.listdir(FONTS_DIR):
        filepath = os.path.join(FONTS_DIR, filename)
        font = Font(filepath)
        print(font.font_family)
        font_service.create_font(font)


def start_collector(GOOGLE_FONTS_API_KEY, font_service):
    fetch_fonts(GOOGLE_FONTS_API_KEY)
    save_fonts(font_service)
    #match_fonts(font_service)
