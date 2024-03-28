def paste(textbox):
    text = textbox.clipboard_get()
    textbox.insert("insert", text)
