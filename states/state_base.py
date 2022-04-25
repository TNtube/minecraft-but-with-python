from typing import Any

import pygame

from renderer.renderer import Renderer


class StateBase:
    def __init__(self, application: Any):
        self.app = application

    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def handle_input(self) -> None:
        pass

    def update(self, dt: float) -> None:
        pass

    def render(self, renderer: Renderer) -> None:
        pass

    def on_enter(self) -> None:
        pass
