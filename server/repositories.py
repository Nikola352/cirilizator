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
