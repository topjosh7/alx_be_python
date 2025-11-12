# daily_reminder.py

print("=== Personal Daily Reminder ===")

# 1. Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# 2. Determine reminder using match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:  # default if input is unexpected
        reminder = f"'{task}' has unspecified priority"

# 3. Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# 4. Display the reminder in the exact format expected
print(f"\nReminder: {reminder}")
