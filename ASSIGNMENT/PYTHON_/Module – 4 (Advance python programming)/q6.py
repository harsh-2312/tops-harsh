#  Write a Python program to read a file line by line and store it into a list 
fil_name="q4.txt"
emplist = []

def line(fil_name):
    with open(fil_name,"r") as file:
        lines=file.readlines()
        for i in lines:
            emplist.append(i)
        return emplist
    
print(line(fil_name))
    
























#     with open("data_file.txt") as f:
#     content_list = f.readlines()

# # print the list
# print(content_list)

# # remove new line characters
# content_list = [x.strip() for x in content_list]
# print(content_list)