# Open a file
fo = open("foo.txt", "w+")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)

fo.write( "Python is a great language.\nYeah its great!!\n");
fo.close()

fo = open("foo.txt", "r")
print ("Opening mode : ", fo.mode)
print("file readable: ", fo.readable())
print (fo.read())

# Close opend file
fo.close()


