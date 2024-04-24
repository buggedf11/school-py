myfile = open("/workspaces/school-py/write_it.txt","w")
myfile.write("Line1\n")
myfile.write("This is line 2 \n")
myfile.write("That makes this line 3 \n")
myfile.close

myfile = open("/workspaces/school-py/write_it.txt","r")
print(myfile.read())
myfile.close()