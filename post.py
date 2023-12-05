import requests

class Post:
    def __init__(self, num):
        self.response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
        self.num = num

    def getPost(self, num):
        return self.response.json()[num]