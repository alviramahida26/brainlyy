import tkinter as tk
from tkinter import ttk


# ==================== QUIZ DATA ====================

QUESTIONS = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "options": [
            "Jawaharlal Nehru",
            "Mahatma Gandhi",
            "Sardar Patel",
            "Subhash Chandra Bose"
        ],
        "answer": "Mahatma Gandhi"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": [
            "Atlantic Ocean",
            "Indian Ocean",
            "Pacific Ocean",
            "Arctic Ocean"
        ],
        "answer": "Pacific Ocean"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "How many continents are there in the world?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Who is commonly credited with inventing the practical electric light bulb?",
        "options": [
            "Isaac Newton",
            "Thomas Edison",
            "Nikola Tesla",
            "Albert Einstein"
        ],
        "answer": "Thomas Edison"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Japan", "South Korea", "Thailand"],
        "answer": "Japan"
    },
    {
        "question": "What is the national animal of India?",
        "options": ["Lion", "Tiger", "Elephant", "Leopard"],
        "answer": "Tiger"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": [
            "Oxygen",
            "Nitrogen",
            "Carbon Dioxide",
            "Hydrogen"
        ],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "Which is the smallest continent?",
        "options": ["Europe", "Australia", "Antarctica", "Africa"],
        "answer": "Australia"
    }
]


# ==================== QUIZ APPLICATION ====================

class QuizApp:

    def __init__(self, root):

        self.root = root

        # ---------- MOBILE STYLE WINDOW ----------

        self.root.title("Brainlyy - Quiz Application")
        self.root.geometry("420x760")
        self.root.resizable(False, False)
        self.root.configure(bg="#F4F7FB")

        self.center_window()

        # ---------- VARIABLES ----------

        self.current_question = 0
        self.score = 0
        self.selected_answer = None
        self.time_left = 10
        self.timer_id = None
        self.option_buttons = []

        self.setup_styles()
        self.show_welcome_screen()

    # ==================== CENTER WINDOW ====================

    def center_window(self):

        self.root.update_idletasks()

        width = 420
        height = 760

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(
            f"{width}x{height}+{x}+{y}"
        )

    # ==================== STYLES ====================

    def setup_styles(self):

        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Quiz.Horizontal.TProgressbar",
            thickness=8
        )

    # ==================== CLEAR SCREEN ====================

    def clear_screen(self):

        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        for widget in self.root.winfo_children():
            widget.destroy()

    # ==================== WELCOME SCREEN ====================

    def show_welcome_screen(self):

        self.clear_screen()

        main_frame = tk.Frame(
            self.root,
            bg="#F4F7FB"
        )

        main_frame.pack(
            fill="both",
            expand=True
        )

        # Logo / App Name
        title = tk.Label(
            main_frame,
            text="Brainlyy",
            font=("Segoe UI", 34, "bold"),
            fg="#1E3A8A",
            bg="#F4F7FB"
        )

        title.pack(pady=(120, 8))

        # Subtitle
        subtitle = tk.Label(
            main_frame,
            text="Interactive Quiz Application",
            font=("Segoe UI", 14),
            fg="#475569",
            bg="#F4F7FB"
        )

        subtitle.pack()

        # Description
        description = tk.Label(
            main_frame,
            text="Test your knowledge\nand improve your skills.",
            font=("Segoe UI", 11),
            fg="#64748B",
            bg="#F4F7FB",
            justify="center"
        )

        description.pack(pady=18)

        # Quiz info card
        info_frame = tk.Frame(
            main_frame,
            bg="white",
            padx=25,
            pady=15
        )

        info_frame.pack(pady=10)

        info = tk.Label(
            info_frame,
            text="10 Questions  •  10 Seconds",
            font=("Segoe UI", 11, "bold"),
            fg="#334155",
            bg="white"
        )

        info.pack()

        # Start button
        start_button = tk.Button(
            main_frame,
            text="START QUIZ",
            font=("Segoe UI", 12, "bold"),
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=50,
            pady=14,
            command=self.start_quiz
        )

        start_button.pack(pady=25)

        # Footer
        footer = tk.Label(
            main_frame,
            text="Built with Python & Tkinter",
            font=("Segoe UI", 9),
            fg="#94A3B8",
            bg="#F4F7FB"
        )

        footer.pack(
            side="bottom",
            pady=20
        )

    # ==================== START QUIZ ====================

    def start_quiz(self):

        self.current_question = 0
        self.score = 0

        self.show_question()

    # ==================== SHOW QUESTION ====================

    def show_question(self):

        self.clear_screen()

        self.selected_answer = None
        self.time_left = 10

        question_data = QUESTIONS[
            self.current_question
        ]

        # ---------- HEADER ----------

        header = tk.Frame(
            self.root,
            bg="#1E3A8A"
        )

        header.pack(
            fill="x"
        )

        title = tk.Label(
            header,
            text="Brainlyy",
            font=("Segoe UI", 18, "bold"),
            fg="white",
            bg="#1E3A8A"
        )

        title.pack(
            pady=(15, 3)
        )

        counter = tk.Label(
            header,
            text=f"Question {self.current_question + 1} / {len(QUESTIONS)}",
            font=("Segoe UI", 10),
            fg="#DBEAFE",
            bg="#1E3A8A"
        )

        counter.pack(
            pady=(0, 15)
        )

        # ---------- CONTENT ----------

        content = tk.Frame(
            self.root,
            bg="#F4F7FB"
        )

        content.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=22
        )

        # ---------- PROGRESS ----------

        progress_value = (
            (self.current_question + 1)
            / len(QUESTIONS)
        ) * 100

        progress = ttk.Progressbar(
            content,
            style="Quiz.Horizontal.TProgressbar",
            maximum=100,
            value=progress_value
        )

        progress.pack(
            fill="x",
            pady=(0, 20)
        )

        # ---------- QUESTION ----------

        question_label = tk.Label(
            content,
            text=question_data["question"],
            font=("Segoe UI", 16, "bold"),
            fg="#0F172A",
            bg="#F4F7FB",
            wraplength=360,
            justify="left"
        )

        question_label.pack(
            anchor="w",
            pady=(5, 15)
        )

        # ---------- TIMER ----------

        self.timer_label = tk.Label(
            content,
            text="Time: 10s",
            font=("Segoe UI", 11, "bold"),
            fg="#DC2626",
            bg="#F4F7FB"
        )

        self.timer_label.pack(
            anchor="w",
            pady=(0, 10)
        )

        # ---------- OPTIONS ----------

        self.option_buttons = []

        for index, option in enumerate(
            question_data["options"]
        ):

            button = tk.Button(
                content,
                text=f"{chr(65 + index)}.  {option}",
                font=("Segoe UI", 11),
                bg="white",
                fg="#1E293B",
                activebackground="#DBEAFE",
                activeforeground="#1E3A8A",
                relief="solid",
                bd=1,
                anchor="w",
                padx=15,
                pady=12,
                cursor="hand2",
                wraplength=330,
                command=lambda selected=option:
                    self.select_answer(selected)
            )

            button.pack(
                fill="x",
                pady=5
            )

            self.option_buttons.append(button)

        # ---------- NEXT BUTTON ----------

        self.next_button = tk.Button(
            content,
            text="NEXT  →",
            font=("Segoe UI", 11, "bold"),
            bg="#CBD5E1",
            fg="#64748B",
            relief="flat",
            cursor="hand2",
            padx=25,
            pady=10,
            state="disabled",
            command=self.next_question
        )

        self.next_button.pack(
            pady=18
        )

        self.start_timer()

    # ==================== SELECT ANSWER ====================

    def select_answer(self, selected):

        if self.selected_answer is not None:
            return

        self.selected_answer = selected

        correct_answer = QUESTIONS[
            self.current_question
        ]["answer"]

        # Stop timer
        if self.timer_id:

            self.root.after_cancel(
                self.timer_id
            )

            self.timer_id = None

        # Disable options
        for button in self.option_buttons:
            button.config(
                state="disabled"
            )

        selected_index = QUESTIONS[
            self.current_question
        ]["options"].index(selected)

        correct_index = QUESTIONS[
            self.current_question
        ]["options"].index(correct_answer)

        # Correct answer highlight
        self.option_buttons[
            correct_index
        ].config(
            bg="#DCFCE7",
            fg="#166534"
        )

        # Wrong answer
        if selected != correct_answer:

            self.option_buttons[
                selected_index
            ].config(
                bg="#FEE2E2",
                fg="#991B1B"
            )

            self.timer_label.config(
                text="Wrong answer!",
                fg="#DC2626"
            )

        else:

            self.score += 1

            self.timer_label.config(
                text="Correct! ✓",
                fg="#16A34A"
            )

        self.next_button.config(
            state="normal",
            bg="#2563EB",
            fg="white"
        )

    # ==================== TIMER ====================

    def start_timer(self):

        if self.selected_answer is not None:
            return

        if self.time_left > 0:

            self.timer_label.config(
                text=f"Time: {self.time_left}s"
            )

            self.time_left -= 1

            self.timer_id = self.root.after(
                1000,
                self.start_timer
            )

        else:

            self.time_up()

    # ==================== TIME UP ====================

    def time_up(self):

        if self.selected_answer is not None:
            return

        self.selected_answer = "TIME_UP"

        correct_answer = QUESTIONS[
            self.current_question
        ]["answer"]

        for button in self.option_buttons:

            button.config(
                state="disabled"
            )

        correct_index = QUESTIONS[
            self.current_question
        ]["options"].index(correct_answer)

        self.option_buttons[
            correct_index
        ].config(
            bg="#DCFCE7",
            fg="#166534"
        )

        self.timer_label.config(
            text="Time's up!",
            fg="#DC2626"
        )

        self.next_button.config(
            state="normal",
            bg="#2563EB",
            fg="white"
        )

    # ==================== NEXT QUESTION ====================

    def next_question(self):

        self.current_question += 1

        if self.current_question < len(QUESTIONS):

            self.show_question()

        else:

            self.show_result()

    # ==================== RESULT SCREEN ====================

    def show_result(self):

        self.clear_screen()

        total = len(QUESTIONS)

        wrong = total - self.score

        percentage = (
            self.score / total
        ) * 100

        if percentage >= 80:

            grade = "A"
            message = "Excellent Performance!"

        elif percentage >= 50:

            grade = "B"
            message = "Good Performance!"

        else:

            grade = "C"
            message = "Keep Practicing!"

        result_frame = tk.Frame(
            self.root,
            bg="#F4F7FB"
        )

        result_frame.pack(
            fill="both",
            expand=True
        )

        # App name
        title = tk.Label(
            result_frame,
            text="Brainlyy",
            font=("Segoe UI", 24, "bold"),
            fg="#1E3A8A",
            bg="#F4F7FB"
        )

        title.pack(
            pady=(60, 5)
        )

        # Result title
        completed = tk.Label(
            result_frame,
            text="Quiz Completed!",
            font=("Segoe UI", 18, "bold"),
            fg="#334155",
            bg="#F4F7FB"
        )

        completed.pack(
            pady=5
        )

        # Message
        message_label = tk.Label(
            result_frame,
            text=message,
            font=("Segoe UI", 12),
            fg="#64748B",
            bg="#F4F7FB"
        )

        message_label.pack(
            pady=8
        )

        # Score
        score_label = tk.Label(
            result_frame,
            text=f"{percentage:.0f}%",
            font=("Segoe UI", 42, "bold"),
            fg="#2563EB",
            bg="#F4F7FB"
        )

        score_label.pack(
            pady=10
        )

        # Details
        details = tk.Label(
            result_frame,
            text=(
                f"Correct Answers : {self.score}\n"
                f"Wrong Answers   : {wrong}\n"
                f"Total Questions : {total}\n"
                f"Grade           : {grade}"
            ),
            font=("Segoe UI", 11),
            fg="#334155",
            bg="#F4F7FB",
            justify="left"
        )

        details.pack(
            pady=10
        )

        # Restart
        restart_button = tk.Button(
            result_frame,
            text="RESTART QUIZ",
            font=("Segoe UI", 11, "bold"),
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=35,
            pady=11,
            command=self.start_quiz
        )

        restart_button.pack(
            pady=10
        )

        # Exit
        exit_button = tk.Button(
            result_frame,
            text="EXIT",
            font=("Segoe UI", 10),
            bg="#E2E8F0",
            fg="#334155",
            relief="flat",
            cursor="hand2",
            padx=30,
            pady=9,
            command=self.root.destroy
        )

        exit_button.pack()


# ==================== RUN APP ====================

if __name__ == "__main__":

    root = tk.Tk()

    app = QuizApp(root)

    root.mainloop()