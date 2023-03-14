import pygame
from data import *


class Board(pygame.Rect):
    def __init__(self, x, y, width, height, image, speed):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.SPEED = speed
        self.MOVE = {"UP": False, "DOWN": False}

    def move(self):
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED
        
        elif self.MOVE["DOWN"] and self.y < 400:
            self.y += self.SPEED
class Ball():
    def __init__(self, x, y, radius, color, image, speed):
        self.X = x
        self.Y = y
        self.RADIUS = radius
        self.COLOR = color
        self.IMAGE = image
        self.SPEED = speed
        self.ANGLE = self.SPEED
        self.VERTICAL = 0
        self.DIRECTION = True if self.SPEED < 0 else False
        self.WIN = True
    def move(self, board):
        
        if self.Y - self.RADIUS <= 0 or self.Y + self.RADIUS >= set_win["HEIGHT"]:
            self.VERTICAL *= -1
        elif board.collidepoint(self.X - self.RADIUS, self.Y) or board.collidepoint(self.X + self.RADIUS, self.Y):
            if board.MOVE["UP"]:
                self.VERTICAL = - self.SPEED
                self.SPEED = 5
            if board.MOVE["DOWN"]:
                self.VERTICAL = self.SPEED
                self.SPEED = 5
            self.ANGLE *= -1
            self.DIRECTION = not self.DIRECTION
        self.X += self.ANGLE
        self.Y += self.VERTICAL



def win_lose_score(window, ball, board1, board2):
    if ball.X - ball.RADIUS < board1.x - ball.RADIUS:
        win_blue = pygame.font.SysFont("Arial", 30)
        render_win_blue = win_blue.render("Переможець синій", True, (0, 0, 255))
        window.blit(render_win_blue, (300, 200))
        if ball.WIN:
            pass
        pygame.draw.rect(window, (252, 142, 24), button_list[0])
        pygame.draw.rect(window, (252, 142, 24), button_list[1])
        window.blit(button_list[2].render("Start", True, (0,0,0)), (set_win["WIDTH"] // 2 - set_button["WIDTH"] // 2 + 70,
                                                                     set_win["HEIGHT"] // 2 - set_button["HEIGHT"] - 30))
        window.blit(button_list[3].render("Stop", True, (0,0,0)), (set_win["WIDTH"] // 2 - set_button["WIDTH"] // 2 + 70,
                                                                     set_win["HEIGHT"] // 2 - set_button["HEIGHT"] + 100))
    elif ball.X + ball.RADIUS > board2.x + ball.RADIUS:
        win_red = pygame.font.SysFont("Arial", 30)
        render_win_red = win_red.render("Переможець червоний", True, (255, 0, 0))
        window.blit(render_win_red, (300, 200))
        pygame.draw.rect(window, (252, 142, 24), button_list[0])
        pygame.draw.rect(window, (252, 142, 24), button_list[1])
        window.blit(button_list[2].render("Start", True, (0,0,0)), (set_win["WIDTH"] // 2 - set_button["WIDTH"] // 2 + 70,
                                                                     set_win["HEIGHT"] // 2 - set_button["HEIGHT"] - 30))
        window.blit(button_list[3].render("Stop", True, (0,0,0)), (set_win["WIDTH"] // 2 - set_button["WIDTH"] // 2 + 70,
                                                                     set_win["HEIGHT"] // 2 - set_button["HEIGHT"] + 100))
def start(ball, board1, board2):
    ball.SPEED = set_ball["SPEED"]
    ball.X = set_win["WIDTH"] // 2
    ball.Y = set_win["HEIGHT"] // 2
    ball.ANGLE = ball.SPEED
    ball.VERTICAL = 0
    ball.DIRECTION = True if ball.SPEED < 0 else False
    board1.y = start_game["RIGHT_PLAYER"][1]
    board2.y = start_game["LEFT_PLAYER"][1]





