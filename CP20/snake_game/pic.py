from turtle import Turtle,Screen
import pygame
pygame.init()

pygame.display.set_caption("fuck")

back = pygame.image.load("D:/python_project/lec/CP20/snake_game/back.png")
screen = Screen()

screen_width= 600
screen_height= 600
screen = pygame.display.set_mode((screen_width,screen_height))

screen.blit(back,(0,0))
pygame.display.update()