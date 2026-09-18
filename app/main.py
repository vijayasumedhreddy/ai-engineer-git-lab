def greet(name, language="English"):
    if language == "English":
        return f"Hello, {name}!"
    elif language == "Spanish":
        return f"Hola, {name}!"
    elif language == "French":
        return f"Bonjour, {name}!"
    elif language == "German":
        return f"Hallo, {name}!"
    else:
        return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("AI Engineer"))