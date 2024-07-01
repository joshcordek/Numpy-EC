import numpy as np

# Step 1: Create a 4x3 array of all 2s
print("-----------------------------------------------   STEP ONE   -----------------------------------------------")
array_step_1 = np.full((4, 3), 2)
print(array_step_1)
print("")

# Step 2: Create a 3x4 array with a range from 0 to 110 where each number increases by 10
print("-----------------------------------------------   STEP TWO   -----------------------------------------------")
array_step_2 = np.arange(0, 120, 10).reshape(3, 4)
print(array_step_2)
print("")

# Step 3: Change the layout of the above array to be 4x3, store it in a new array
print("-----------------------------------------------   STEP THREE   -----------------------------------------------")
array_step_3 = array_step_2.reshape(4, 3)
print(array_step_3)
print("")

# Step 4: Multiply every element of the above array by 3 and store the new values in a different array
print("-----------------------------------------------   STEP FOUR   -----------------------------------------------")
array_step_4 = array_step_3 * 3
print(array_step_4)
print("")

# Step 5: Multiply your array from step one by your array from step 2
print("-----------------------------------------------   STEP FIVE   -----------------------------------------------")

#array_step_5 = array_step_1 * array_step_2
#print(array_step_5)


# Step 6: Comment out your code from Step 5 and then multiply your array from step 1 by your array from step 3
print("-----------------------------------------------   STEP SIX   -----------------------------------------------")
array_step_6 = array_step_1 * array_step_3
print(array_step_6)
print("")

