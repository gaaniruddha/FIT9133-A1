# task 2
# Name:  Gayatri Aniruddha
# Student id: 30945305
# Start date: 25/08/2019
# Last modified date: 08/09/2019
# Description:
# This program calculates the food remaining at the end of a single year's cycle. Here we don't consider changes in population.
# We open town_start.txt in read mode and open town_end.txt in write mode.
# fp1 is the file handler for town_start.txt and fp2 is the file handler for town_end.txt
# To read the contents in town_start.txt we use readlines() which reads the entire content of a file and returns it as a list.
# Firstly, food is allocated at the beginning of every year. Now, if food is greater then or equal to the population, there's no problem.
# However, if food is lesser than the population, people leave the town such that food is completely available for the remaining popultion.
# Hence, the new value of population becomes that of the food.
# At the end of the year, (1/5)th of the food is thrown away. Thus, (4/5)th of the food is remaining.
# Hence, the new value of food becomes (4/5) i.e (0.8) times the value of old food.
# Finally, we are doing the calculations for one year, hence the value of year is incremented by one.
# Source - Gavin's Lecture Notes

# Opening town_start.txt in read mode
fp1 = open('town_start.txt','r')

# Opening town_end.txt in write mode
fp2 = open('town_end.txt','w')

# Reading the contents of town_start.txt and saving it in fp1_content
fp1_content = fp1.readlines()

# Converting the contents of fp1_content into integer data type for calculations
food = int(fp1_content[0])
population = int(fp1_content[1])
year = int(fp1_content[2])

# Calculating food present at the end of one year.
if (food >= population):
    food = int((0.8)*food)
else:
    population = food
    food = int((0.8)*food)

# Incrementing the year value by one
year = year + 1

# Converting into string data type
food = str(food)
population = str(population)
year = str(year)

# Creating a list of values of food, population and year which will be written on town_end.txt file
values = [food, population, year]

# Writing values of food, population, year in town_end.txt
for i in values:
    fp2.write(i)
    fp2.write("\n")

# Closing the two files
fp1.close()
fp2.close()








