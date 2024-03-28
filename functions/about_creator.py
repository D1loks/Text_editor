from customtkinter import set_default_color_theme, set_appearance_mode, CTkLabel, CTk


def about_creator():
    creator_info = """
    Creator: Danylo Chubatiuk

    Email: danylochubatiuk@gmail.com

    Place of study: Ivan Bosko College

    Group: IT-12
    """
    creator_window = CTk()
    creator_window.title("About Creator")
    set_default_color_theme("dark-blue")
    set_appearance_mode("dark")
    creator_label = CTkLabel(creator_window, text=creator_info, font=("helvetica", 14), text_color="#2a99f5")
    creator_label.pack(padx=20, pady=20)
    creator_window.mainloop()
