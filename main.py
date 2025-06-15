import pygame

from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    # ASTEROID_MIN_RADIUS,
    # ASTEROID_KINDS,
    # ASTEROID_SPAWN_RATE,
    # ASTEROID_MAX_RADIUS,
)
from player import Player


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        player.draw(screen)

        # final
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
