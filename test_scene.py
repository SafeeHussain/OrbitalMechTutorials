# test_scene.py
from manim import *

class TestScene(Scene):
    def construct(self):
        title = MathTex(r"\text{Manim Test: } y = \sin(x)").to_edge(UP)

        axes = Axes(
            x_range=[-2 * PI, 2 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=6,
            y_length=3,
        )

        sin_curve = axes.plot(lambda x: np.sin(x), color=BLUE)
        label = MathTex(r"y = \sin(x)").next_to(axes, DOWN)

        self.add(axes, sin_curve, label, title)
        self.wait(0.5)