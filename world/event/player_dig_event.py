from world.event.world_event import WorldEvent


class PlayerDigEvent(WorldEvent):
    def __init__(self, button, location, player):
        self.button = button
        self.location = location
        self.player = player
        super().__init__()
