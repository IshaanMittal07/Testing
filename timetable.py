from tabulate import tabulate

def create_timetable():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    periods_per_day = int(input("Enter number of periods per day: "))
    
    timetable = []

    for day in days:
        print(f"\nEnter subjects for {day}:")
        periods = []
        for i in range(periods_per_day):
            subject = input(f"  Period {i+1}: ")
            periods.append(subject)
        timetable.append(periods)

    # Display the timetable
    headers = ["Day"] + [f"P{i+1}" for i in range(periods_per_day)]
    table = [[days[i]] + timetable[i] for i in range(len(days))]

    print("\nGenerated Timetable:")
    print(tabulate(table, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    create_timetable()
