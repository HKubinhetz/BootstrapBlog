import requests


def get_posts():
    with requests.Session() as rq:
        return rq.get("https://api.npoint.io/c790b4d5cab58020d391").json()
