import datetime

current_time = datetime.datetime.now().strftime("%d-%m-%Y, %I:%M:%S: %p")

status={
    1:"generate note",
    2:"view note",
    3:"exit"
}
 
def write_log(log):
    file=open('h.txt','a')
    file.write(log)
    file.close()

q_list=[]

while(1):
    q_dict = {}
    
    print("\n----------Welcom to python E - Note-----------")

    print("\npress 1 for Generate Note")
    print("press 2 for view Note")
    print("press 3 for exit")

    choice=input("\nEnter your choice :")
    if choice.isdigit():
        choice = int(choice)
        if choice==1:
            while(1):
                name=str(input("\nEnter Pythone E-Note Generate Name :")).capitalize()
                if name.isdigit():
                    print("---Invalid input pliz enter name---")
                else:
                    break
            title=input("Enter Python E-Note Title :").capitalize()
            content=input("Enter E-Note Content :").capitalize()

            q_dict['username'] = name
            q_dict['title'] = title
            q_dict['content'] = content

            q_list.append(q_dict)
            log_msg=f"\n------------------------------------------\n{current_time}-[{status[1]}]\nE-Note Title : {title}\nE-Note Description : {content}\n              Note Generator : {name}\n"
            write_log(log_msg)

        elif choice==2:
            if q_list==[]:
                print("\n-------plizz anter content----------")
            else:
            

                for i in q_list:
                    print(f"\nE-Note Generator Name: {i['username']}")
                    print(f"E-Note Title: {i['title']}")
                    print(f"E-Note content: {i['content']}")
                    print("--------------------------------\n")
                    
                log_msg=f"\n------------------------------------------\n{current_time}-[{status[2]}]\nE-Note Title : {title}\nE-Note Description : {content}\n              Note Generator Name : {name}\n"
                write_log(log_msg)


        elif choice==3:
            log_msg=f"\n{current_time}-[{status[3]}]\n"
            break

        else:
            print("\n-------------Invalid choice plizz enter valid number(1--2--3)---------------")

    else:
        print("\n-------------Invalid choice plizz enter valid number(1--2--3)---------------")

print("--------Thank you---------")


