import random

# stat_block will be the list where all 6 final values will be stored
stat_block = []

# while statement set up to run 6 times to get the stats for stat_block
count = 0
while count <= 5:

# start of the sets of 4d6 rolls.
    firstRollSet = []
    firstRollSet_count = 0
    while firstRollSet_count < 4:
        firstRollSet.append(random.randint(1, 6))
        firstRollSet_count += 1

# print statement to view all 6 of the 4d6 rolls
    print(str(firstRollSet))

# takes the initial lists of rolls and sorts descending in to new list.
# the lowest value is then taken out.
    finalRollSet = sorted(firstRollSet, reverse=True)
    finalRollSet.pop()

# takes the sum of the three highest rolls then appends the result into stat_block
    sumOfRollSet = 0
    for item in finalRollSet:
        sumOfRollSet += item

    stat_block.append(sumOfRollSet)
    count += 1

print(stat_block)
