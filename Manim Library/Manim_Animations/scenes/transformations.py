from manim import *

class MovingDot(Scene):
    def construct(self):
        dot = Dot()
        self.play(FadeIn(dot))
        self.play(dot.animate.shift(RIGHT*3))
        self.play(dot.animate.shift(UP*2))
        self.play(FadeOut(dot))
