import datetime
import random
import holidays

# Start and end days
start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 1, 31)

# Definition for MA holidays
moroccan_holidays = holidays.Morocco(years=start_date.year)

id_intervals = {
    29845: [1, 2, 3, 4, 5, 6, 7],  # Monday to Sunday
    83749: [2, 3, 4, 5, 6],       # Tuesday to Saturday
    42016: [1, 3, 5],             # Monday, Wednesday, Friday
    70124: [2, 4, 6],             # Tuesday, Thursday, Saturday
    29847: [2, 3, 4, 5, 6],  # Monday to Sunday
    83709: [2, 3, 4, 5, 6],       # Tuesday to Saturday
    42056: [1, 3, 5],             # Monday, Wednesday, Friday
    79124: [11, 12, 15],             # wednesday, Tuesday, Friday
}

results = []
num_results = {id_: 0 for id_ in id_intervals}

# Loop through each ID and its corresponding intervals
while id_intervals:
    # Choose a random ID from the remaining IDs
    id_ = random.choice(list(id_intervals.keys()))

    if num_results[id_] == len(id_intervals[id_]):
        del id_intervals[id_]
        continue

    # Choose a random day from the remaining days for this ID
    day = random.choice(id_intervals[id_])

    # Calculate the date for the current day in the interval
    current_date = start_date + datetime.timedelta(days=day-1)

    # Check if the current date is within the specified month
    if current_date.month != start_date.month:
        continue
        #  random ingestion time for the current day
    ingestion_time = datetime.datetime(
        current_date.year,
        current_date.month,
        current_date.day,
        random.randint(0, 23),
        random.randint(0, 59),
        random.randint(0, 59),
        random.randint(0, 999)
    )
    # Check if the current day is a Moroccan holiday
    if current_date in moroccan_holidays:
        print(f"Flow for the count {id_} of the flow was ingested on holiday {moroccan_holidays[current_date]} at {ingestion_time}")

    #  random ingestion time for the current day
    ingestion_time = datetime.datetime(
        current_date.year,
        current_date.month,
        current_date.day,
        random.randint(0, 23),
        random.randint(0, 59),
        random.randint(0, 59),
        random.randint(0, 999)
    )

    # Add the result to the list
    results.append({'ID': str(id_), 'Ingestion Time': ingestion_time})
    num_results[id_] += 1

random.shuffle(results)
print('{:<10}{}'.format('ID', 'Ingestion Time'))
for result in results:
    print('{:<10}{}'.format(result['ID'], result['Ingestion Time']))
