import threading

from fonts.font_collector import FontCollector
from fonts.font_matcher import match_fonts

from repositories.font_repository import FontRepository
from repositories.font_match_repository import FontMatchRepository


class FontService:
    def __init__(self,
                 repository: FontRepository,
                 font_match_repository: FontMatchRepository,
                 db,
                 google_fonts_api_key):
        self.repository = repository
        self.font_match_repository = font_match_repository
        self.db = db
        self.font_collector = FontCollector(google_fonts_api_key)
        self.font_queue = self.font_collector.font_queue
        self.start_collector()

    def get_all_fonts(self):
        return self.repository.get_all_fonts()

    def get_font_by_id(self, font_id):
        return self.repository.get_font_by_id(font_id)

    def get_font_by_name(self, font_name):
        return self.repository.get_font_by_name(font_name)

    def create_font(self, font_data):
        return self.repository.create_font(font_data)

    def get_random_font_pair(self):
        font_match = self.font_match_repository.get_random_font_match()
        font = self.repository.get_font_by_id(font_match.font_id)
        matching_font = self.repository.get_font_by_id(font_match.match_font_id)
        return {
            'font': font.as_dict(),
            'matching': matching_font.as_dict()
        }

    def get_matching_font(self, font_name):
        font = self.get_font_by_name(font_name)
        font_match = self.font_match_repository.get_font_matches_by_font_id(font.id)
        return self.repository.get_font_by_id(font_match.match_font_id)

    def new_match(self, font_name, matching_font_name, score):
        font = self.get_font_by_name(font_name)
        matching_font = self.get_font_by_name(matching_font_name)
        self.font_match_repository.create_font_match(font.id, matching_font.id, score)

    def clear_table(self):
        self.repository.delete_all_fonts()
        self.font_match_repository.delete_all_font_matches()

    def start_collector(self):
        # Start the collector in a separate thread
        font_thread = threading.Thread(target=self.font_collector.task_start_font_collector)
        font_thread.start()
        self.font_collector.task_running.set()

        while not self.font_queue.empty():
            font = self.font_queue.get()
            self.create_font(font)

        match_fonts(self)

    def is_collector_running(self):
        return self.font_collector.task_running.is_set()
