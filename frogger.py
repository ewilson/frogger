import arcade

SCREEN_HEIGHT = 560
SCREEN_WIDTH = 800
ROAD_SECTION_HEIGHT = SCREEN_HEIGHT / 8


class Frog(arcade.Sprite):

    def __init__(self, x_pos, y_pos):
        super().__init__(center_x=x_pos, center_y=y_pos)
        self.textures.append(arcade.load_texture("assets/frog/frog-animation/frog3.png", scale=0.4))
        self.set_texture(0)

    def jump(self, direction):
        jump_distance = ROAD_SECTION_HEIGHT / 2
        if direction == arcade.key.UP:
            if self.center_y < jump_distance * 13:
                self.angle = 0
                self.center_y += jump_distance
        if direction == arcade.key.DOWN:
            if self.center_y > jump_distance:
                self.angle = 180
                self.center_y -= jump_distance
        if direction == arcade.key.RIGHT:
            if self.center_x < SCREEN_WIDTH - 2 * jump_distance:
                self.angle = -90
                self.center_x += jump_distance * 1.2
        if direction == arcade.key.LEFT:
            if self.center_x > 2 * jump_distance:
                self.angle = 90
                self.center_x -= jump_distance * 1.2


class Frogger(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Frogger")
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.PURPLE)

    def setup(self):
        self.frog = Frog(SCREEN_WIDTH/2, ROAD_SECTION_HEIGHT/2)

    def on_draw(self):
        arcade.start_render()
        self._build_road()
        self._draw_score_area()
        self.frog.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            exit()
        if key in [arcade.key.UP, arcade.key.DOWN, arcade.key.RIGHT, arcade.key.LEFT]:
            self.frog.jump(key)

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
window.setup()
arcade.run()
