#create a set of colors.
#add "yellow" to the start of the set
#remove "blue" from the set
#check whether "green" is in the set
#print all elements using a for loop
#count unique words in a sentence 

colors = {"Red", "Black", "Blue", "Green", "White"}

print(colors)

for color in colors:
    print(color)

if "Green" in colors:
    print("Yes, Green exists in the set")
else:
    print("No, Green doesnot exist in the set")

# A set is unordered, which means it doesnot keep track of first, last or position
# "yellow" will be added randomly

colors.add("Yellow")

print(colors)

colors.remove("Blue")

print(colors)

sentence = "apple mango apple orange mango banana"

print(sentence)

words = sentence.split()

unique_words = set(words)

print("Unique words:", unique_words)
print("Count:", len(unique_words))


