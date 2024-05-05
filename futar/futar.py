"""
# Read the data from the file tavok.txt
with open("tavok.txt") as f:
    data = [line.strip().split() for line in f]

# Sort the data by day and journey number
data.sort(key=lambda x: (int(x[0]), int(x[1])))

# Print the first and last trip of the week
print("First trip:", data[0][2], "km")
print("Last trip:", data[-1][2], "km")

# Count the number of days when the courier was off work
off_days = 0
for i in range(1, 8):
    if not any(d[0] == str(i) for d in data):
        off_days += 1
print("Days off:", off_days)

# Determine which day of the week had the most journeys and print it
max_journeys = 0
max_day = 0
for i in range(1, 8):
    day_data = [d for d in data if d[0] == str(i)]
    if len(day_data) > max_journeys:
        max_journeys = len(day_data)
        max_day = i
print("Day with most journeys:", max_day)

# Calculate the total distance travelled on each day and print it
day_distances = {}
"""
# Read the data from the file tavok.txt
with open("tavok.txt") as f:
    data = [line.strip().split() for line in f]

# Sort the data by day and journey number
data.sort(key=lambda x: (int(x[0]), int(x[1])))

# Print the first and last trip of the week
print("First trip:", data[0][2], "km")
print("Last trip:", data[-1][2], "km")

# Count the number of days when the courier was off work
off_days = sum(1 for day, journeys, distance in data if int(journeys) == 1)
print("Number of off days:", off_days)

# Determine which day of the week had the most journeys
most_journeys = max(int(journeys) for day, journeys, distance in data)
print("Day with most journeys:", next(day for day, journeys, distance in data if int(journeys) == most_journeys))

# Calculate the total distance travelled on each day
distances_by_day = {}
for day, journeys, distance in data:
    distances_by_day[day] = distances_by_day.get(day, 0) + int(distance)

# Print the total distance travelled on each day
for day, distance in distances_by_day.items():
    print(f"Day {day}: {distance} km")

# Ask the user for an arbitrary distance and calculate the remuneration
distance = int(input("Enter a distance: "))
if distance <= 2:
    remuneration = 500
elif distance <= 5:
    remuneration = 700
elif distance <= 10:
    remuneration = 900
elif distance <= 20:
    remuneration = 1400
else:
    remuneration = 2000
print("Remuneration for this distance:", remuneration, "Ft")

# Calculate the total remuneration for all the trips
total_remuneration = 0
for day, journeys, distance in data:
    if distance <= 2:
        remuneration = 500
    elif distance <= 5:
       pass
