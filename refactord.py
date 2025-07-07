import os

favthings = {}

def main():

    if os.path.exists("favthings.txt"):
        with open("favthings.txt", "r") as file:
            for line in file:
                line = line.strip()
                if ":" in line:
                    key, value = line.split(":", 1)
                    favthings[key.strip()] = value.strip()
    else:
        print("No saved favorite things list found. Starting fresh.")

    def lookcats(favs):
        cat = input("\nWhich category do you want to access?(Type none for no category) ").lower()
        if cat in favs:
            print(f"My favorite {cat} is {favs[cat]}!")
        elif cat == "none":
            print("Alright then!")
        else:
            print("Invalid category!")
    def showcats(favs):
        if favs == {}:
            print("Nothing in your list.")
        else:
            print("\nThe categories you have are:")
            for key in favs.keys():
                print(f"- {key}")
    def add_favorite(favs):
        if input("Add a new category? (y/n): ").lower() == "y":
            new_category = input("New category name: ").strip().lower()
            new_value = input(f"Your favorite {new_category}: ").strip()
            favs[new_category] = new_value
    def changecats(favs):
        def change_favorite(favorites_dict):
            if input("Make a change to a category? (y/n): ").lower() == "y":
                changecat = input("Which category to change? ").strip().lower()
                if changecat in favs:
                    newval = input(f"New favorite for {changecat}: ").strip()
                favs[changecat] = newval
            else:
                print("That category doesn't exist.")
    def delcats(favs):
        if input("Delete a category? (y/n): ").lower() == "y":
            delcat = input("Which category to delete? ").strip().lower()
            if delcat in favs:
                del favs[delcat]
                print(f"{delcat} deleted.")
            else:
                print("That category doesn't exist.")

    while True:

        showcats(favthings)
        lookcats(favthings)
        addcats(favthings)
        changecats(favthings)
        delcats(favthings)

        if input("Do you want to continue? (y/n): ").lower() != "y":
            break

    with open("favthings.txt", "w") as file:
        for key, value in favthings.items():
            file.write(f"{key}: {value}\n")

    print("\nThanks for using! Your data has been saved.")

if __name__ == "__main__":
    main()