
'''
THIS IS UNFINISHED!!!
I will finish it on monday because i couldn't finish it before deadline because i was having some technical problems with my laptop.
I'm so sorry for this unfinished project. Thank you for your understanding.

'''


nameList = ["Ahmet Çoban","Mehmet Erdem","Şimal Topal","Elif Yiğit","Ömer Cengiz","Güven Uzun"]

name_surname = input("Please enter your name and surname: ")

trys = 3
success = False

while trys > 0 :
    
    if name_surname in nameList :
        print('Welcome ',name_surname)
        success = True

        break

    else:
        print("Try again. You have " + str(trys) + "trys left.")
        trys = trys - 1

if success:
    
    course = input("Enter 5 course name seperated by ',' : ")
    course_list = course.split(",")
    print(course_list)


    

    Min = 3
    Max = 5
    course_taken = len(course_list)
    




else:
    print("Please try again later.")
        
        

    


