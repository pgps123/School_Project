list_file = open("vote_list.txt", "r")
vote_file = open("vote_program.txt", "w")

print(list_file.read())
vote_file.writelines(lines)

list_file.close()
vote_file.close()