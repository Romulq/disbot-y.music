from yandex_music import Client
import logging

logging.basicConfig(level=logging.DEBUG)


client = Client('token').init()
client.users_likes_tracks()[].fetch_track().download(filename='test.mp3')
