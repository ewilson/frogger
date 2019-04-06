import arcade

SCREEN_HEIGHT = 560
SCREEN_WIDTH = 800


class Frogger(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Frogger")
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.PURPLE)

    def on_draw(self):
        arcade.start_render()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            exit()


window = Frogger()
arcade.run()
