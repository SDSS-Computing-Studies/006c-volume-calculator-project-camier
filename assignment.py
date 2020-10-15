#!python3
# Volume Calculator
# Feel free to rename your variables
"""

Introduction:

> This is a program for calculating the volume of different geometries.

> You need to input variables namely geometry length and height. Then the program will calculate the geometry volume and display the result.

> The geometry list:
[ Cuboid , Cube , Cylinder , Cone(round) , Cone(sided) , Sphere ]

> If you want to know more introduction and the principle of program operation, please check out the attachment [ Program description ].


Instructions for use:

1 - You need to choose one geometry from the geometry list.

2 - You need to enter the data of the geometry which you want to calculate in the input box, and then press Enter.

3 - The program automatically calculates the volume of the geometry and displays the results.

4 - When you finish using the program, you can choose to exit. If you do not choose to exit, the system will automatically return to the original interface, allowing you to re-select the geometry calculation.

"""

import math
def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Chara Yu
    # Modified:
    print("\n\n")
    print("==================== Volumetric calculator ====================")                                  
    for i in range(0,5):
        print("*" * (5 - 1 - i) + " " * (i + 1) + "                                                      " + " " * i +"*" * (5 - 1 - i))
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Jacky Xu
    # Modified:
    insbool = int(input("\nIf you want to see the instructions, please enter the number 1, otherwise, enter 0: \n"))
    if insbool == 1:
        print("Introduction:\n> This is a program for calculating the volume of different geometries.\n> You need to input variables namely geometry length and height. Then the program will calculate the geometry volume and display the result.\n> The geometry list:\n[ Cuboid , Cube , Cylinder , Cone(round) , Cone(sided) , Sphere ]\n> If you want to know more introduction and the principle of program operation, please check out the attachment [ Program description ].\nInstructions for use:\n1 - You need to choose one geometry from the geometry list.\n2 - You need to enter the data of the geometry which you want to calculate in the input box, and then press Enter.\n3 - The program automatically calculates the volume of the geometry and displays the results.\n4 - When you finish using the program, you can choose to exit. If you do not choose to exit, the system will automatically return to the original interface, allowing you to re-select the geometry calculation.")
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    if shape == 1:
        global a,b,c
        a = float(input("\nEnter the length: "))
        b = float(input("\nEnter the width: "))
        c = float(input("\nEnter the height: "))
        return a,b,c
    elif shape == 2:
        a = float(input("\nEnter the length: "))
        return a
    elif shape == 3:
        a = float(input("\nEnter the radius: "))
        b = float(input("\nEnter the height: "))
        return a,b
    elif shape == 4:
        a = float(input("\nEnter the bottom area: "))
        b = float(input("\nEnter the height: "))
        return a,b
    elif shape == 5:
        a = float(input("\nEnter the radius: "))
        b = float(input("\nEnter the height: "))
        return a,b
    elif shape == 6:
        a = float(input("\nEnter the radius: "))
        return a
    else:
        print("\nWrong number.")
        exit()

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    if questions == 1:
        global answer
        answer = a * b * c
        return answer 
    elif questions == 2:
        answer = a * a * a
        return answer
    elif questions == 3:
        answer = math.pi * a ** 2 * b
        return answer
    elif questions == 4:
        answer = 1 / 3 * a * b
        return answer
    elif questions == 5:
        answer = 1 / 3 * math.pi * a ** 2 * b
        return answer
    elif questions == 6:
        answer = 4 / 3 * math.pi * a ** 3
        return answer
    

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    #1 chang fang ti 2:zheng fang ti 3:yuanzhu 4:jinzita 5:yuanzhuiti
    title()
    exitbool = int(1)
    while exitbool != 0:
        instructions()
        print("\n\nNumber 1 stands for cuboid\n\nNumber 2 stands for cube\n\nNumber 3 stands for cylindrical\n\nNumber 4 stands for pyramid\n\nNumber 5 stands for cone\n\nNumber 6 stands for sphere")
        shapebool = int(input("\nChoose one number: "))
        getParams(shapebool)
        getInputs(shapebool)
        print("\nThe answer is: " + str(answer))
        exitbool = int(input("\nIf you want to stop it, enter 0 to stop, enter 1 to continue: "))


main()
