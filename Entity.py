import glm

from physics.aabb import AABB


class Entity:
    def __init__(self, position: glm.vec3 = None, rotation: glm.vec3 = None, box: glm.vec3 = None):
        self.position: glm.vec3 = position or glm.vec3(0.0, 0.0, 0.0)
        self.rotation: glm.vec3 = rotation or glm.vec3(0.0, 0.0, 0.0)
        self.velocity: glm.vec3 = glm.vec3(0.0, 0.0, 0.0)

        self.box: AABB = AABB(box or glm.vec3(0.0, 0.0, 0.0))
