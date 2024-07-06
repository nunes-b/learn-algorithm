"""
What do I want to know by creating this game?
OOP with Python
how to create games with the pygame library
and something new.
"""

import pygame
import random

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

clock = pygame.time.Clock()
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


class Snake:
    def __init__(self):
        self.snake_block = 10
        self.snake_List = []
        self.Length_of_snake = 1
        self.x = width / 2
        self.y = height / 2
        self.x_change = 0
        self.y_change = 0

    def move(self, direction):
        if direction == "LEFT":
            self.x_change = -self.snake_block
            self.y_change = 0
        elif direction == "RIGHT":
            self.x_change = self.snake_block
            self.y_change = 0
        elif direction == "UP":
            self.y_change = -self.snake_block
            self.x_change = 0
        elif direction == "DOWN":
            self.y_change = self.snake_block
            self.x_change = 0

    def update_position(self):
        self.x += self.x_change
        self.y += self.y_change

    def grow(self):
        self.Length_of_snake += 1

    def draw(self):
        for x in self.snake_List:
            pygame.draw.rect(
                window, black, [x[0], x[1], self.snake_block, self.snake_block]
            )

    def add_segment(self):
        self.snake_List.append([self.x, self.y])
        if len(self.snake_List) > self.Length_of_snake:
            del self.snake_List[0]

    def check_collision(self):
        for segment in self.snake_List[:-1]:
            if segment == [self.x, self.y]:
                return True
        if self.x >= width or self.x < 0 or self.y >= height or self.y < 0:
            return True
        return False


class Food:
    def __init__(self):
        self.snake_block = 10
        self.x = round(random.randrange(0, width - self.snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, height - self.snake_block) / 10.0) * 10.0

    def draw(self):
        pygame.draw.rect(
            window, green, [self.x, self.y, self.snake_block, self.snake_block]
        )

    def relocate(self):
        self.x = round(random.randrange(0, width - self.snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, height - self.snake_block) / 10.0) * 10.0


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        self.game_close = False

    def run(self):
        while not self.game_over:
            while self.game_close:
                window.fill(blue)
                self.show_message("You Lost! Press Q-Quit or C-Play Again", red)
                pygame.display.update()
                self.handle_game_over_events()

            self.handle_events()
            self.update_game_state()
            self.render()

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.move("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.move("RIGHT")
                elif event.key == pygame.K_UP:
                    self.snake.move("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.move("DOWN")

    def handle_game_over_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.game_over = True
                    self.game_close = False
                if event.key == pygame.K_c:
                    self.__init__()

    def update_game_state(self):
        self.snake.update_position()
        self.snake.add_segment()
        if self.snake.check_collision():
            self.game_close = True
        if self.snake.x == self.food.x and self.snake.y == self.food.y:
            self.food.relocate()
            self.snake.grow()

    def render(self):
        window.fill(blue)
        self.food.draw()
        self.snake.draw()
        pygame.display.update()

    def show_message(self, msg, color):
        mesg = font_style.render(msg, True, color)
        window.blit(mesg, [width / 6, height / 3])


if __name__ == "__main__":
    game = Game()
    game.run()
