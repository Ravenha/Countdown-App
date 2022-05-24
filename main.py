from datetime import datetime as dt

user_input = input("Enter your goal with a deadline separated by a colon.\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = dt.strptime(deadline, "%m/%d/%Y")
today_date = dt.today()
time_until = deadline_date - today_date

print(f"Time remaining until reaching your goal: {goal} is {time_until.days} days")
