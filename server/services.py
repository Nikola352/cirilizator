import requests

from models import NewBlogPost, NewUser


class BlogPostService:
    def __init__(self, repository):
        self.repository = repository

    def get_all_posts(self):
        return self.repository.get_all_posts()

    def get_paginated_posts(self, page, per_page):
        return self.repository.get_paginated_posts(page, per_page)

    def get_post_by_id(self, post_id):
        return self.repository.get_post_by_id(post_id)

    def create_post(self, title, text, category, thumbnail):
        post_data = NewBlogPost(title=title, text=text, category=category, thumbnail=thumbnail)
        return self.repository.create_post(post_data)

    def update_post(self, post_id, title, text):
        return self.repository.update_post(post_id, title, text)

    def delete_post(self, post_id):
        return self.repository.delete_post(post_id)


class AdminUserService:
    def __init__(self, repository):
        self.repository = repository

    def get_user_by_username(self, username):
        return self.repository.get_user_by_username(username)

    def register(self, username, password):
        user_data = NewUser(username=username, password=password)
        self.repository.register(user_data)


class GPTService:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def call_gpt_api(self, prompt):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
        }

        request_data = {
            'prompt': prompt,
            'max_tokens': 1
        }

        response = requests.post(self.api_url, headers=headers, json=request_data)

        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['text']
        else:
            raise Exception(f'Error calling GPT-3 API: {response.text}')
        

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
    
    def get_matching_font(self, font): # TODO: implement
        return self.repository.get_random_font()
        