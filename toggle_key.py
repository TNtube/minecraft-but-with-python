import pygame


class ToggleKey:
    def __init__(self, key):
        self._key = key
        self._clock = pygame.time.Clock()

    def is_pressed(self):
        if self._clock.get_time() > 200:
            if pygame.key.get_pressed()[self._key]:
                self._clock.tick()
                return True
        return False
