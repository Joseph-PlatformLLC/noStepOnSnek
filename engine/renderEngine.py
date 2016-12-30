import pygame
import components

class RenderEngine():
    def __init__(self):
        self.colors = components.Colors()


    def updateSneks(self, sneks):
        self.renderOverlay()
