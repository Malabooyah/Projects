import numpy as np
import matplotlib.pyplot as plt

#Bench Press Workout Data
weights = np.array([
    [135,185,205,225,245],
    [135,185,205,225,205]
    ])
reps= np.array([
    [12,10,8,4,2],
    [12,10,7,3,5]
    ])

##Calculates volumes for each set
set_volumes= weights * reps

##Overall Stats
total_volume_per_workout =np.sum(set_volumes, axis=1)
total_reps_per_workout = np.sum(reps, axis=1)
average_weight_per_workout = np.mean(weights, axis=1)
average_reps_per_workout = np.mean(reps, axis=1)
max_weight_per_workout = np.max(weights, axis=1)
hardest_set_per_workout = np.argmax(set_volumes, axis=1) + 1

best_workout = np.argmax(total_volume_per_workout) + 1
overall_max_weight = np.max(weights)

print("Bench Press Workout Analysis")
print("============================")

#Shows stats per workout
for i in range(len(weights)):
    print(f"\nWorkout {i+1}")
    print("----------------------------")
    print(f"Weights: {weights[i]}")
    print(f"Reps: {reps[i]}")
    print(f"Set Volumes: {set_volumes[i]}")
    print(f"Total Reps: {total_reps_per_workout[i]}")
    print(f"Total Volume: {total_volume_per_workout[i]}")
    print(f"Average Weight: {round(average_weight_per_workout[i], 2)}")
    print(f"Average Reps: {round(average_reps_per_workout[i], 2)}")
    print(f"Heaviest Set: {max_weight_per_workout[i]}")
    print(f"Hardest Set(by volume): Set {hardest_set_per_workout[i]}")

#Shows overall stats over time
print("\nOverall Analysis")
print("----------------------------")
print(f"Total Volume per Workout: {total_volume_per_workout}")
print(f"Best Workout: {best_workout}")
print(f"Overall Heaviest Weight: {overall_max_weight}")

## Data Visualization in a graph
workouts= np.arange(1, len(total_volume_per_workout)+1)
plt.plot(workouts, total_volume_per_workout, marker='o')

for i, v in enumerate(total_volume_per_workout):
    plt.text(workouts[i], v+40, str(v), ha='center')

plt.title('Workout Volume Progress')
plt.xlabel("Workout Number")
plt.ylabel("Total Volume")
plt.grid(True, alpha=0.3)
plt.show()
