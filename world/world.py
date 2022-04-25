from camera import Camera
from renderer.renderer import Renderer
from world.block.chunk_block import ChunkBlock


class World:
    def __init__(self, camera: Camera):
        pass

    def update(self, camera: Camera):
        pass

    def render(self, renderer: Renderer, camera: Camera):
        pass

    def get_block(self, x, y, z) -> ChunkBlock:
        return ChunkBlock()

    def add_event(self, type_event: type, *args):
        pass
