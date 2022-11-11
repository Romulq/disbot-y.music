from yandex_music import Client
import logging

logging.basicConfig(level=logging.DEBUG)


client = Client('y0_AgAAAAAtx9z7AAG8XgAAAADTrAfQOcc8jVjzSpeqDA6w8hTPHyjA3kU').init()
client.users_likes_tracks()[].fetch_track().download(filename='test.mp3')
