import random
from datetime import datetime, timedelta

# Define the start and end dates for the data
start_date = datetime(2023, 1, 1, 0, 0, 0)
end_date = datetime(2023, 2, 1, 0, 0, 0)

# Define the holidays in Morocco in January 2023
morocco_holidays = {
    1: "New Year's Day",
    11: "Day of Independence",
}

# Generate a list of datetimes for each line (excluding Sundays)
datetimes = []
used_days = set()
for day in range(1, 32):
    if (start_date + timedelta(days=day - 1)).weekday() == 6:
        continue  # skip Sundays
    while True:
        new_datetime = start_date + timedelta(days=day - 1, seconds=random.randint(1, 60 * 60 * 24))
        if new_datetime.month == 1 and new_datetime.day == day and new_datetime not in datetimes:
            datetimes.append(new_datetime)
            used_days.add(day)
            break

# Generate a list of counts for each line
counts = [random.randint(1, 99999) for _ in range(len(datetimes))]
for i in range(4, len(counts), 5):
    counts[i] = counts[i-1]

# Combine the lists into a table
table = []
for i in range(len(datetimes)):
    time_str = datetimes[i].strftime('%Y-%m-%d %H:%M:%S.%f')
    count_str = f"{counts[i]:05d}"
    day = datetimes[i].day
    if  day in morocco_holidays:
        holiday = morocco_holidays[day]
        table.append((count_str, time_str, holiday))
    else:
        table.append((count_str, time_str, ""))

# Print the table header
print("| Count | Time                       | Holiday                               |")
print("|-------|--------------------- ------|---------------------------------------|")

# Print each row of the table
for row in table:
    count_str, time_str, holiday = row
    print(f"| {count_str} | {time_str:<19} | {holiday:<37} |")
