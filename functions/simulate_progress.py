from time import sleep
from functions import create_new_window


def simulate_progress(progress_bar, label, root):
    progress_bar.set(0)
    progress_bar.update()
    for i in range(101):
        progress_bar.start()
        label.configure(text=f"Progress {i}%")
        sleep(0.01)
        progress_bar.update()
        label.update()
    root.destroy()
    create_new_window()
