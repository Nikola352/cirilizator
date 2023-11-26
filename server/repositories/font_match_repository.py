from sqlalchemy import func
from models.font_match import FontMatch


class FontMatchRepository:
    def __init__(self, model: FontMatch, db):
        self.model = model
        self.db = db

    def get_all_font_matches(self):
        return self.model.query.all()
    
    def get_font_match_by_id(self, font_match_id):
        return self.model.query.get(font_match_id)
    
    def get_font_matches_by_font_id(self, font_id):
        return self.model.query.filter_by(font_id=font_id).first()
    
    def get_random_font_match(self):
        return self.model.query.order_by(func.random()).first()
    
    def create_font_match(self, font_id, matching_font_id, score):
        new_font_match = self.model(font_id=font_id, match_font_id=matching_font_id, score=score)
        self.db.session.add(new_font_match)
        self.db.session.commit()
        return new_font_match
        
    def delete_all_font_matches(self):
        try:
            self.model.query.delete()
            self.db.session.commit()
            return True
        except Exception as e:
            # Handle exceptions if needed
            print(f"Error deleting all font matches: {str(e)}")
            self.db.session.rollback()
            return False