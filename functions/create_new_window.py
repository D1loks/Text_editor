from customtkinter import CTk, set_default_color_theme, set_appearance_mode, CTkFrame, CTkButton, CTkTextbox

from functions import save_file, open_file, copy, paste, clear, about_creator


def create_new_window():
    new_root = CTk()
    new_root.title("Text editor")
    new_root.geometry("500x400")
    set_default_color_theme("dark-blue")
    set_appearance_mode("dark")

    frame = CTkFrame(new_root, fg_color="#1a1a1a")
    frame.pack(padx=20, pady=20, anchor="nw")

    save_btn = CTkButton(frame, text="Save file", text_color="#2a99f5", font=("helvetica", 14), border_width=1,
                         border_color="#2a99f5", fg_color="#192841", command=lambda: save_file(tx))
    save_btn.pack(side="left", padx=10)

    open_btn = CTkButton(frame, text="Open file", text_color="#2a99f5", font=("helvetica", 14), border_width=1,
                         border_color="#2a99f5", fg_color="#192841", command=lambda: open_file(tx))
    open_btn.pack(side="left", padx=10)

    tx = CTkTextbox(new_root, text_color="#2a99f5", font=("helvetica", 14), border_width=1,
                    border_color="#2a99f5", fg_color="#192841", width=400, height=150)
    tx.pack(padx=50, anchor="nw", pady=20)

    button_frame = CTkFrame(new_root, fg_color="#1a1a1a")
    button_frame.pack(padx=20, pady=(20, 20), anchor="nw")

    copy_btn = CTkButton(button_frame, text="Copy", text_color="#2a99f5", font=("helvetica", 14), border_width=1,
                         border_color="#2a99f5", fg_color="#192841", command=lambda: copy(tx))
    copy_btn.pack(side="left", padx=10)

    paste_btn = CTkButton(button_frame, text="Paste", text_color="#2a99f5", font=("helvetica", 14), border_width=1,
                          border_color="#2a99f5", fg_color="#192841", command=lambda: paste(tx))
    paste_btn.pack(side="left", padx=10)

    clear_btn = CTkButton(button_frame, text="Clear", text_color="#2a99f5", font=("helvetica", 14), border_width=1,
                          border_color="#2a99f5", fg_color="#192841", command=lambda: clear(tx))
    clear_btn.pack(side="left", padx=10)

    about_btn = CTkButton(frame, text="About Creator", text_color="#2a99f5", font=("helvetica", 14),
                          border_width=1,
                          border_color="#2a99f5", fg_color="#192841", command=about_creator)
    about_btn.pack(side="left", padx=10)

    new_root.mainloop()
