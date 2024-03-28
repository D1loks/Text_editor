def copy(textbox):
    selected_text = textbox.selection_get()
    textbox.clipboard_clear()
    textbox.clipboard_append(selected_text)
