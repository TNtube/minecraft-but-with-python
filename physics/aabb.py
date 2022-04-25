import glm


class AABB:
    def __init__(self, dimensions: glm.vec3):
        self.dimensions: glm.vec3 = dimensions
        self.position: glm.vec3 = glm.vec3(0.0, 0.0, 0.0)
