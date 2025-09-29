# main.py
import pygame
from player import Player

# Alustus
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Echo Protocol – Kammio 01")
clock = pygame.time.Clock()

# Värit
BLACK = (10, 10, 10)
GRAY = (100, 100, 100)

# Pelaaja
player = Player(pos=(100, 100))
player_group = pygame.sprite.Group()
player_group.add(player)

# Este (seinä)
wall = pygame.Rect(300, 200, 200, 40)

# Päälooppi
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Liikkuminen
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Törmäystarkistus
    if player.rect.colliderect(wall):
        player.undo_move()  # Palauttaa edellisen sijainnin

    # Piirto
    screen.fill(BLACK)
    pygame.draw.rect(screen, GRAY, wall)
    player_group.draw(screen)
    pygame.display.flip()

pygame.quit()
