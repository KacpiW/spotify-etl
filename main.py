import base64
import requests
from requests.api import request

# Generate your credentials here : https://developer.spotify.com/dashboard/login
# Note: You need to have a spotify account

CLIENT_ID = ""      # your Spotify client id
CLIENT_SECRET = ""  # your Spotify client secret


class SpotifyExtract:
    def __init__(self, client_id=None, client_secret=None, redirect_uri=None) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

    @property
    def auth_str(self):
        return "{}:{}".format(self.client_id, self.client_secret)

    def get_auth_token(self):

        # Encode to base 64 string format according to requirements
        b64_auth_str = base64.urlsafe_b64encode(
            (self.auth_str).encode()).decode()

        body = {"grant_type": "client_credentials"}
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Authorization": "Basic %s" % b64_auth_str}

        endpoint = "https://accounts.spotify.com/api/token"

        response = requests.post(
            url=endpoint, data=body, headers=headers).json()
        return response["access_token"]


if __name__ == "__main__":
    extractor = SpotifyExtract(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    access_token = extractor.get_auth_token()
