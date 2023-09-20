#Name: Vansh Bataviya
#Email: vansh.bataviya94@myhunter.cuny.edu
#Date: 09/19/2023
#This highlights what was covered in Lec_4

#Group Work
val = 2%5
print(val)
val = 5%5
print(val)
val = 10%5
print(val)
val = (24+5)%26
print(val)

#⁡⁣⁢⁣ Quizzes and Unix
# Using command line to go through your file system instead of a graphical interface
# “Directory”: another word for a folder
# How to see what’s in the folder? Remember there is no graphical interface only the terminal. $ls will list the contents of the current folder.
# How to make a new folder? $mkdir newFolder will create a new folder
# How to see what folder youre in, ie where in the file system you are? $pwd⁡

#Challenge - Group Work
import turtle
teddy = turtle.Turtle()

teddy.color("#000000") #black
teddy.color("#FFFFFF") #white
teddy.color("#0000FF") #blue
teddy.color("#FF00FF") #purple
teddy.color("#424242") #gray

turtle.exitonclick()

#⁡⁣⁢⁣ Recap Colors:
    # Can specify by name.
    # Can specify by numbers:
        # Amount of Red, Green, and Blue (RGB).
        # Adding light, not paint:
            # Black: 0% red, 0% green, 0% blue
            # White: 100% red, 100% green, 100% blue⁡
    # ⁡⁣⁢⁣Can specify by numbers (RGB):
        # Fractions of each:
            # e.g. (1.0, 0, 0) is 100% red, no green, and no blue.
        # 8-bit colors: numbers from 0 to 255:
            # e.g. (0, 255, 0) is no red, 100% green, and no blue.
        # Hexcodes (base-16 numbers)...

#⁡⁣⁢⁣ 𝗔𝗿𝗿𝗮𝘆𝘀
    # 𝗔𝗻 𝗮𝗿𝗿𝗮𝘆 𝗶𝘀 𝗮 𝘀𝗲𝗾𝘂𝗲𝗻𝗰𝗲 𝗼𝗳 𝗲𝗹𝗲𝗺𝗲𝗻𝘁𝘀, 𝗺𝘂𝗰𝗵 𝗹𝗶𝗸𝗲 𝗮 𝗹𝗶𝘀𝘁
    # 𝗔 𝟮𝗗 𝗮𝗿𝗿𝗮𝘆 𝗶𝘀 𝗹𝗶𝗸𝗲 𝗮 𝗴𝗿𝗶𝗱 𝗼𝗳 𝗲𝗹𝗲𝗺𝗲𝗻𝘁𝘀, 𝘁𝗵𝗶𝗻𝗸 𝗮 𝗹𝗶𝘀𝘁 𝗼𝗳 𝗹𝗶𝘀𝘁𝘀. 
    # 𝗖𝗮𝗻 𝗸𝗲𝗲𝗽 𝗼𝗻 𝗮𝗱𝗱𝗶𝗻𝗴 𝗱𝗶𝗺𝗲𝗻𝘀𝗶𝗼𝗻𝘀(𝟯𝗗, 𝗲𝘁𝗰.)
    # 𝗖𝗮𝗻 𝗮𝗰𝗰𝗲𝘀𝘀 𝗽𝗶𝗲𝗰𝗲𝘀/𝘀𝗹𝗶𝗰𝗲𝘀 𝗮𝘀 𝘄𝗲 𝗱𝗼𝘄𝗶𝘁𝗵 𝘀𝘁𝗿𝗶𝗻𝗴𝘀 𝗮𝗻𝗱 𝗹𝗶𝘀𝘁𝘀

    # 𝗪𝗲 𝘄𝗶𝗹𝗹 𝘂𝘀𝗲 𝟮 𝘂𝘀𝗲𝗳𝘂𝗹 𝗽𝗮𝗰𝗸𝗮𝗴𝗲𝘀 𝗳𝗼𝗿 𝗶𝗺𝗮𝗴𝗲𝘀:
        #𝗻𝘂𝗺𝗽𝘆: 𝗻𝘂𝗺𝗲𝗿𝗶𝗰𝗮𝗹 𝗮𝗻𝗮𝗹𝘆𝘀𝗶𝘀 𝗽𝗮𝗰𝗸𝗮𝗴𝗲
        # 𝗽𝘆𝗽𝗹𝗼𝘁: 𝗽𝗮𝗿𝘁 𝗼𝗳 𝗺𝗮𝘁𝗽𝗹𝗼𝘁𝗹𝗶𝗯 𝗳𝗼𝗿 𝗺𝗮𝗸𝗶𝗻𝗴 𝗴𝗿𝗮𝗽𝗵𝘀 𝗮𝗻𝗱 𝗽𝗹𝗼𝘁𝘀

    # 𝗧𝗼 𝗰𝗿𝗲𝗮𝘁𝗲 𝗮𝗻 𝗶𝗺𝗮𝗴𝗲 𝗳𝗿𝗼𝗺 𝘀𝗰𝗿𝗮𝘁𝗰𝗵:
    # 𝟭 𝗜𝗺𝗽𝗼𝗿𝘁 𝘁𝗵𝗲 𝗹𝗶𝗯𝗿𝗮𝗿𝗶𝗲𝘀.⁡
import matplotlib.pyplot as plt
import numpy as np
    #⁡⁣⁢⁣ 2 Create the image– easy to set all color
    # 1 to 0% (black):⁡
# num = 0
# img = np.zeros( (num,num,3) )
#     #⁡⁣⁢⁣ 2 to 100% (white):⁡
# img = np.ones( (num,num,3) )
    #⁡⁣⁢⁣ 3 Do stuff to the pixels to make your image
    # 4 You can display your image:⁡
# plt.imshow(img)
# plt.show()
#     #⁡⁣⁢⁣ 5 And save your image:⁡
# plt.imsave("myImage.png", img)

#⁡⁣⁢⁣ Slicing and Image Examples
    # Basic pattern: img[rows, columns, channels] with: start:stop:step.
    # Assuming the libraries are imported, what do the following code fragments produce:⁡
img = np.zeros( (10,10,3) )
img[0:10,0:5,0:1] = 1
    #⁡⁣⁢⁣ Basic pattern: img[rows, columns, channels] with: start:stop:step.
    # Assuming the libraries are imported, what do the following codefragments produce:⁡
num = 10
img = np.zeros( (num,num,3) )
img[0:2,:,2:3] = 1.0
    #⁡⁣⁢⁣ Basic pattern: img[rows, columns, channels] with: start:stop:step.
    # Assuming the libraries are imported, what do the following codefragments produce:⁡
num = int(input("Enter size"))
img = np.zeros( (num,num,3) )
img[:,::2,1] = 1.0

#⁡⁣⁢⁣ Challenge (Group Work)
    # Basic pattern: img[rows, columns, channels] with: start:stop:step.
    # Assuming the libraries are imported, what do the following code fragments produce:
    #1⁡
img = np.ones( (10,10,3) )
img[0:10,0:5,0:2] = 0
    #2
num = int(input("Enter size"))
img = np.ones( (num,num,3) )
img[::2,:,1:] = 0
    #3
img = np.zeros( (8,8,3) )
img[::2,::2,0] = 1

#⁡⁣⁢⁣ Decisions⁡
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y must be equal")

    #⁡⁢⁣⁡⁣⁢⁣ (This was just a first glance, will do much more on decisions over the next several weeks.)⁡
