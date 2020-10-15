#!python3
# Volume Calculator
# Feel free to rename your variables
"""

Introduction:

> This is a program for calculating the volume of different geometries.

> You need to input variables namely geometry length and height. Then the program will calculate the geometry volume and display the result.

> The geometry list:
[ Cuboid , Cube , Cylinder , Cone(round) , Cone(sided) , Sphere ]

Instructions for use:

1 - You need to choose one geometry from the geometry list.

2 - You need to enter the data of the geometry which you want to calculate in the input box, and then press Enter.

3 - The program automatically calculates the volume of the geometry and displays the results.

4 - When you finish using the program, you can choose to exit. If you do not choose to exit, the system will automatically return to the original interface, allowing you to re-select the geometry calculation.

"""

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print("\n\n")
    print("==================== Volumetric calculator ====================")
    print("\n\n")
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts

    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements
    
    return measurements

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    title()


main()
