# task 3
# Name:  Gayatri Aniruddha
# Student id: 30945305
# Start date: 25/08/2019
# Last modified date: 08/09/2019
# Description:
# This program calculates the population remaining at the end of a single year's cycle. Here we don't consider changes in food.
# We open town_start.txt in read mode and open town_end.txt in write mode.
# fp1 is the file handler for town_start.txt and fp2 is the file handler for town_end.txt
# To read the contents in town_start.txt we use readlines() which reads the entire content of a file and returns it as a list.
# Firstly, food is allocated at the beginning of every year. Now, if food is greater then or equal to the population, there's no problem.
# However, if food is lesser than the population, people leave the town such that food is completely available for the remaining popultion.
# Hence, the new value of population becomes that of the food.
# The population increases by 30% every year, hence the new population becomes 1.3 times the old population.
# Every 18 years, it's a draft year. In a draft year, the population decreases by 40%.
# Thus, the new population becomes 60% i.e 0.6 times the old population.
# Finally, we are doing the calculations for one year, hence the value of year is incremented by one.
# Source - Gavin's Lecture Notes

# Opening town_start.txt in read mode, town_end.txt in write mode
fp1 = open('town_start.txt','r')
fp2 = open('town_end.txt','w')

# Reading the contents of the file
fp1_content = fp1.readlines()

# Converting the contents of fp1_content into integer data type for calculations
food = int(fp1_content[0])
population = int(fp1_content[1])
year = int(fp1_content[2])

# When food is not sufficient, some part of population leaves the town
if(food < population):
    population = food

# If the year is a draft year, the population decreases by 40% i.e 0.6 times the old population
if(year%18 == 0):
    # Increase in population by 30%
    population = int((1.3*population))
    # Decrease in population by 40%
    population = int((0.6*population))
else:
    #Increase in population by 30%
    population = int((1.3*population))

# For proper approximation, so that we don't have a fractional value of the population
population = int(population)

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








