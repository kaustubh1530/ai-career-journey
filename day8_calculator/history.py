history_file = "calc_history.txt"


def save_history(text):
    with open(history_file, "a") as file:
        file.write(text + "\n")


def view_history():
    try:
        with open(history_file, "r") as file:
            print("\n--- Calculation History ---")
            print(file.read())
    except FileNotFoundError:
        print("No history found yet.")