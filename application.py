import pygame

from context import Context
from renderer.renderer import Renderer
from states.state_base import StateBase
from camera import Camera
from states.state_playing import StatePlaying
from world.block.block_database import BlockDatabase


class Application:
    def __init__(self, name: str):
        self._states: list[StateBase] = []
        self.renderer: Renderer = Renderer()
        self._camera: Camera = Camera()
        self._context: Context = Context(name)
        self._is_pop_state: bool = False
        self.is_running: bool = True

        BlockDatabase.get()
        self.push_state(StatePlaying, self)

    def run(self):
        clock = pygame.time.Clock()
        while self.is_running and not len(self._states) == 0:
            dt = clock.tick() / 1000
            state = self._states[-1]

            state.handle_input()
            state.update(dt)
            self._camera.update()

            state.render(self.renderer)
            self.renderer.finish_render(self.get_screen(), self._camera)
            self._handle_events()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False
                    pygame.quit()
                    exit()

    def push_state(self, type_state: type, *args):
        self._states.append(type_state(*args))
        s = self._states[-1]
        s.on_enter()

    def pop_state(self):
        self._is_pop_state = True

    def get_camera(self) -> Camera:
        return self._camera

    def get_screen(self):
        return self._context.screen

    @staticmethod
    def mouse_on() -> None:
        pygame.mouse.set_visible(True)

    @staticmethod
    def mouse_off() -> None:
        pygame.mouse.set_visible(False)



