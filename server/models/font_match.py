from database.db import db


class FontMatch(db.Model):
    __tablename__ = 'font_match'
    id = db.Column(db.Integer, primary_key=True)
    
    font_id = db.Column(db.Integer, db.ForeignKey('font.id'), nullable=False)
    font = db.relationship('Font', foreign_keys=[font_id], backref=db.backref('font_match', lazy=True))
    
    match_font_id = db.Column(db.Integer, db.ForeignKey('font.id'), nullable=False)
    match_font = db.relationship('Font', foreign_keys=[match_font_id], backref=db.backref('match_font', lazy=True))
    
    score = db.Column(db.Float, nullable=False)

    def as_dict(self):
        return {
            'font_id': self.font_id,
            'match_font_id': self.match_font_id,
            'score': self.score,
        }
