class FontService:
    def __init__(self, repository):
        self.repository = repository

    def get_all_fonts(self):
        return self.repository.get_all_fonts()

    def get_font_by_id(self, font_id):
        return self.repository.get_font_by_id(font_id)

    def get_font_by_name(self, font_name):
        return self.repository.get_font_by_name(font_name)

    def create_font(self, font_data):
        return self.repository.create_font(font_data)

    def get_random_font_pair(self):
        font = self.repository.get_random_font()
        matching = self.get_matching_font(font)
        return {
            'font': font.as_dict(),
            'matching': matching.as_dict()
        }

    def get_matching_font(self, font):  # TODO: implement
        return self.repository.get_random_font()
