#Write a program that takes the name of a text file, reads from the file and displays the
#number of lines in that file.
with open("C:/Users/FaithOdunayoAdeosun/Documents/ATS_Assessment2/poem.txt", mode="r", encoding= "utf8", newline="") as f:
    for count, line in enumerate(f):
        pass
print(f'The number of lines in poem.txt file is', count+1)
    