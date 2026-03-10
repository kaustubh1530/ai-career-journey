import json

history_file = "calc_history.json"

def save_history(operation, num1, num2, result):

    new_entry = {
        "operation": operation,
        "num1": num1,
        "num2": num2,
        "result": result
    }

    try:
        with open(history_file, "r") as file:
            data = json.load(file)
    except:
        data = []

    data.append(new_entry)

    with open(history_file, "w") as file:
        json.dump(data, file, indent=4)


def view_history():

    try:
        with open(history_file, "r") as file:
            data = json.load(file)

        print("\n--- Calculation History ---")

        for entry in data:
            print(f"{entry['num1']} {entry['operation']} {entry['num2']} = {entry['result']}")

    except:
        print("No history found yet.")