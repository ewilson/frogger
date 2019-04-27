import arcade

SCREEN_HEIGHT = 560
SCREEN_WIDTH = 800
ROAD_SECTION_HEIGHT = SCREEN_HEIGHT / 8
score = 0


class Car(arcade.Sprite):

    def __init__(self, image_file, x_pos, y_pos, angle, speed):
        super().__init__(image_file, 1, center_x=x_pos, center_y=y_pos)
        self.speed = speed
        self.angle = angle

    def update(self):
        self.center_x += self.speed
        if self.right < 0:
            self.left = SCREEN_WIDTH
        if self.left > SCREEN_WIDTH:
            self.right = 0


class Frog(arcade.Sprite):

    def __init__(self, x_pos, y_pos):
        super().__init__(center_x=x_pos, center_y=y_pos)
        self.textures.append(arcade.load_texture("assets/frog/frog-animation/frog3.png", scale=0.4))
        self.set_texture(0)
        self.jump_sound = arcade.load_sound("assets/sounds/jump.mp3")
        self.success_sound = arcade.load_sound("assets/sounds/success.mp3")
        self.progress = 1

    def jump(self, direction):
        arcade.play_sound(self.jump_sound)
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
        self._update_score()

    def _update_score(self):
        if self.center_y > ROAD_SECTION_HEIGHT * self.progress:
            global score
            self.progress += 1
            score += 10
            if self.progress == 7:
                arcade.play_sound(self.success_sound)
                score += 40


class Frogger(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Frogger")
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.PURPLE)
        self.cars = arcade.SpriteList()
        self.car_speed = 1

    def setup(self):
        self.frog = Frog(SCREEN_WIDTH/2, ROAD_SECTION_HEIGHT/2)
        self._car_setup()

    def on_draw(self):
        arcade.start_render()
        self._build_road()
        self._draw_score_area()
        self.frog.draw()
        self.cars.draw()

    def on_update(self, delta_time):
        self.cars.update()

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

    def _car_setup(self):
        # Row one cars
        first_lane = ROAD_SECTION_HEIGHT * 1.5
        self.cars.append(Car("assets/cars/car_red_small_4.png", 100, first_lane, -90, 2 * self.car_speed))
        self.cars.append(Car("assets/cars/car_red_small_4.png", 250, first_lane, -90, 2 * self.car_speed))
        self.cars.append(Car("assets/cars/car_red_small_4.png", 700, first_lane, -90, 2 * self.car_speed))
        # Row two cars
        second_lane = ROAD_SECTION_HEIGHT * 2.5
        self.cars.append(Car("assets/cars/car_yellow_small_1.png", 50, second_lane, 90, -5 * self.car_speed))
        # Row three cars
        third_lane = ROAD_SECTION_HEIGHT * 3.5
        self.cars.append(Car("assets/cars/car_blue_small_2.png", 50, third_lane, -90, 3 * self.car_speed))
        self.cars.append(Car("assets/cars/car_blue_small_2.png", 160, third_lane, -90, 3 * self.car_speed))
        self.cars.append(Car("assets/cars/car_blue_small_2.png", 500, third_lane, -90, 3 * self.car_speed))
        self.cars.append(Car("assets/cars/car_blue_small_2.png", 610, third_lane, -90, 3 * self.car_speed))
        # Row four cars
        fourth_lane = ROAD_SECTION_HEIGHT * 4.5
        self.cars.append(Car("assets/cars/car_red_small_3.png", 600, fourth_lane, 90, -4 * self.car_speed))
        self.cars.append(Car("assets/cars/car_red_small_3.png", 200, fourth_lane, 90, -4 * self.car_speed))
        # Row five cars
        fifth_lane = ROAD_SECTION_HEIGHT * 5.5
        self.cars.append(Car("assets/cars/car_yellow_small_5.png", 0, fifth_lane, -90, 4 * self.car_speed))
        self.cars.append(Car("assets/cars/car_yellow_small_5.png", 150, fifth_lane, -90, 4 * self.car_speed))
        self.cars.append(Car("assets/cars/car_yellow_small_5.png", 500, fifth_lane, -90, 4 * self.car_speed))

    def _draw_score_area(self):
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 7 * ROAD_SECTION_HEIGHT, arcade.color.BLACK)
        global score
        arcade.draw_text("Score: " + str(score), 10, SCREEN_HEIGHT - 40, arcade.color.WHITE, 20)


window = Frogger()
window.setup()
arcade.run()
