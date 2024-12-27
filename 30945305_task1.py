# task 1
# Name:  Gayatri Aniruddha
# Student id: 30945305
# Start date: 25/08/2019
# Last modified date: 08/09/2019
# Description:
# Here, we are opening town_start.txt in read mode and town_end.txt in write mode.
# fp1 is the file handler for town_start.txt and fp2 is the file handler for town_end.txt.
# To read the contents of town_start.txt, we use the command readlines() which reads the entire content of a file and returns it as a list.
# We then iterate through the contents of town_start.txt using a for loop and copy it in town_end.txt.
# Source - Gavin's Lecture Notes

# Opening town_start in read mode, using the file handler fp1
fp1 = open('town_start.txt','r')

# Reading the contents of town_start.txt and saving it in file_content
file_content = fp1.readlines()

# Opening town_end.txt in write mode, using the file handler fp2
fp2 = open('town_end.txt','w')

# Iterating through contents of town_start.txt and copying it in town_end.txt
for i in file_content:
    fp2.write(i)

# Closing the two files
fp1.close()
fp2.close()

