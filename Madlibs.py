'''
Write a program to create nice story.
TODO: Create MadLibs
			Add something from you: IF
'''

print "Mad Libs started"

name = raw_input("Enter a name: ")
if len(name) == 0:
  name = "LazyBoy"

adjectives1 = raw_input("Write 1st adjective: ")
if len(adjectives1) == 0:
  adjectives1 = "slow"
adjectives2 = raw_input("Write 2nd adjective: ")
if len(adjectives2) == 0:
  adjectives2 = "dull"
adjectives3 = raw_input("Write 3rd adjective: ")
if len(adjectives3) == 0:
  adjectives3 = "gruff"

verb1 = raw_input("Write 1st verb: ")
if len(verb1) == 0:
  verb1 = "bum"
verb2 = raw_input("Write 2nd verb: ")
if len(verb2) == 0:
  verb2 = "loiter"
verb3 = raw_input("Write 3rd verb: ")
if len(verb3) == 0:
  verb3 = "potter"

noun1 = raw_input("Write 1st noun: ")
if len(noun1) == 0:
  noun1 = "cup"
noun2 = raw_input("Write 2nd noun: ")
if len(noun2) == 0:
  noun2 = "fan"
noun3 = raw_input("Write 3rd noun: ")
if len(noun3) == 0:
  noun3 = "contrabass"
noun4 = raw_input("Write 4th noun: ")
if len(noun4) == 0:
  noun4 = "airbrush"

animal = raw_input("Write the name of some animal ")
if len(animal) == 0:
  animal = "aardvark"
food = raw_input("What food do you like? ")
if len(food) == 0:
  food = "Brussels sprouts"
fruit = raw_input("What fruit would you like to eat? ")
if len(fruit) == 0:
  fruit = "durian"
number = raw_input("What is you like number? ")
if len(number) == 0:
  number = "13"
superhero = raw_input("Who is you favorite superhero? ")
if len(superhero) == 0:
  superhero = "Plastic Man"
country = raw_input("Which country do you like to visit? ")
if len(country) == 0:
  country = "SanEscobar"
dessert = raw_input("What dessert did you eat last week? ")
if len(dessert) == 0:
  dessert = "spinach"
year = raw_input("Give me some year ")
if len(year) == 0:
  year = "1347"

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world." 
print STORY % (adjectives1, name, verb1, adjectives2, noun1, noun2, animal, food, verb2, noun3, fruit, adjectives3, name, verb3, number, name, superhero, superhero, name, country, name, dessert, name, year, noun4)