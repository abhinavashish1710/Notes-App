import json
import os

FILE = "notes.json"

def load_notes():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_notes(notes):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=4)

def add_note():
    title = input("Title: ")
    content = input("Content: ")
    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)
    print("Note added!")

def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    for i, note in enumerate(notes, 1):
        print(f"\n{i}. {note['title']}")
        print(note["content"])

def delete_note():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    view_notes()
    try:
        idx = int(input("\nDelete note number: ")) - 1
        notes.pop(idx)
        save_notes(notes)
        print("Deleted.")
    except:
        print("Invalid choice.")

while True:
    print("\n===== Notes App =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        break
    else:
        print("Invalid option.")
