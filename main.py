from customtkinter import CTk, CTkLabel, CTkProgressBar, set_default_color_theme, set_appearance_mode, CTkButton

from functions import simulate_progress


def main():
    root = CTk()
    root.title("Progress Bar")
    root.geometry("300x200")
    set_default_color_theme("dark-blue")
    set_appearance_mode("dark")

    label = CTkLabel(root, text="Progress 0%", text_color="#2a99f5", font=("helvetica", 14))
    label.pack(pady=(50, 20))

    progress_bar = CTkProgressBar(root, progress_color="#2a99f5", orientation="horizontal", mode="determinate")
    progress_bar.pack()

    btn = CTkButton(root, text="Start", text_color="#2a99f5", font=("helvetica", 14), border_width=1,
                    border_color="#2a99f5", fg_color="#192841",
                    command=lambda: simulate_progress(progress_bar, label, root))
    btn.pack(pady=(20, 20))

    root.mainloop()


if __name__ == "__main__":
    main()
