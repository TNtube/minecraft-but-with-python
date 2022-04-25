import pygame
import OpenGL.GL as GL


class Context:
    def __init__(self, name: str):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 720), pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
        pygame.display.set_caption(name)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glViewport(0, 0, 1280, 720)

        GL.glCullFace(GL.GL_BACK)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
