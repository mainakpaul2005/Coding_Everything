from manim import *

class HelloWorld(Scene):
    def construct(self):
        # Create a text object
        text = Text("Hello, Manim!", font_size=72)
        
        # Animate writing the text
        self.play(Write(text))
        
        # Pause for 1 second
        self.wait(1)
        
        # Fade out the text
        self.play(FadeOut(text))
