from getter import SteamUserCountGetter
from sender import WebhookSender
import time
import json

with open("config.json", "r") as f:
    games = json.load(f)

class Game():
    def __init__(self, **kwargs):
        self.getter = SteamUserCountGetter(**kwargs)
        self.sender = WebhookSender(**kwargs)
        self.threshold = kwargs.pop("threshold", 1)
        self.webhook_title = kwargs.pop("webhook_title", "Playercount")
        self.webhook_message = kwargs.pop("webhook_message", None)
        self.kwargs = kwargs
        self.previous = 0
    
    def get_and_send(self):
        result = self.getter.get()
        self.previous = result
        code = self.send(result)
        return code
    
    def send(self, message):
        return self.sender.send(
                description=f"`{message}` Players",
                title=self.webhook_title,
                message=self.webhook_message)
            
    def send_if_different(self):
        result = self.getter.get()
        diff = result - self.previous
        if diff >= self.threshold: # at least threshold more players than before
            self.previous = result
            return self.send(result)
        elif abs(diff) >= self.threshold: # at least threshold less players than before
            self.previous = result
            return self.send(result)
        return 304

games = [Game(**game) for game in games]
for game in games:
    game.get_and_send()

while True:
    for game in games:
        print(game.send_if_different())
    time.sleep(4)