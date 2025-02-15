data_file = open("data.txt","r")    # open file in read mode
print(data_file.readable()) # check if file is readable
#print(data_file.read()) # read the file
print(data_file.readline()) # read first line of the file
print(data_file.readline()) 
data_file.close()