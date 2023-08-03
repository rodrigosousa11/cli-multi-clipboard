import sys
import clipboard
import json
import os

CLIPBOARD = "clipboard.json"

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent='\t')

def load_data(file):
    try:
        with open(file, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

def delete_all_data(file):
    with open(file, "w") as f:
        f.write("")
    print("All data deleted!")

if len(sys.argv) == 1:
    command = input("Enter a command (save/load/list/delete): ")
else:
    command = sys.argv[1]

data = load_data(CLIPBOARD)

if command == "save":
    key = input("Insert a name to remember the copied data: ")
    data[key] = clipboard.paste()
    save_data(CLIPBOARD, data)
    print("Data saved!")
elif command == "load":
    key = input("Insert the name of the saved data: ")
    if key in data:
        clipboard.copy(data[key])
        print("Data copied to clipboard.")
    else:
        print("Name not found!")
elif command == "list":
    print("Saved data:")
    for key, value in data.items():
        print(f"{key} -> {value}")
elif command == "delete":
    if os.path.exists(CLIPBOARD):
        confirm = input("Are you sure you want to delete all copied data? (y/n): ")
        if confirm.lower() == "y":
            delete_all_data(CLIPBOARD)
        else:
            print("Deletion canceled.")
    else:
        print("No data saved!")
else:
    print("Unknown command!")