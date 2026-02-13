"""
Author: Dharwyn Ivor Olpindo 
Assignment #1
"""
#String
gym_member = "Alex Alliton"

#Float for weight in kg
preferred_weight_kg = 20.5 

#integer for number of reps
highest_reps = 25 

#bolean for membership status
membership_active = True

#Dictionary for workout stats
workout_stats = {
    "Alex": (30, 45, 20), 
    "Jamie": (55, 65, 35),
    "Taylor": (20, 35, 10)
}

#Calculating total workout minutes for each friend
for friend, minutes in list(workout_stats.items()):
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

#2D list for workout minutes
workout_list = [
    workout_stats["Alex"], 
    workout_stats["Jamie"],
    workout_stats["Taylor"]
]

#Extract and print yoga and running minutes for all friends
print("Yoga and Running minutes for all friends:")
friends = ["Alex", "Jamie", "Taylor"]
for i in range(len(workout_list)):
    print(f"{friends[i]}: Yoga: {workout_list[i][0]}, Running: {workout_list[i][1]}")    

#Extract and print weightlifting minutes for the last two friends
print("\nWeightlifting minutes for the last two friends:") 
friends = ["Alex", "Jamie", "Taylor"]
for i in range(-2, 0):
    print(f"{friends[i]}: Weightlifting: {workout_list[i][2]}")

#Check if any friend has total workout minutes greater than or equal to 120 and print a message
for friend in ["Alex", "Jamie", "Taylor"]:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")
#User input 
name = input("\nEnter a friend's name: ")
if name in workout_stats:
    minutes = workout_stats[name]
    total = workout_stats[f"{name}_Total"]
    print(f"{name}'s workout minutes:")
    print(f"Yoga: {minutes[0]}")
    print(f"Running: {minutes[1]}")
    print(f"Weightlifting: {minutes[2]}")
    print(f"Total workout minutes: {total}")
else:
    print(f"Sorry, {name} is not in the workout stats.")

#Find friend with the highest and lowest total workout minutes and print their names and totals
totals = {
    "Alex": workout_stats["Alex_Total"],
    "Jamie": workout_stats["Jamie_Total"],
    "Taylor": workout_stats["Taylor_Total"]
}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"\n{highest_friend} has the highest total workout minutes: {totals[highest_friend]}")
print(f"{lowest_friend} has the lowest total workout minutes: {totals[lowest_friend]}")