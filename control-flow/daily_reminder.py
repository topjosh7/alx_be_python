# daily_reminder.py
# Program that gives a daily reminder based on task priority and time sensitivity

# Prompt user for task details
task = input("Enter your task for today: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Process the task based on priority using match case
match priority:
    case "high":
        reminder = f"Your task '{task}' is of HIGH priority. Make sure to focus on it first."
    case "medium":
        reminder = f"Your task '{task}' has a MEDIUM priority. Try to complete it after high-priority tasks."
    case "low":
        reminder = f"Your task '{task}' is of LOW priority. You can do it when you have free time."
    case _:
        reminder = f"Your task '{task}' has an UNKNOWN priority level."

# Add condition for time sensitivity
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"

# Display the customized reminder
print(reminder)
