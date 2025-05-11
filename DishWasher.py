import time

class Dish:
    def __init__(self, name):
        self.name = name
        self.is_clean = False

    def wash(self):
        print(f"Washing {self.name}...")
        time.sleep(1)
        self.is_clean = True
        print(f"{self.name} is now clean!\n")

def display_dishes(dishes):
    print("Dishes:")
    for i, dish in enumerate(dishes):
        status = "Clean" if dish.is_clean else "Dirty"
        print(f"{i + 1}. {dish.name} - {status}")
    print()

def wash_dishes(dishes):
    for dish in dishes:
        if not dish.is_clean:
            dish.wash()

def main():
    dishes = [
        Dish("Plate"),
        Dish("Cup"),
        Dish("Fork"),
        Dish("Spoon"),
        Dish("Pan")
    ]

    while True:
        display_dishes(dishes)
        action = input("Type 'wash' to clean all dishes, 'exit' to quit: ").strip().lower()

        if action == "wash":
            wash_dishes(dishes)
        elif action == "exit":
            print("Exiting the dishwashing simulator. Bye!")
            break
        else:
            print("Invalid command.\n")

if __name__ == "__main__":
    main()
