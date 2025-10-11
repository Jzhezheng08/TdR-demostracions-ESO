from manim import *


class QuadraticGeometry(Scene):
    def construct(self):
        # ====== Problem parameters ======
        # General equation: a x^2 + b x + c = 0
        a = 1.0
        b = 4.0
        c = 3.0

        # Normalized: x^2 + p x + q = 0
        p = b / a
        q = c / a

        # ====== Visualization parameters (graphic scale) ======
        unit = 0.6  # base size for graphic units
        x_visual = 1.0  # size of the square representing x
        base_side = x_visual * unit

        # ====== Base figure construction ======
        # Blue square representing x^2
        base_square = Square(side_length=base_side, stroke_width=3)
        base_square.set_fill(BLUE, opacity=0.25)
        base_square.to_edge(LEFT, buff=1)
        tex_x2 = MathTex("x^2").move_to(base_square.get_center())

        # Green rectangle representing p·x
        right_rect = Rectangle(width=p * unit, height=base_side, stroke_width=2)
        right_rect.set_fill(GREEN, opacity=0.25)
        right_rect.next_to(base_square, RIGHT, buff=0)
        tex_px = MathTex("p x").move_to(right_rect)

        # Show x^2 and p x
        self.play(Create(base_square), Write(tex_x2))
        self.wait(0.6)
        self.play(Create(right_rect), Write(tex_px))
        self.wait(0.8)

        # ====== Division of p·x rectangle into two equal parts ======
        rect1 = Rectangle(width=(p / 2) * unit, height=base_side, stroke_width=2)
        rect1.set_fill(GREEN, opacity=0.35)
        rect1.next_to(base_square, RIGHT, buff=0)
        textrect1 = MathTex(r"\frac{p x}{2}").scale(0.5).move_to(rect1)

        rect2 = Rectangle(width=(p / 2) * unit, height=base_side, stroke_width=2)
        rect2.set_fill(GREEN, opacity=0.35)
        rect2.next_to(rect1, RIGHT, buff=0)
        textrect2 = MathTex(r"\frac{p x}{2}").scale(0.5).move_to(rect2)

        self.play(FadeOut(tex_px), Transform(right_rect, VGroup(rect1.copy(), rect2.copy())))
        self.play(FadeIn(rect1), FadeIn(textrect1), FadeIn(rect2), FadeIn(textrect2))
        self.wait(0.6)
        self.play(FadeOut(textrect2))

        # ====== Reposition one rectangle on top to complete the square ======
        top_rect = Rectangle(width=base_side, height=(p / 2) * unit, stroke_width=2)
        top_rect.set_fill(GREEN, opacity=0.35)
        top_rect.next_to(base_square, UP, buff=0)

        self.play(ReplacementTransform(rect2, top_rect), FadeOut(right_rect))
        textrect2.move_to(top_rect)
        self.play(FadeIn(textrect2))
        self.wait(0.6)

        # ====== Yellow small square appears (p/2)^2 ======
        small_corner = Square(side_length=(p / 2) * unit, stroke_width=2)
        small_corner.set_fill(YELLOW, opacity=0.5)
        small_corner.align_to(rect1, RIGHT)
        small_corner.next_to(rect1, UP, buff=0)
        textsc = MathTex(r"\left(\frac{p}{2}\right)^2").move_to(small_corner)
        self.play(FadeIn(small_corner))
        self.play(FadeIn(textsc))
        self.wait(0.6)

        # Indicate that all pieces form a perfect square
        self.play(Indicate(VGroup(base_square, rect1, top_rect, small_corner)), run_time=1.2)
        self.wait(0.6)

        # ====== Show algebraic equivalences ======
        # Step 1: complete the square
        eq1 = MathTex(
            r"x^2 + p x + \left(\frac{p}{2}\right)^2 = \left(x + \frac{p}{2}\right)^2"
        ).shift(UP * 2.75)
        self.play(Write(eq1))
        self.wait(1.0)

        # Step 2: normalized equation
        eq2 = MathTex(
            r"x^2 + p x + q = 0 \quad (\text{Normalized Form})"
        ).next_to(eq1, DOWN, aligned_edge=LEFT)

        eq25 = MathTex(
            r"x^2 + p x = - q"
        ).next_to(eq2, DOWN, aligned_edge=LEFT)

        # Step 3: isolate the square
        eq3 = MathTex(
            r"\Rightarrow\quad (x + \tfrac{p}{2})^2 = \tfrac{p^2}{4} - q"
        ).next_to(eq25, DOWN, aligned_edge=LEFT)

        self.play(Write(eq2), Write(eq25), Write(eq3))
        self.wait(1.0)

        # Step 4: solve for x
        eq4 = MathTex(
            r"x + \tfrac{p}{2} = \pm\sqrt{\tfrac{p^2}{4} - q}"
        ).next_to(eq3, DOWN, aligned_edge=LEFT)
        eq5 = MathTex(
            r"x = -\tfrac{p}{2} \pm \sqrt{\tfrac{p^2}{4} - q}"
        ).next_to(eq4, DOWN, aligned_edge=LEFT)
        self.play(Write(eq4), Write(eq5))
        self.wait(1.2)
        self.play(FadeOut(VGroup(eq1, eq2, eq25, eq3, eq4, eq5)))

        final = MathTex(
            r"p = \tfrac{b}{a},\ \ q=\tfrac{c}{a}"
        ).shift(UP * 2)
        formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4 a c}}{2 a}"
        ).next_to(final, DOWN, aligned_edge=LEFT)
        self.play(Write(final), Write(formula))
        self.wait(1.4)
        self.play(Flash(formula, line_length=1.0))
