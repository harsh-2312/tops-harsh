# Write a Python program to copy the contents of a file to another file. 

#>> with open("q10.txt",'r') as file1 , open("q12.txt",'a') as file2:
    # for i in file1:
    #     file2.write(i)


# >>import shutil 
  
# # use copyfile() 
# shutil.copyfile("q10.txt","q12.txt")


file= open("q10.txt",'r')
copy=file.read()
file.close()

file1= open("q12.txt",'w')
file1.write(copy)
file1.close()

