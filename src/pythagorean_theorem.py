from manim import *
import math


class PythagoreanTheorem(Scene):
    def construct(self):
        # ========== PARAMETERS INITIALIZATION ==========
        # Define initial triangle dimensions (can be modified to demonstrate different cases)
        a = 2.0  # Length of first leg
        b = 1.2  # Length of second leg
        side_length = a + b  # Side length of the large outer square
        hypotenuse = math.sqrt(a ** 2 + b ** 2)  # Calculate hypotenuse using Pythagorean theorem
        rotation_angle = math.atan2(b, a)  # Angle for rotating the central square to align with hypotenuse

        # ========== GEOMETRIC OBJECTS CREATION ==========
        # Create the large outer square that contains all other elements
        large_square = Square(side_length=side_length).set_stroke(width=3).set_fill(opacity=0)
        large_square.move_to(ORIGIN)  # Center the large square at origin for symmetry

        # Calculate vertices of the large square for precise triangle placement
        half_side = side_length / 2
        bottom_left = np.array([-half_side, -half_side, 0])
        bottom_right = np.array([half_side, -half_side, 0])
        top_right = np.array([half_side, half_side, 0])
        top_left = np.array([-half_side, half_side, 0])

        # Create four congruent right triangles, each positioned at a different corner
        # Each triangle has legs of lengths a and b, with right angles at the corners
        triangle_bl = Polygon(
            bottom_left,
            bottom_left + np.array([b, 0, 0]),  # Horizontal leg of length b
            bottom_left + np.array([0, a, 0]),  # Vertical leg of length a
            stroke_width=2,
            fill_opacity=0.5,
        ).set_fill(BLUE)  # Bottom-left triangle

        triangle_br = Polygon(
            bottom_right,
            bottom_right + np.array([-a, 0, 0]),  # Horizontal leg of length a (pointing left)
            bottom_right + np.array([0, b, 0]),  # Vertical leg of length b
            stroke_width=2,
            fill_opacity=0.5,
        ).set_fill(GREEN)  # Bottom-right triangle

        triangle_tr = Polygon(
            top_right,
            top_right + np.array([-b, 0, 0]),  # Horizontal leg of length b (pointing left)
            top_right + np.array([0, -a, 0]),  # Vertical leg of length a (pointing down)
            stroke_width=2,
            fill_opacity=0.5,
        ).set_fill(RED)  # Top-right triangle

        triangle_tl = Polygon(
            top_left,
            top_left + np.array([a, 0, 0]),  # Horizontal leg of length a
            top_left + np.array([0, -b, 0]),  # Vertical leg of length b (pointing down)
            stroke_width=2,
            fill_opacity=0.5,
        ).set_fill(YELLOW)  # Top-left triangle

        # Create the central square with side length equal to the hypotenuse
        # Rotated to align with the hypotenuses of the triangles
        small_square = Square(side_length=hypotenuse).rotate(rotation_angle).move_to(ORIGIN)
        small_square.set_stroke(width=3).set_fill(PINK, opacity=0.6)

        # ========== TEXT AND LABELS SETUP ==========
        # Create title for the visualization
        title = Tex("Area Proof: Pythagorean Theorem", font_size=36).to_edge(UP)

        # Create braces and labels to indicate side lengths of the bottom-left triangle
        brace_a = Brace(Line(bottom_left, bottom_left + np.array([0, a, 0])), LEFT, buff=0.15)
        brace_a_label = brace_a.get_tex("a")  # Label for vertical leg

        brace_b = Brace(Line(bottom_left, bottom_left + np.array([b, 0, 0])), DOWN, buff=0.15)
        brace_b_label = brace_b.get_tex("b")  # Label for horizontal leg

        # Create brace and label for the hypotenuse
        hypotenuse_line = Line(bottom_left + np.array([0, a, 0]), bottom_left + np.array([b, 0, 0]))
        brace_c = Brace(hypotenuse_line, direction=hypotenuse_line.copy().rotate(PI / 2).get_unit_vector(), buff=0.15)
        brace_c_label = brace_c.get_tex("c")  # Label for hypotenuse

        # Position the hypotenuse label for optimal visibility
        brace_c_label.move_to(brace_c.get_center() + UP * 0.3 + RIGHT * 0.375)

        # ========== ANIMATION SEQUENCE ==========
        # Display title and create visual hierarchy
        self.play(Create(title))
        self.wait(0.6)

        # Introduce the large square and its area formula
        self.play(Create(large_square))
        area_formula = MathTex(r"\text{Area} = (a+b)^2", font_size=36).next_to(large_square, UP, buff=0.1)
        self.play(Write(area_formula))
        self.wait(0.7)

        # Reveal the four triangles that partition the large square
        self.play(FadeIn(triangle_bl), FadeIn(triangle_br), FadeIn(triangle_tr), FadeIn(triangle_tl), run_time=1.2)

        # Show measurement labels for triangle sides
        self.play(FadeIn(brace_a, brace_a_label, brace_b, brace_b_label))
        self.wait(1)

        # Introduce the central square and its hypotenuse label
        self.play(Create(small_square))
        self.play(Create(brace_c), Write(brace_c_label))
        self.wait(0.8)

        # ========== ALGEBRAIC PROOF DEVELOPMENT ==========
        # Present the area equivalence equation: large square = 4 triangles + central square
        area_equation = MathTex(
            r"(a+b)^2 = 4\cdot\left(\tfrac{1}{2}ab\right) + c^2",
            font_size=36,
        ).to_edge(DOWN)
        self.play(Write(area_equation))
        self.wait(1.5)

        # Step 1: Simplify the equation by calculating 4 × (1/2 ab) = 2ab
        step1 = MathTex(r"(a+b)^2 = 2ab + c^2", font_size=36).to_edge(DOWN)
        self.play(Transform(area_equation, step1))
        self.wait(1.5)

        # Step 2: Expand the left side using binomial expansion
        step2 = MathTex(r"a^2 + 2ab + b^2 = 2ab + c^2", font_size=36).to_edge(DOWN)
        self.play(Transform(area_equation, step2))
        self.wait(1.5)

        # Step 3: Cancel 2ab from both sides to arrive at the Pythagorean theorem
        step3 = MathTex(r"a^2 + b^2 = c^2", font_size=48).to_edge(DOWN)
        self.play(Transform(area_equation, step3), run_time=1.2)
        self.wait(1.75)

        # Display the final conclusion statement
        final_conclusion = Tex(
            "Therefore, in any\\\\right triangle:\\\\"
            r"$c^2 = a^2 + b^2$",
            font_size=30,
        ).move_to(ORIGIN).shift(RIGHT * 4.5)
        self.play(FadeIn(final_conclusion))
        self.wait(1.4)

        # Highlight the area partition to emphasize the visual proof
        self.play(
            large_square.animate.set_stroke(WHITE, 3),
            triangle_bl.animate.set_fill(opacity=0.6),
            triangle_br.animate.set_fill(opacity=0.6),
            triangle_tr.animate.set_fill(opacity=0.6),
            triangle_tl.animate.set_fill(opacity=0.6),
            small_square.animate.set_fill(LIGHT_PINK, opacity=0.9),
            run_time=1.0,
        )
        self.wait(1.2)

        # ========== DYNAMIC DIMENSION CHANGE DEMONSTRATION ==========
        # Announce the upcoming transformation with different triangle dimensions
        dimension_change_text = Tex(
            "Now we change the dimensions of $a$ and $b$",
            font_size=30
        ).to_edge(UP, buff=1)
        self.play(Write(dimension_change_text))
        self.wait(1)

        # Define new triangle dimensions to demonstrate the theorem's generality
        a_new = 1.5
        b_new = 2.5

        # Recalculate geometric properties with new dimensions
        side_length_new = a_new + b_new
        hypotenuse_new = math.sqrt(a_new ** 2 + b_new ** 2)
        rotation_angle_new = math.atan2(b_new, a_new)

        # Update vertex positions for the new large square
        half_side_new = side_length_new / 2
        bottom_left_new = np.array([-half_side_new, -half_side_new, 0])
        bottom_right_new = np.array([half_side_new, -half_side_new, 0])
        top_right_new = np.array([half_side_new, half_side_new, 0])
        top_left_new = np.array([-half_side_new, half_side_new, 0])

        # Update triangle vertices to match new dimensions while maintaining congruence
        triangle_bl.generate_target()
        triangle_bl.target.set_points_as_corners([
            bottom_left_new,
            bottom_left_new + np.array([b_new, 0, 0]),
            bottom_left_new + np.array([0, a_new, 0])
        ])

        triangle_br.generate_target()
        triangle_br.target.set_points_as_corners([
            bottom_right_new,
            bottom_right_new + np.array([-a_new, 0, 0]),
            bottom_right_new + np.array([0, b_new, 0])
        ])

        triangle_tr.generate_target()
        triangle_tr.target.set_points_as_corners([
            top_right_new,
            top_right_new + np.array([-b_new, 0, 0]),
            top_right_new + np.array([0, -a_new, 0])
        ])

        triangle_tl.generate_target()
        triangle_tl.target.set_points_as_corners([
            top_left_new,
            top_left_new + np.array([a_new, 0, 0]),
            top_left_new + np.array([0, -b_new, 0])
        ])

        # Remove old measurement braces to prepare for new ones
        self.play(
            FadeOut(brace_a), FadeOut(brace_a_label),
            FadeOut(brace_b), FadeOut(brace_b_label),
            FadeOut(brace_c), FadeOut(brace_c_label)
        )
        self.wait(0.3)

        # Create new measurement braces for the updated triangle
        brace_a_new = Brace(
            Line(bottom_left_new, bottom_left_new + np.array([0, a_new, 0])),
            LEFT, buff=0.15
        )
        brace_a_label_new = brace_a_new.get_tex("a")

        brace_b_new = Brace(
            Line(bottom_left_new, bottom_left_new + np.array([b_new, 0, 0])),
            DOWN, buff=0.15
        )
        brace_b_label_new = brace_b_new.get_tex("b")

        hypotenuse_line_new = Line(
            bottom_left_new + np.array([0, a_new, 0]),
            bottom_left_new + np.array([b_new, 0, 0])
        )
        brace_c_new = Brace(
            hypotenuse_line_new,
            direction=hypotenuse_line_new.copy().rotate(PI / 2).get_unit_vector(),
            buff=0.15
        )
        brace_c_label_new = brace_c_new.get_tex("c")
        brace_c_label_new.move_to(brace_c_new.get_center() + UP * 0.45 + RIGHT * 0.25)

        # Update the central square to match new hypotenuse and rotation
        small_square.generate_target()
        small_square.target.become(
            Square(side_length=hypotenuse_new)
            .rotate(rotation_angle_new)
            .move_to(ORIGIN)
            .set_fill(PINK, opacity=0.6)
        )

        # Update the large square to new dimensions
        large_square.generate_target()
        large_square.target.become(
            Square(side_length=side_length_new)
            .set_stroke(width=3)
            .move_to(ORIGIN)
        )

        # Adjust formula position to maintain visual balance
        self.play(area_formula.animate.shift(UP * 0.35))

        # Animate the transformation to new dimensions
        self.play(
            MoveToTarget(triangle_bl),
            MoveToTarget(triangle_br),
            MoveToTarget(triangle_tr),
            MoveToTarget(triangle_tl),
            MoveToTarget(small_square),
            MoveToTarget(large_square),
            run_time=3
        )

        # Display the key insight: the Pythagorean relationship remains valid
        invariant_text = Tex(
            "Even though the sides change, \\\\ the relationship $a^2 + b^2 = c^2$ \\\\ remains true!",
            font_size=30
        ).shift(LEFT * 4.5)

        # Show new measurement labels
        self.play(
            FadeIn(brace_a_new),
            FadeIn(brace_a_label_new),
            FadeIn(brace_b_new),
            FadeIn(brace_b_label_new),
            FadeIn(brace_c_new),
            FadeIn(brace_c_label_new),
            run_time=1.5
        )

        # Conclude with the invariant relationship message
        self.play(Write(invariant_text))
        self.wait(2.5)
