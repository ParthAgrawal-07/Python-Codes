data_file = open("data.txt","w")    # open file in write mode
data_file.write("Hello World\n") # write to the file
data_file=open("data.txt","a")
data_file.write("Hello World")
data_file = open("data.txt","r")    # open file in read mode
print(data_file.read()) # read the file
data_file.close()
