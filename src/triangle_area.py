from manim import *


class TriangleAreaInteriorAltitude(Scene):
    def construct(self):
        A = np.array([-2, 2, 0])
        B = np.array([2, 0, 0])
        C = np.array([-2, 0, 0])
        D = np.array([-3, 0, 0])

        triangle = Polygon(A, B, C, color=BLUE)
        altitude = Polygon(A, D, C, color=YELLOW)

        label_A = Tex("A").next_to(A, UP)
        label_B = Tex("C").next_to(B, DOWN)
        label_C = Tex("D").next_to(C, DOWN)
        label_D = Tex("B").next_to(D, DOWN)

        triangle_ACD = Polygon(A, C, D, color=GREEN, fill_opacity=0.4)
        triangle_ABD = Polygon(A, B, D, color=RED, fill_opacity=0.4)

        elements = VGroup(
            triangle, altitude,
            triangle_ACD, triangle_ABD,
            label_A, label_B, label_C, label_D
        )

        elements.shift(LEFT * 3.5)

        self.play(Create(triangle), run_time=2)
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)

        self.play(Create(altitude), Write(label_D))
        self.wait(1)

        self.play(FadeIn(triangle_ACD), FadeIn(triangle_ABD))
        self.wait(1)

        formula1 = MathTex(
            r"\text{Area}_{ABC} = \text{Area}_{ACD} + \text{Area}_{ABD}"
        ).to_edge(UP).shift(RIGHT * 2)
        self.play(Write(formula1))
        self.wait(1)

        formula2 = MathTex(
            r"= \frac{1}{2} \cdot CD \cdot AD + \frac{1}{2} \cdot DB \cdot AD"
        ).next_to(formula1, DOWN * 1.5)
        self.play(Write(formula2))
        self.wait(1)

        formula3 = MathTex(
            r"= \frac{1}{2} \cdot AD \cdot (CD + DB)"
        ).next_to(formula2, DOWN * 1.5)
        self.play(Write(formula3))
        self.wait(1)

        formula4 = MathTex(
            r"= \frac{1}{2} \cdot AD \cdot CB"
        ).next_to(formula3, DOWN * 1.5)
        self.play(Write(formula4))
        self.wait(1)

        formula_final = MathTex(
            r"\text{Area}_{ABC} = \frac{1}{2} \cdot \text{base} \cdot \text{height}"
        ).next_to(formula4, DOWN * 1.5).set_color(YELLOW)
        self.play(Write(formula_final))
        self.wait(2)

        conclusion = Tex(
            "The formula is also valid when the height is inside the triangle."
        ).next_to(formula_final, DOWN * 1.5).shift(LEFT * 1.5).set_color(GREEN)
        self.play(Write(conclusion))
        self.wait(3)


class TriangleAreaExteriorAltitude(Scene):
    def construct(self):
        A = np.array([-2, 2, 0])
        B = np.array([2, -1, 0])
        C = np.array([0, -1, 0])
        D = np.array([-2, -1, 0])

        triangle = Polygon(A, B, C, color=BLUE)
        altitude1 = Line(A, D, color="#FFFF99")
        altitude2 = Line(C, D, color="#FFFF99")

        label_A = Tex("A").next_to(A, UP)
        label_B = Tex("B").next_to(B, DOWN)
        label_C = Tex("C").next_to(C, DOWN)
        label_D = Tex("D").next_to(D, DOWN)

        triangle_ACD = Polygon(A, C, D, color=YELLOW, fill_opacity=0.4)
        triangle_ACB = Polygon(A, C, B, color=BLUE, fill_opacity=0.4)
        triangle_ABD = Polygon(A, B, D, color=RED, fill_opacity=0.4)

        elements = VGroup(
            triangle, altitude1, altitude2,
            triangle_ACD, triangle_ABD, triangle_ACB,
            label_A, label_B, label_C, label_D
        )

        elements.shift(LEFT * 3.5)

        self.play(Create(triangle), run_time=2)
        self.play(Write(label_A), Write(label_B), Write(label_C))
        self.wait(1)

        self.play(Create(altitude1), Create(altitude2), Write(label_D))
        self.wait(1)
        self.play(FadeIn(triangle_ACB))
        self.wait(1)
        self.play(FadeIn(triangle_ACD))
        self.wait(1)
        self.play(FadeIn(triangle_ABD))
        self.wait(1)

        formula1 = MathTex(
            r"\text{Area}_{ABC} = \text{Area}_{ABD} - \text{Area}_{ACD}"
        ).to_edge(UP).shift(RIGHT * 2)
        self.play(Write(formula1))
        self.wait(1)

        formula2 = MathTex(
            r"= \frac{1}{2} \cdot DB \cdot AD - \frac{1}{2} \cdot DC \cdot AD"
        ).next_to(formula1, DOWN * 1.5)
        self.play(Write(formula2))
        self.wait(1)

        formula3 = MathTex(
            r"= \frac{1}{2} \cdot AD \cdot (DB - DC)"
        ).next_to(formula2, DOWN * 1.5)
        self.play(Write(formula3))
        self.wait(1)

        formula4 = MathTex(
            r"= \frac{1}{2} \cdot AD \cdot CB"
        ).next_to(formula3, DOWN * 1.5)
        self.play(Write(formula4))
        self.wait(1)

        formula_final = MathTex(
            r"\text{Area}_{ABC} = \frac{1}{2} \cdot \text{base} \cdot \text{height}"
        ).next_to(formula4, DOWN * 1.5).set_color(YELLOW)
        self.play(Write(formula_final))
        self.wait(2)

        conclusion = Tex(
            "The formula is also valid when the height falls outside the triangle."
        ).next_to(formula_final, DOWN * 1.5).shift(LEFT * 1.5).set_color(GREEN)
        self.play(Write(conclusion))
        self.wait(3)


class TriangleAreaRectangle(Scene):
    def construct(self):
        square = Square(side_length=3, color=BLUE)
        square.set_fill(BLUE, opacity=0.5)
        square.move_to(np.array([-2, 0, 0]))

        base_label = MathTex("b").next_to(square, DOWN)
        height_label = MathTex("h").next_to(square, RIGHT)

        self.play(Create(square))
        self.play(Write(base_label), Write(height_label))
        self.wait(1)

        diagonal = Line(square.get_corner(DL), square.get_corner(UR), color=RED)
        self.play(Create(diagonal))
        self.wait(1)

        left_triangle = Polygon(
            square.get_corner(DL),
            square.get_corner(UL),
            square.get_corner(UR),
            color=GREEN,
            fill_opacity=0.5
        )

        right_triangle = Polygon(
            square.get_corner(DL),
            square.get_corner(DR),
            square.get_corner(UR),
            color=YELLOW,
            fill_opacity=0.5
        )

        self.play(
            FadeOut(square),
            FadeOut(diagonal),
            FadeIn(left_triangle),
            FadeIn(right_triangle),
        )
        self.wait(1)

        self.play(FadeOut(left_triangle))
        self.wait(1)

        formula = MathTex(r"A_{\text{square}} = b \cdot h").scale(1.5).move_to(np.array([3.5, 1, 0]))
        self.play(Write(formula))
        self.wait(2)

        area_square = MathTex(r"A_{\text{triangle}} = \frac{A_{\text{square}}}{2}").next_to(formula, DOWN)
        self.play(Write(area_square))
        self.wait(1)

        area_triangle = MathTex(r"A = \frac{b \cdot h}{2}").next_to(area_square, DOWN)
        self.play(Write(area_triangle))
        self.wait(2)

        conclusion = Tex("The area of the triangle is half the area of the square.").to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)
