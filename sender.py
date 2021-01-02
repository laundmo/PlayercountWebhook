import requests


class WebhookSender():
    def __init__(self, **kwargs):
        self.session = requests.Session()
        self.webhook_url = kwargs.pop('webhook_url', None)
        self.image = kwargs.pop('webhook_image', None)
        self.username = kwargs.pop('webhook_username', "Webhook")
    
    def send(self, description="Default Description", title="Default Title", message=None):
        embed = {
            "description": description,
            "title": title
            }

        data = {
            "username": self.username,
            "avatar_url": self.image,
            "embeds": [
                embed
                ],
        }
        if message:
            data["content"] = message

        headers = {
            "Content-Type": "application/json"
        }

        result = self.session.post(self.webhook_url, json=data, headers=headers)
        if 200 <= result.status_code < 300:
            return result.status_code
        result.raise_for_status()