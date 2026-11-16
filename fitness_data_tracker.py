"""
Fitness Data Tracker
PS No.: 73
Language: Python 3

Features:
- Record daily steps and calories burned
- Check the 10,000-step daily goal
- Show average steps, total calories, best day, and goal days
- Calculate BMI and display its category
- Plot a bar chart of daily steps with the 10,000-step goal line
"""

import matplotlib.pyplot as plt

DAILY_GOAL = 10000

# The records are stored in two parallel Python lists.
steps_records = []
calories_records = []


def get_non_negative_integer(prompt, field_name):
    """Read a non-negative whole number; return None if input is invalid."""
    value = input(prompt).strip()
    try:
        number = int(value)
        if number < 0:
            raise ValueError
        return number
    except ValueError:
        print(f"Invalid {field_name}. Enter a non-negative whole number.")
        print("Record not saved.")
        return None


def add_record():
    """Add one day's steps and calories only when both inputs are valid."""
    steps = get_non_negative_integer("Enter steps: ", "steps")
    if steps is None:
        return

    calories = get_non_negative_integer("Enter calories burned: ", "calories")
    if calories is None:
        return

    steps_records.append(steps)
    calories_records.append(calories)

    day = len(steps_records)
    achieved = "Yes" if steps >= DAILY_GOAL else "No"
    percentage = (steps / DAILY_GOAL) * 100
    print(
        f"Record saved for Day {day}. Goal achieved: {achieved} "
        f"({percentage:.2f}% of goal)"
    )


def calculate_average_steps():
    """Return the average number of steps, or 0 when there are no records."""
    if not steps_records:
        return 0
    return sum(steps_records) / len(steps_records)


def calculate_total_calories():
    """Return the total calories recorded."""
    return sum(calories_records)


def find_best_day():
    """Return (day_number, steps) for the day with the most steps."""
    if not steps_records:
        return None
    best_index = steps_records.index(max(steps_records))
    return best_index + 1, steps_records[best_index]


def count_goal_days():
    """Count days on which the daily step goal was reached."""
    return sum(1 for steps in steps_records if steps >= DAILY_GOAL)


def show_summary():
    """Display the weekly/current-record summary in the required format."""
    if not steps_records:
        print("No records available. Add a record first.")
        return

    average = calculate_average_steps()
    total_calories = calculate_total_calories()
    best_day, best_steps = find_best_day()
    goal_days = count_goal_days()

    print(
        f"Average steps: {average:.2f} | Total calories: {total_calories}"
    )
    print(
        f"Best day: Day {best_day} ({best_steps} steps) | "
        f"Goal days: {goal_days}/{len(steps_records)}"
    )


def calculate_bmi():
    """Read valid weight and height, then calculate BMI and category."""
    while True:
        try:
            weight = float(input("Enter weight in kg: "))
            if weight <= 0:
                print("Invalid weight. Enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid weight. Enter a positive number.")

    while True:
        try:
            height = float(input("Enter height in metres: "))
            if height <= 0:
                print("Invalid height. Enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid height. Enter a positive number.")

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"BMI: {bmi:.2f} | Category: {category}")


def show_chart():
    """Display a bar chart of daily steps and the daily goal line."""
    if not steps_records:
        print("No records available. Add a record first.")
        return

    days = [f"Day {i}" for i in range(1, len(steps_records) + 1)]

    plt.figure(figsize=(9, 5))
    plt.bar(days, steps_records, label="Daily Steps")
    plt.axhline(
        y=DAILY_GOAL,
        linestyle="--",
        linewidth=2,
        label="10,000-step goal"
    )
    plt.title("Daily Steps")
    plt.xlabel("Day")
    plt.ylabel("Number of Steps")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main():
    """Run the menu-driven Fitness Data Tracker."""
    while True:
        print("\n===== FITNESS DATA TRACKER =====")
        print("1. Add record")
        print("2. Show summary")
        print("3. Calculate BMI")
        print("4. Display daily steps chart")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            calculate_bmi()
        elif choice == "4":
            show_chart()
        elif choice == "5":
            print("Thank you for using Fitness Data Tracker.")
            break
        else:
            print("Invalid menu option. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()
