import os

# Start with a default dictionary
favthings = {}

# Try to load saved data from file
if os.path.exists("favthings.txt"):
    with open("favthings.txt", "r") as file:
        for line in file:
            line = line.strip()
            if ":" in line:
                key, value = line.split(":", 1)
                favthings[key.strip()] = value.strip()
else:
    print("No saved favorite things list found. Starting fresh.")

# Main loop
while True:
    if favthings == {}:
        print("Nothing in your list.")
    else:
        print("\nThe categories you have are:")
        for key in favthings.keys():
            print(f"- {key}")
    
    cat = input("\nWhich category do you want to access? ").lower()
    if cat in favthings:
        print(f"My favorite {cat} is {favthings[cat]}!")
    else:
        print("Invalid category!")

    if input("Add a new category? (y/n): ").lower() == "y":
        newcat = input("New category name: ").strip().lower()
        newval = input(f"Your favorite {newcat}: ").strip()
        favthings[newcat] = newval

    if input("Make a change to a category? (y/n): ").lower() == "y":
        changecat = input("Which category to change? ").strip().lower()
        if changecat in favthings:
            newval = input(f"New favorite for {changecat}: ").strip()
            favthings[changecat] = newval
        else:
            print("That category doesn't exist.")

    if input("Delete a category? (y/n): ").lower() == "y":
        delcat = input("Which category to delete? ").strip().lower()
        if delcat in favthings:
            del favthings[delcat]
            print(f"{delcat} deleted.")
        else:
            print("That category doesn't exist.")

    if input("Do you want to continue? (y/n): ").lower() != "y":
        break

# Save updated dictionary to file
with open("favthings.txt", "w") as file:
    for key, value in favthings.items():
        file.write(f"{key}: {value}\n")

print("\nThanks for using! Your data has been saved.")
