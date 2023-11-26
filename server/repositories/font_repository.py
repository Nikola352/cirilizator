from sqlalchemy import func


class FontRepository:
    def __init__(self, model, db):
        self.model = model
        self.db = db

    def get_all_fonts(self):
        return self.model.query.all()

    def get_font_by_id(self, font_id):
        return self.model.query.get(font_id)

    def get_font_by_name(self, font_name):
        return self.model.query.filter_by(font_family=font_name).first()

    def create_font(self, font_data):
        new_font = self.model(
            font_family=font_data.font_family,
            font_subfamily=font_data.font_subfamily,
            font_full_name=font_data.font_full_name,
            font_postscript_name=font_data.font_postscript_name,
            font_weight=font_data.font_weight,
            font_width=font_data.font_width,
            font_italic=font_data.font_italic,
            font_ascent=font_data.font_ascent,
            font_descent=font_data.font_descent,
            font_line_gap=font_data.font_line_gap,
            font_cap_height=font_data.font_cap_height,
            font_x_height=font_data.font_x_height,
            font_stem_v=font_data.font_stem_v,
            font_file=font_data.font_file,
        )
        self.db.session.add(new_font)
        self.db.session.commit()
        return new_font

    def delete_font(self, font_id):
        font = self.get_font_by_id(font_id)
        if font:
            self.db.session.delete(font)
            self.db.session.commit()
            return True
        return False

    def get_random_font(self):
        return self.model.query.order_by(func.random()).first()
