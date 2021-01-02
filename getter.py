import requests


class SteamUserCountGetter():
    URL = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"
    def __init__(self, **kwargs):
        self.session = requests.Session()
        self.game_id = kwargs.pop('game_id', None)
    
    def get(self):
        result = self.session.get(self.URL, params={"appid": self.game_id})
        if 200 <= result.status_code < 300:
            return result.json()["response"]["player_count"]
        result.raise_for_status()