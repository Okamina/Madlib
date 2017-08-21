'''
Write a program to create nice story.
I add IF statement to fill empty answers. I added variable: count_of_laziness to count the missing words 

TODO: Change stories on your own or more than one.
'''

print ("Mad Libs started")
count_of_laziness = 0

name = input("Enter a name: ")
if len(name) == 0:
  name = "LazyBoy"
  count_of_laziness += 1

adjectives1 = input("Write 1st adjective: ")
if len(adjectives1) == 0:
  adjectives1 = "slow"
  count_of_laziness += 1
adjectives2 = input("Write 2nd adjective: ")
if len(adjectives2) == 0:
  adjectives2 = "dull"
  count_of_laziness += 1
adjectives3 = input("Write 3rd adjective: ")
if len(adjectives3) == 0:
  adjectives3 = "gruff"
  count_of_laziness += 1

verb1 = input("Write 1st verb: ")
if len(verb1) == 0:
  verb1 = "bum"
  count_of_laziness += 1
verb2 = input("Write 2nd verb: ")
if len(verb2) == 0:
  verb2 = "loiter"
  count_of_laziness += 1
verb3 = input("Write 3rd verb: ")
if len(verb3) == 0:
  verb3 = "potter"
  count_of_laziness += 1

noun1 = input("Write 1st noun: ")
if len(noun1) == 0:
  noun1 = "cup"
  count_of_laziness += 1
noun2 = input("Write 2nd noun: ")
if len(noun2) == 0:
  noun2 = "fan"
  count_of_laziness += 1
noun3 = input("Write 3rd noun: ")
if len(noun3) == 0:
  noun3 = "contrabass"
  count_of_laziness += 1
noun4 = input("Write 4th noun: ")
if len(noun4) == 0:
  noun4 = "airbrush"
  count_of_laziness += 1

animal = input("Write the name of some animal ")
if len(animal) == 0:
  animal = "aardvark"
  count_of_laziness += 1
food = input("What food do you like? ")
if len(food) == 0:
  food = "Brussels sprouts"
  count_of_laziness += 1
fruit = input("What fruit would you like to eat? ")
if len(fruit) == 0:
  fruit = "durian"
  count_of_laziness += 1
number = input("What is you like number? ")
if len(number) == 0:
  number = "13"
  count_of_laziness += 1
superhero = input("Who is you favorite superhero? ")
if len(superhero) == 0:
  superhero = "Plastic Man"
  count_of_laziness += 1
country = input("Which country do you like to visit? ")
if len(country) == 0:
  country = "SanEscobar"
  count_of_laziness += 1
dessert = input("What dessert did you eat last week? ")
if len(dessert) == 0:
  dessert = "spinach"
  count_of_laziness += 1
year = input("Give me some year ")
if len(year) == 0:
  year = "1347"
  count_of_laziness += 1
print ("\n")
if count_of_laziness == 19:
  print ("You are the most lazy person in the world")
elif count_of_laziness >= 14:
  print ("You are really lazy")
elif count_of_laziness >= 5:
  print ("You could do better")
elif count_of_laziness > 0:
  print ("Almost your story, you skipped a few words")
else:
  print ("Enjoy your own story")
print ("\n")
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world." 
print (STORY % (adjectives1, name, verb1, adjectives2, noun1, noun2, animal, food, verb2, noun3, fruit, adjectives3, name, verb3, number, name, superhero, superhero, name, country, name, dessert, name, year, noun4))