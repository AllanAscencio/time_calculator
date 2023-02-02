def add_time(start, duration, day=""):
    # Getting hold of the start and dividing it into elements
    input_day = day.lower()
    start = start.split()
    split_time = start[0].split(":")
    am_pm = start[1]
    hours = int(split_time[0])
    minutes = int(split_time[1])
    list_am_pm = ["AM", "PM"]

    # Getting hold of the duration and dividing it into elements
    duration = duration.split(":")
    duration_hours = int(duration[0])
    duration_min = int(duration[1])

    # Adding start and duration to get total of hours and minutes
    sum_of_all_hours = hours + duration_hours
    total_minutes = minutes + duration_min

    days_of_the_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# ------------------------------------------------------------------------------------------------------------------ #
    days_elapsed = 0

    # Check if the sum of the total hours is more than 24hrs or equal to
    if duration_hours == 24 and total_minutes <= 59:
        days_elapsed += 1
        if days_elapsed <= 1:
            if input_day in days_of_the_week:
                print(f"{hours}:{total_minutes} {am_pm}, {input_day.capitalize()} (next day)")
        elif days_elapsed <= 1 and input_day in days_of_the_week:
            print(f"{hours}:{total_minutes} {am_pm}, {input_day.capitalize()}")

    # Check if the duration hours are 24hrs but minutes are more than 59
    elif duration_hours == 24 and total_minutes > 59 and am_pm == "AM":
        total_minutes = total_minutes - 60
        hours += 1
        am_pm = "PM"
        print(f"{hours}:0{total_minutes} {am_pm}")

    elif duration_hours == 24 and total_minutes > 59 and am_pm == "PM":
        total_minutes = total_minutes - 60
        hours += 1
        am_pm = "AM"
        if input_day in days_of_the_week:
            index = days_of_the_week.index(f"{input_day}") + 2
            print(f"{hours}:0{total_minutes} {am_pm}, {days_of_the_week[index].capitalize()} (2 days later)")
        else:
            print(f"{hours}:0{total_minutes} {am_pm} (2 days later)")

    elif sum_of_all_hours < 12 and total_minutes > 59 and am_pm == "AM":
        total_minutes = total_minutes - 60
        hours += 1
        am_pm = "PM"
        if duration_hours == 0:
            print(f"{hours}:0{total_minutes} {am_pm}")
        else:
            print(f"{hours}:0{total_minutes} {am_pm} (2 days later)")

    elif sum_of_all_hours < 12 and total_minutes < 59:
        if total_minutes < 9:
            if input_day in days_of_the_week:
                print(f"{sum_of_all_hours}:0{total_minutes} {am_pm}, {input_day.capitalize()}")
            else:
                print(f"{sum_of_all_hours}:0{total_minutes} {am_pm}")
        else:
            if input_day in days_of_the_week:
                print(f"{sum_of_all_hours}:{total_minutes} {am_pm}, {input_day.capitalize()}")
            else:
                print(f"{sum_of_all_hours}:{total_minutes} {am_pm}")

    elif sum_of_all_hours > 11 and total_minutes > 59 and am_pm == "AM":
        total_minutes = total_minutes - 60
        am_pm = "PM"
        sum_of_all_hours += 1
        modular_hours = sum_of_all_hours % 12
        if total_minutes < 9:
            if input_day in days_of_the_week:
                print(f"{modular_hours}:0{total_minutes} {am_pm}, {input_day.capitalize()}")
        else:
            print(f"{modular_hours}:{total_minutes} {am_pm}")

    elif sum_of_all_hours > 11 and total_minutes > 59 and am_pm == "PM":
        total_minutes = total_minutes - 60
        am_pm = "PM"
        sum_of_all_hours += 1
        modular_hours = sum_of_all_hours % 12
        if total_minutes < 9:
            if input_day in days_of_the_week:
                print(f"{modular_hours}:0{total_minutes} {am_pm}, {input_day}")
            else:
                print(f"{modular_hours}:0{total_minutes} {am_pm}")
        else:
            print(f"{modular_hours}:{total_minutes} {am_pm}")

    elif sum_of_all_hours > 11 and total_minutes < 59 and am_pm == "PM":
        am_pm = "AM"
        modular_hours = sum_of_all_hours % 12
        days_elapsed = (sum_of_all_hours / 24) + 1
        if total_minutes < 9:
            print(f"{modular_hours}:0{total_minutes} {am_pm}")
        else:
            if input_day in days_of_the_week:
                index = ((days_of_the_week.index(f"{input_day}")) + int(days_elapsed) % 7) % 7
                if int(days_elapsed) == 1:
                    print(f"{modular_hours}:{total_minutes} {am_pm}, {days_of_the_week[index].capitalize()} (next day)")
                else:
                    print(
                        f"{modular_hours}:{total_minutes} {am_pm}, {days_of_the_week[index].capitalize()} ({int(days_elapsed)} days later)")
            else:
                if int(days_elapsed) == 1:
                    print(f"{modular_hours}:{total_minutes} {am_pm} (next day)")
                else:
                    print(f"{modular_hours}:{total_minutes} {am_pm} ({int(days_elapsed)} days later)")


add_time("6:30 PM", "205:12")

