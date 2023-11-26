import threading


from fonts.font_collector import FontCollector

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

    def get_all_fonts(self):
        return self.repository.get_all_fonts()

    def get_font_by_id(self, font_id):
        return self.repository.get_font_by_id(font_id)

    def get_font_by_name(self, font_name, app_context):
        with app_context:
            return self.repository.get_font_by_name(font_name)

    def create_font(self, font_data, app_context):
        return self.repository.create_font(font_data, app_context)

    def get_random_font_pair(self):
        font_match = self.font_match_repository.get_random_font_match()
        font = self.repository.get_font_by_id(font_match.font_id)
        matching_font = self.repository.get_font_by_id(font_match.match_font_id)
        return {
            'font': font.as_dict(),
            'matching': matching_font.as_dict()
        }

    def get_matching_font(self, font_name, app_context):
        font = self.get_font_by_name(font_name, app_context)
        font_match = self.font_match_repository.get_font_matches_by_font_id(font.id)
        return self.repository.get_font_by_id(font_match.match_font_id)

    def new_match(self, font_name, matching_font_name, score, app_context):
        font = self.get_font_by_name(font_name, app_context)
        if font:
            matching_font = self.get_font_by_name(matching_font_name, app_context)
            self.font_match_repository.create_font_match(font.id, matching_font.id, score, app_context)

    def clear_table(self):
        self.repository.delete_all_fonts()
        self.font_match_repository.delete_all_font_matches()

    def start_collector(self, app_context):
        with app_context:
            # Start the collector in a separate thread
            font_thread = threading.Thread(target=self.font_collector.task_start_font_collector, args=(self,app_context,))
            font_thread.start()
            self.font_collector.task_running.set()

    def is_collector_running(self):
        return self.font_collector.task_running.is_set()
