class BlogPostService:
    def __init__(self, repository):
        self.repository = repository

    def get_all_posts(self):
        return self.repository.get_all_posts()

    def get_post_by_id(self, post_id):
        return self.repository.get_post_by_id(post_id)

    def create_post(self, post_data):
        return self.repository.create_post(post_data)

    def update_post(self, post_id, title, text):
        return self.repository.update_post(post_id, title, text)

    def delete_post(self, post_id):
        return self.repository.delete_post(post_id)
