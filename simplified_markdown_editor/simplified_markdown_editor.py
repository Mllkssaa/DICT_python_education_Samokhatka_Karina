def plain(text):
    return text


def bold(text):
    return f"**{text}**"


def italic(text):
    return f"*{text}*"


def inline_code(text):
    return f"`{text}`"


def header(text, level):
    level = max(1, min(level, 6))
    return f"{'#' * level} {text}"


def link(label, url):
    return f"[{label}]({url})"


def new_line():
    return "\n"


def list_formatter(formatter):
    while True:
        try:
            rows = int(input("Number of rows: \n> "))
            if rows <= 0:
                print("The number of rows must be greater than zero.")
                continue

            items = [input(f"Row #{i + 1}: > ") for i in range(rows)]
            if formatter == "unordered-list":
                return "\n".join(f"- {item}" for item in items) + "\n"
            elif formatter == "ordered-list":
                return "\n".join(f"{i + 1}. {item}" for i, item in enumerate(items)) + "\n"
        except ValueError:
            print("Invalid input. Please enter a number.")


def save_to_file(content):
    with open("output.md", "a", encoding="utf-8") as file:
        file.write(content + "\n")


def main():
    print("Hello! Do you want to try formatting the text? (yes(y) or no(n))")
    answer = input("\n> ").strip().lower()

    if answer not in ("yes", "y"):
        print("Goodbye!")
        return

    print("Great! Let's start formatting. Choose a formatting option.\n")
    options = ["plain", "bold", "italic", "inline-code", "link", "header", "unordered-list", "ordered-list", "new-line"]
    for option in options:
        print(f"* {option}")

    choice = input("Enter your choice: >\n").strip().lower()
    result = ""

    if choice == "plain":
        text = input("Enter text: > \n")
        result = plain(text)

    elif choice == "bold":
        text = input("Enter text: > \n")
        result = bold(text)

    elif choice == "italic":
        text = input("Enter text: > \n")
        result = italic(text)

    elif choice == "inline-code":
        text = input("Enter text: > \n")
        result = inline_code(text)

    elif choice == "header":
        text = input("Enter text: > \n")
        try:
            level = int(input("Enter header level (1-6): > \n"))
            result = header(text, level)
        except ValueError:
            print("Invalid level. Must be a number between 1 and 6.")

    elif choice == "link":
        label = input("Enter link text: > \n")
        url = input("Enter URL: > \n")
        result = link(label, url)

    elif choice == "unordered-list":
        result = list_formatter("unordered-list")

    elif choice == "ordered-list":
        result = list_formatter("ordered-list")

    elif choice == "new-line":
        result = new_line()

    else:
        print("Invalid choice.")

    if result:
        print(result)
        save_to_file(result)


if __name__ == "__main__":
    main()