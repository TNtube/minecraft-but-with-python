import glm
import pygame
from pygame.locals import *

from typing import Any

from math_utils.ray import Ray
from player import Player
from renderer.renderer import Renderer
from states.state_base import StateBase
from world.block.block_id import BlockId
from world.event.player_dig_event import PlayerDigEvent
from world.world import World


class StatePlaying(StateBase):
    def __init__(self, application: Any):
        super().__init__(application)
        self._player: Player = Player()
        self._world: World = World(application.get_camera())
        self._clock = pygame.time.Clock()
        application.get_camera().hook_entity(self._player)

    def update(self, dt: float) -> None:
        if self._player.position.x < 0:
            self._player.position.x = 0
        if self._player.position.z < 0:
            self._player.position.z = 0

        self._player.update(dt, self._world)
        self._world.update(self.app.get_camera())

    def handle_input(self) -> None:
        self._player.handle_input()

        last_position: glm.vec3 = glm.vec3(0, 0, 0)
        ray: Ray = Ray(self._player.position, self._player.rotation)

        while ray.get_length() < 6:
            x, y, z = ray.get_end()

            block = self._world.get_block(x, y, z)
            block_id = block.id
            if block_id != BlockId.AIR and block_id != BlockId.WATER:
                if self._clock.get_time() > 200:
                    if pygame.mouse.get_pressed()[0]:
                        self._clock.tick()
                        self._world.add_event(PlayerDigEvent, pygame.BUTTON_LEFT, ray.get_end(), self._player)
                        break
                    elif pygame.mouse.get_pressed()[2]:
                        self._clock.tick()
                        self._world.add_event(PlayerDigEvent, pygame.BUTTON_RIGHT, last_position, self._player)
                        break

            last_position = ray.get_end()
            ray.step(0.1)

    def render(self, renderer: Renderer) -> None:
        self._world.render(renderer, self.app.get_camera())

    def on_enter(self) -> None:
        self.app.mouse_off()
