from google import genai


class GoogleAIClientInterface:
    def generate_content(self, model, config, contents):
        pass

class GoogleAIClient(GoogleAIClientInterface):
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
    
    def generate_content(self, model, config, contents):
        return self.client.models.generate_content(
            model=model, 
            config=config,
            contents=contents
        )