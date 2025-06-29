import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main ():
  pygame.init()
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)

  player = Player(
   SCREEN_WIDTH / 2,
   SCREEN_HEIGHT / 2
  )

  AsteroidField()


  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return

    screen.fill("black")
    updatable.update(dt)

    for a in asteroids:
      for b in shots:
        if a.collide(b):
          a.split()

      if a.collide(player):
        print("Game over!")
        exit(0)

    for obj in drawable:
      obj.draw(screen)

    pygame.display.flip()
    dt = clock.tick(120) / 1000

if __name__ == "__main__":
  main()