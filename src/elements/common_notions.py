from manim import *

class Solution(Scene):
    def construct(self):
        title = Text("公理 1", color=WHITE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        common_notion1 = Text("等于同量的量也彼此相等", color=WHITE)
        self.play(Write(common_notion1))
        self.wait(2)
        self.play(FadeOut(common_notion1))

        title = Text("公理 2", color=WHITE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        common_notion2 = Text("等量加等量，其和相等", color=WHITE)
        self.play(Write(common_notion2))
        self.wait(2)
        self.play(FadeOut(common_notion2))

        title = Text("公理 3", color=WHITE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        common_notion3 = Text("等量减等量，其差相等", color=WHITE)
        self.play(Write(common_notion3))
        self.wait(2)
        self.play(FadeOut(common_notion3))

        title = Text("公理 4", color=WHITE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        common_notion4 = Text("彼此重合的东西彼此相等", color=WHITE)
        self.play(Write(common_notion4))
        self.wait(2)
        self.play(FadeOut(common_notion4))

        title = Text("公理 5", color=WHITE)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        common_notion5 = Text("整体大于部分", color=WHITE)
        self.play(Write(common_notion5))
        self.wait(2)
        self.play(FadeOut(common_notion5))