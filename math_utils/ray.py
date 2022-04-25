import glm


class Ray:
    def __init__(self, origin: glm.vec3, direction: glm.vec3):
        self.origin = origin
        self.direction = direction
        self.inv_direction = 1.0 / direction

    def get_length(self) -> float:
        return 0

    def step(self, t: float) -> glm.vec3:
        return glm.vec3(0)

    def get_end(self) -> glm.vec3:
        return glm.vec3(0)
