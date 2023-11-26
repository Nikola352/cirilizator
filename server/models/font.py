from database.db import db


class Font(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    font_family = db.Column(db.String(255), nullable=False)
    font_subfamily = db.Column(db.String(255), nullable=False)
    font_full_name = db.Column(db.String(255), nullable=False)
    font_postscript_name = db.Column(db.String(255), nullable=False)
    font_weight = db.Column(db.Integer, nullable=False)
    font_width = db.Column(db.Integer, nullable=False)
    font_italic = db.Column(db.Integer, nullable=False)
    font_ascent = db.Column(db.Integer, nullable=False)
    font_descent = db.Column(db.Integer, nullable=False)
    font_line_gap = db.Column(db.Integer, nullable=False)
    font_cap_height = db.Column(db.Integer, nullable=False)
    font_x_height = db.Column(db.Integer, nullable=False)
    font_stem_v = db.Column(db.Integer, nullable=False)
    font_file = db.Column(db.String(255), nullable=False)

    def as_dict(self):
        return {
            'font_family': self.font_family,
            'font_subfamily': self.font_subfamily,
            'font_full_name': self.font_full_name,
            'font_postscript_name': self.font_postscript_name,
        }
