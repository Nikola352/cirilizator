import os

import requests
from PyPDF2 import PdfReader


class BlogPostService:
    def __init__(self, repository):
        self.repository = repository

    def get_all_posts(self):
        return self.repository.get_all_posts()

    def get_post_by_id(self, post_id):
        return self.repository.get_post_by_id(post_id)

    def create_post(self, post_data):
        return self.repository.create_post(post_data)

    def update_post(self, post_id, title, text):
        return self.repository.update_post(post_id, title, text)

    def delete_post(self, post_id):
        return self.repository.delete_post(post_id)


class AdminUserService:
    def __init__(self, repository):
        self.repository = repository

    def get_user_by_username(self, username):
        return self.repository.get_user_by_username(username)


class GPTService:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def call_gpt_api(self, prompt):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
        }

        request_data = {
            'prompt': prompt,
            'max_tokens': 1
        }

        response = requests.post(self.api_url, headers=headers, json=request_data)

        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['text']
        else:
            raise Exception(f'Error calling GPT-3 API: {response.text}')


class TransliterationService:
    def __init__(self):
        pass

    def get_edited_file_path(self, file):
        # Save the uploaded file
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)

        # Edit the PDF file
        translated_text = self.translate_pdf_text(file_path)

        # Save the modified PDF
        edited_file_path = os.path.join("uploads", "edited_" + file.filename)
        save_text_to_pdf(translated_text, edited_file_path)
        return edited_file_path

    def translate_pdf_text(self, pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            reader = PdfReader(pdf_file)
            translated_text = ""
            for page_number in range(len(reader.pages)):
                page_text = reader.pages[page_number].extract_text()
                translated_page_text = self.translate_text(page_text)
                translated_text += translated_page_text
            return translated_text

    def translate_text(self, text):
        transliterated_text = ''
        i = 0
        while i < len(text):
            if i + 2 <= len(text) and text[i:i + 2].lower() in ['lj', 'nj']:
                transliterated_text += latin_to_cyrillic_map.get(text[i:i + 2].lower(), text[i:i + 2])
                i += 2
            else:
                transliterated_text += latin_to_cyrillic_map.get(text[i].lower(), text[i])
                i += 1
        return transliterated_text


latin_to_cyrillic_map = {
    'a': 'а', 'b': 'б', 'c': 'ц', 'č': 'ч', 'ć': 'ћ', 'd': 'д', 'đ': 'ђ',
    'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'х', 'i': 'и', 'j': 'ј', 'k': 'к',
    'l': 'л', 'lj': 'љ', 'm': 'м', 'n': 'н', 'nj': 'њ', 'o': 'о', 'p': 'п',
    'r': 'р', 's': 'с', 'š': 'ш', 't': 'т', 'u': 'у', 'v': 'в', 'z': 'з',
    'ž': 'ж', 'A': 'А', 'B': 'Б', 'C': 'Ц', 'Č': 'Ч', 'Ć': 'Ћ', 'D': 'Д',
    'Đ': 'Ђ', 'E': 'Е', 'F': 'Ф', 'G': 'Г', 'H': 'Х', 'I': 'И', 'J': 'Ј',
    'K': 'К', 'L': 'Л', 'Lj': 'Љ', 'M': 'М', 'N': 'Н', 'Nj': 'Њ', 'O': 'О',
    'P': 'П', 'R': 'Р', 'S': 'С', 'Š': 'Ш', 'T': 'Т', 'U': 'У', 'V': 'В',
    'Z': 'З', 'Ž': 'Ж'
}

def save_text_to_pdf(text, output_path):
    # Save the translated text to a new PDF file
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)
