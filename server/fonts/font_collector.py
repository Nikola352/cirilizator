import threading
from queue import Queue

import requests
import os

from fonts.font_parser import Font
from fonts.font_matcher import match_fonts


FONTS_DIR = os.path.join(os.getcwd(), 'resources', 'fonts')


def fetch_fonts(API_KEY):
    response = requests.get(f'https://webfonts.googleapis.com/v1/webfonts?sort=POPULARITY&subset=cyrillic-ext&key={API_KEY}')
    fonts_dict = response.json()

    for font in fonts_dict['items']:
        response = requests.get(font['files']['regular'])
        filepath = os.path.join(FONTS_DIR, font['family'] + '.ttf')
        with open(filepath, 'wb') as f:
            f.write(response.content)


class FontCollector:
    def __init__(self, google_fonts_api_key):
        self.font_queue = Queue()
        # A threading event to signal task completion
        self.task_running = threading.Event()
        self.google_fonts_api_key = google_fonts_api_key

    def save_fonts(self):
        for filename in os.listdir(FONTS_DIR):
            filepath = os.path.join(FONTS_DIR, filename)
            font = Font(filepath).set_category()
            print("Saving font:", font.font_family)
            self.font_queue.put(font)

    def start_collector(self, GOOGLE_FONTS_API_KEY):
        fetch_fonts(GOOGLE_FONTS_API_KEY)
        self.save_fonts()

    def task_start_font_collector(self, service, app_context):
        self.start_collector(self.google_fonts_api_key)
        self.task_running.clear()
        while not self.font_queue.empty():
            font = self.font_queue.get()
            service.create_font(font, app_context)

        match_fonts(service, app_context)
