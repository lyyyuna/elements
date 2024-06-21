from manim import *
from util import CustomScene

class Solution(CustomScene):
    def construct(self):
        self.custom_title("公设 1")

        postlutate1 = Text("从任一点到任一点可作一条直线", color='#FFFFFF')
        self.play(Write(postlutate1))
        self.wait(2)
        self.play(FadeOut(postlutate1))

        title = Text("公设 2", color='#FFFFFF')
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        postlutate2 = Text("一条有限直线可沿直线继续延长", color='#FFFFFF')
        self.play(Write(postlutate2))
        self.wait(2)
        self.play(FadeOut(postlutate2))

        title = Text("公设 3", color='#FFFFFF')
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        postlutate3 = Text("以任一点为心和任意距离可以作圆", color='#FFFFFF')
        self.play(Write(postlutate3))
        self.wait(2)
        self.play(FadeOut(postlutate3))

        title = Text("公设 4", color='#FFFFFF')
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        postlutate4 = Text("所有直角都彼此相等", color='#FFFFFF')
        self.play(Write(postlutate4))
        self.wait(2)
        self.play(FadeOut(postlutate4))

        title = Text("公设 5", color='#FFFFFF')
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        postlutate5_1 = Text("一直线与两条直线相交", color='#FFFFFF')
        postlutate5_2 = Text("若在同侧的两内角之和小于两直角", color='#FFFFFF')
        postlutate5_3 = Text("则这两条直线无定限延长后在该侧相交", color='#FFFFFF')
        postlutate5 = VGroup(postlutate5_1, postlutate5_2, postlutate5_3).arrange(direction=DOWN, aligned_edge=ORIGIN)
        self.play(Write(postlutate5))
        self.wait(2)
        self.play(FadeOut(postlutate5))