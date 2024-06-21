from manim import *


class CustomScene(Scene):
    def custom_title(self, title, wait=1):
        scene_title = Text(title, color=WHITE)
        self.play(Write(scene_title))
        self.wait(wait)
        self.play(FadeOut(scene_title))