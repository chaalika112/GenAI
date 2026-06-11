#find common elements between 2 sets
#find all unique values
#find the union of the 2 sets
#find the diff b/w 2 sets
#count unique words in a sentence


set1 = {12, 15, 18, 22, 25, 30, 35, 40, 45, 50}

set2 = {18, 22, 27, 30, 33, 40, 48, 55, 60, 65}

print("Common elemetns b/w two sets:", set1.intersection(set2))

print("All unique values:", set1.symmetric_difference(set2))

print("Union of 2 sets:", set1.union(set2))

print("Difference between 2 sets:", set1.difference(set2))