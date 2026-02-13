import arcade
import requests

WIN_W = 600
WIN_H = 400
API_KEY = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"

lon, lat = float(input("Догота: ")) , float(input("Широта: ")) #37.677751, 55.757718
width, height = 600, 400
zoom = int(input("Масштабирования карты (0-21): "))
url = (
    f"https://static-maps.yandex.ru/v1?"
    f"ll={lon},{lat}&size={width},{height}&z={zoom}"
    f"&apikey={API_KEY}"
)
response = requests.get(url)

with open("map.png", "wb") as f:
    f.write(response.content)


class API(arcade.Window):
    def __init__(self,WIN_W, WIN_H):
        super().__init__(WIN_W, WIN_H)
        self.WINDOW_WIDTH = WIN_W
        self.WINDOW_HEIGHT = WIN_H
        self.ui_camera = arcade.Camera2D()
        self.background = arcade.Sprite("map.png")

        self.background.center_x = WIN_W // 2
        self.background.center_y = WIN_H // 2


    def on_draw(self):
        self.ui_camera.use()
        self.clear()
        arcade.draw_sprite(self.background)

app = API(WIN_W, WIN_H)
arcade.run()