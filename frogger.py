import arcade

SCREEN_HEIGHT = 560
SCREEN_WIDTH = 800
ROAD_SECTION_HEIGHT = SCREEN_HEIGHT / 8


class Frogger(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Frogger")
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.PURPLE)

    def on_draw(self):
        arcade.start_render()
        self._build_road()
        self._draw_score_area()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            exit()

    def _build_road(self):
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 6 * ROAD_SECTION_HEIGHT, ROAD_SECTION_HEIGHT,
                                          arcade.color.BLACK)

        def _stripe_road(height, offset=0):
            for x in range(0, SCREEN_WIDTH + 50, 100):
                arcade.draw_rectangle_filled(x + offset, height, 40, 2, arcade.color.WHITE)

        _stripe_road(ROAD_SECTION_HEIGHT * 2, 50)
        _stripe_road(ROAD_SECTION_HEIGHT * 3)
        _stripe_road(ROAD_SECTION_HEIGHT * 4, 50)
        _stripe_road(ROAD_SECTION_HEIGHT * 5)

    def _draw_score_area(self):
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 7 * ROAD_SECTION_HEIGHT, arcade.color.BLACK)
        arcade.draw_text("Score: ", 10, SCREEN_HEIGHT - 40, arcade.color.WHITE, 20)


window = Frogger()
arcade.run()
