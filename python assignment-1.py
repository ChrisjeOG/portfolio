#python assignment-1.py Chrisje Ganzevoort
#welcome
print("Welcome to this awesome site")

#asking for the first name and make it start with a capital letter
name = input("What is your first name? ")
name = name.strip()
name = name.title()

print("Welcome " + str(name) + ",let's make an account")

#asking for the last name and make it start with a capital letter
last_name = input("What is your last name? ")
last_name = name.strip()
last_name = name.title()

if last_name == "Ganzevoort" or last_name == "ganzevoort":
    print ("We are family")
else:
    print("Cool name")

#count the amount of letters in the names and giving points
count_name = len(name)
count_last_name = len(last_name)

#it needs to be a string so I can print it
total = str(count_name + count_last_name)

print("You have now " + (total) + " points")

#turning it back into int so we can continue the count
total = int(count_name + count_last_name)

#asking age
age = input("What is your age? ")
final_age = int(age)

if final_age >= 18:
    print ("Join the club my friend")
else:
    print ("You can't join the club...")
    exit()

#make a string of it again
total = str(total + final_age)

print("You have now " + (total) + " points")

#turning it back into int so we can continue the count
total = int(total)

#asking for the gender
gender = input("What is your gender? F, M, Neutral? ")
if gender == "F" or gender == "f":
    total = total + 5
elif gender == "M" or gender == "m":
    total = total + 1
else:
    total = total + 3

#make a string of it again
total = str(total)
print("You have now " + (total) + " points")
#turning it back into int so we can continue the count
total = int(total)

hometown = input("Where do you live? ")
hometown = hometown.strip()
hometown = hometown.title()
#giving points to hometown awnser
if hometown == "Utrecht" or hometown == "Uuuu":
    total = total + 10
    print("030!")
elif hometown == "Amsterdam" or hometown == "Damsko":
    total = total + 5
    print("020!")
else:
    total = total + 1
    print ("This is far away")

#make a string of it again
total = str(total)
print("You have now " + (total) + " points")
#turning it back into int so we can continue the count
total = int(total)

netflix = input("Where do you watch your series? ")
netflix = netflix.strip()
netflix = netflix.title()

#giving points to serie awnser
if netflix == "Netflix":
    total = total + 10
    print("Thanks for your awnser")
elif netflix == "Youtube":
    total = total + 5
    print("Thanks for your awnser")
elif netflix == "Popcorntime":
    total = total + 4
    print("It's not allowed, but okay! Thanks for your awnser")
else:
    total = total + 1
    print ("Thanks for your awnser")

#make a string of it again
total = str(total)

#saying goodbye
print("You have a total of " + (total) + " points, thank you and have a nice day")
