def hint(a, b):
    hint_message = ""
    if a > b:
        hint_message = "hint: Seems like you should shoot higher!"
    elif a < b:
        hint_message = "hint: You overreached!"
    return hint_message
