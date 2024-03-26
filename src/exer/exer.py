from manim import *

class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT*4)
        line_moving = Line(LEFT, RIGHT*4)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        
        angle_text = Integer(theta_tracker.get_value()).move_to(
            Angle(
                line1, line_moving, radius=0.5 + 6 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        self.add(line1, line_moving, a, angle_text)
        self.wait()

        line_moving.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )

        def text_update(m: Integer):
            m.set_value(theta_tracker.get_value())
            m.move_to(
                Angle(line1, line_moving, radius=0.5 + 6 * SMALL_BUFF, other_angle=False).point_from_proportion(0.5)
            )
        angle_text.add_updater(
            text_update
        )

        self.play(theta_tracker.animate.set_value(30), run_time=1.5)
        self.play(theta_tracker.animate.increment_value(140), run_time=2)
        self.play(theta_tracker.animate.set_value(360), run_time=1.5)
        self.wait(2)