write_file = __import__('1-write_file').write_file

nb_characters = write_file("text/my_first_file.txt", "This School is so cool!\n")
print(nb_characters)