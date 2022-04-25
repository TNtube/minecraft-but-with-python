import glm
import pygame

from Entity import Entity
from item.item_stack import ItemStack
from item.material import MaterialBlock, Material
from toggle_key import ToggleKey
from world.world import World


class Player(Entity):
    def __init__(self):
        super().__init__(glm.vec3(1500, 125, 1500), glm.vec3(0, 0, 0), glm.vec3(0.5, 1.5, 0.5))
        self.item_down: ToggleKey = ToggleKey(pygame.K_DOWN)
        self.item_up: ToggleKey = ToggleKey(pygame.K_UP)
        self._is_on_ground = False
        self.items: list[ItemStack] = []
        self.held_item_index = 0

        for i in range(5):
            self.items.append(ItemStack(MaterialBlock.NOTHING, 0))

    def update(self, dt: float, world: World):
        pass

    def handle_input(self):
        pass

    def collide(self, world: World, velocity: glm.vec3, dt: float):
        pass

    def add_item(self, material):
        material_id: Material.ID = material.id
        for i in range(len(self.items)):
            if self.items[i].material.id == material_id:
                left_over = self.items[i].add(1)
                return
            elif self.items[i].material.id == Material.ID.NOTHING:
                self.items[i] = ItemStack(material, 1)
                return

    def render(self, renderer):
        pass

    def keyboard_input(self, key):
        pass

    def mouse_input(self, mouse_pos):
        pass



