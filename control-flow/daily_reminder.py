# daily_reminder.py

# 1. Prompt for user input exactly as expected
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# 2. Match-case for priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:  # default if input is unexpected
        reminder = f"'{task}' has unspecified priority"

# 3. If statement for time-bound modification
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# 4. Print exactly in the format expected
print(f"Reminder: {reminder}")