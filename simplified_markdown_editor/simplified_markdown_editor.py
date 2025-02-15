from sys import prefix


def print_reference():
    print("Available formatters: \n plain \n bold italic \n header \n link \n inline-coge \n ordered=list ")
    print("Special commands: \n !help \n !done ")

def ask_format(text, formatter):
    if formatter == "plain":
        return text
    elif formatter == "bold italic":
        return f"***{text}***"
    elif formatter == "inline-code":
        return f"'{text}'"
    elif formatter == "header":
        level = int(input("Level: > "))
        if 1 <= level <=6:
            text = input("Text: > ")
            return f"{'#' * level} {text} \n"
        else:
            print("The level should be within the range of 1 to 6. ")
            return f""
    elif formatter == "link":
        label = input("Label: > ")
        url = input("URL: > ")
        return f"[{label}]({url})"
    elif formatter == "new-line":
        return "\n"
    elif formatter in ["ordered-list", "unordered-list"]:
        num_rows = int(input("Number of rows: > "))
        if num_rows > 0:
            result = []
            for i in range(1, num_rows + 1):
                row_text = input(f"Row #{i}: > ")
                prefix = f"{i}. " if formatter == "order-list" else "* "
                result.append(f"{prefix}{row_text}")
            return  "\n".join(result) + "\n"
        else:
            print("The number of rows should be greater than zero ")
            return ""
    elif:
        return ""
