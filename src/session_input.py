class SessionInput:

    def collect_session(self):

        print("\n--- New Learning Session ---")

        subject = input("Subject: ")

        topic = input("Topic: ")

        duration = int(
            input("Study duration (minutes): ")
        )

        focus = int(
            input("Focus level (1-10): ")
        )

        understanding = int(
            input("Understanding level (1-10): ")
        )

        mistakes_input = input(
            "Mistakes (separate with commas): "
        )

        if mistakes_input.strip():

            mistakes = [
                item.strip()
                for item in mistakes_input.split(",")
            ]

        else:

            mistakes = []


        summary = input(
            "Did you write a summary? (yes/no): "
        )


        summary_written = (
            summary.lower() == "yes"
        )


        return {
            "subject": subject,
            "topic": topic,
            "duration": duration,
            "focus": focus,
            "understanding": understanding,
            "mistakes": mistakes,
            "summary_written": summary_written
        }



def collect_learning_session():

    session_input = SessionInput()

    return session_input.collect_session()