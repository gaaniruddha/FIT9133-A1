# task 4
# Name:  Gayatri Aniruddha
# Student id: 30945305
# Start date: 25/08/2019
# Last modified date: 08/09/2019
# Description:
# This program creates a complete simulation of the town as per the algorithm provided.
# We open town_start.txt in read mode and open town_end.txt in write mode.
# fp1 is the file handler for town_start.txt and fp2 is the file handler for town_end.txt
# To read the contents in town_start.txt we use readlines() which reads the entire content of a file and returns it as a list.
# 1: Food is handed out to the town.
# 2: If food is lesser than population, people leave the town. T
# Hence, new value of population is equal to the value of food.
# 3a: Food is sorted among the population. One unit of food is given to one unit of population.
# Hence, new value of food after sorting becomes food - population.
# 3b: Now, (1/5)th of the food is thrown away, hence new value of food becomes (4/5) i.e (0.8) times the old value of food.
# 4: Population grows. Every year, population grows by 30%. Thus, new population is 1.3 times the old population.
# 5: Every 18 years, a draft year takes place and population decrease by 40%.
# Hence, population now becomes 60% i.e 0.6 times the old population.
# 6: The food order is placed and food is delivered for the next year.
# Food ordered is for 80% i.e for 0.8 times of the population.
# Hence, new value of food now becomes existing food + food ordered for remaining population.
# Value of year is incremented.
# Now, the above logic is placed in a while loop, which runs as long as population and food are positive i.e greater than or equal to zero and
# the value of year is less than 100, as this town should run normally for 100 years.
# Finally, we should be able to come out of the loop immediately, whenever the value of population and food becomes zero.
# Hence, we have used a break statement for that.
# Source - Gavin's Lecture Notes

# Opening town_start.txt in read mode, town_end.txt in write mode
fp1 = open('town_start.txt','r')
fp2 = open('town_end.txt','w')

# Reading the contents of town_start.txt
fp1_content = fp1.readlines()

# Converting the contents of fp1_content into integer data type for calculations
food = int(fp1_content[0])
population = int(fp1_content[1])
year = int(fp1_content[2])

while( population >= 0 and food >= 0 and year < 100):

    # 1 and 2
    if(food < population):
         population = food

    # 3 Food is sorted and rotten food is thrown away
    food = food - population
    food = int(0.8*food)

    # 4 Population grows
    # 5 Every 18 years, a draft year takes place
    if(year % 18 == 0):
        # Increase in population by 30%
        population = int((1.3*population))
        # Decrease in population by 40%
        population = int((0.6*population))

    else:
        # Increase in population by 30%
        population = int((1.3*population))

    # 6 Food is ordered and food is delivered for the next year.
    food = food + int(((0.8)*population))

    # Incrementing the year by one
    year = (year + 1)

    # Break to come out of the loop, when population and food become 0
    if(population == 0 and food == 0):
        break

# Converting into int for approximation
food = int(food)
population = int(population)
year = int(year)

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
