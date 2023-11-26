from sqlalchemy import func


class BlogPostRepository:
    def __init__(self, model, db):
        self.model = model
        self.db = db

    def get_all_posts(self):
        return self.model.query.all()

    def get_paginated_posts(self, page, per_page):
        paginated_posts = self.model.query.paginate(page=page, per_page=per_page, error_out=False)
        return paginated_posts.items

    def get_post_by_id(self, post_id):
        return self.model.query.get(post_id)

    def create_post(self, post_data):
        new_post = self.model(title=post_data.title, text=post_data.text, category=post_data.category, thumbnail=post_data.thumbnail)
        self.db.session.add(new_post)
        self.db.session.commit()
        return new_post

    def update_post(self, post_id, title, text):
        post = self.get_post_by_id(post_id)
        if post:
            post.title = title
            post.text = text
            self.db.session.commit()
            return post
        return None

    def delete_post(self, post_id):
        post = self.get_post_by_id(post_id)
        if post:
            self.db.session.delete(post)
            self.db.session.commit()
            return True
        return False


class AdminUserRepository:
    def __init__(self, model, db):
        self.model = model
        self.db = db

    def get_user_by_username(self, username):
        return self.model.query.filter_by(username=username).first()

    def register(self, user_data):
        new_user = self.model(username=user_data.username, password=user_data.username)
        self.db.session.add(new_user)
        self.db.session.commit()
        return new_user


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