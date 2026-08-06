class DailyState:

    def collect_state(self):

        print("\n--- Daily Learning Condition ---")


        condition = input(
            "How do you feel today? (normal/tired/sick): "
        )


        energy = int(
            input(
                "Energy level (1-10): "
            )
        )


        focus = int(
            input(
                "Expected focus level (1-10): "
            )
        )


        stress = int(
            input(
                "Stress level (1-10): "
            )
        )


        learning_mode = input(
            "Do you want a light, normal, or deep session? "
        )


        return {

            "condition": condition,

            "energy": energy,

            "focus": focus,

            "stress": stress,

            "learning_mode": learning_mode

        }