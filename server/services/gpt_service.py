import requests


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
