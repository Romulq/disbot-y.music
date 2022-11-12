from yandex_music import Client
import logging

import config

logging.basicConfig(level=logging.DEBUG)


client = Client(config.TOKEN).init()
client.users_likes_tracks()[0].fetch_track().download(filename='test.mp3')
