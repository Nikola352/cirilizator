# repositories.py
from models import BlogPost


class BlogPostRepository:
    def __init__(self):
        self.posts = []
        self.counter = 1

    def get_all_posts(self):
        return self.posts

    def get_post_by_id(self, post_id):
        return next((post for post in self.posts if post.id == post_id), None)

    def create_post(self, post_data):
        new_post = BlogPost(id=self.counter, title=post_data.title, text=post_data.text)
        self.posts.append(new_post)
        self.counter += 1
        return new_post

    def update_post(self, post_id, title, text):
        post = self.get_post_by_id(post_id)
        if post:
            post.title = title
            post.text = text
            return post
        return None

    def delete_post(self, post_id):
        post = self.get_post_by_id(post_id)
        if post:
            self.posts.remove(post)
            return True
        return False
