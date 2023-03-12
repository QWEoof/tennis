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
    score1 = 0
    score2 = 0
    if ball.X - ball.RADIUS < board1.x:
        score += 1
    elif ball.x + ball.RADIUS > board2.x:
        score1 += 1
        ball.x





