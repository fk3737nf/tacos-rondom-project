from  PIL import Image, ImageDraw, ImageFont  # this imports the image and image font when i'm doing my project for the image part

#  Brian Hullan ITEC 1150-60. This is my final project code tha will generate a recipe book of taco recipes including a rondom pictur of a tco and three rondomly genrated recipes.



# my first step is to open the image that i'll use for my poject. to do that i'm using image = image.open to open it.
image = Image.open('christine-siracusa-vzX2rgUbQXM-unsplash.jpg')    # this opens the image that will use for the project.

# the next step i'm going to resize my picture not more than 800 or less
image.thumbnail((800, 800))                  # resizing image to 800 using image.thubnall this will resize it and use   (()) to put the numbers between


# the next step is going to be image .show()  so that it shows my image when i run it

image.show()  # this shows the image when every thing is typed and resized the picture it will show the outcome

#  since i finished everything i'm going to go head and save my picture so that it appears on the project side

image.save('Rondom tacos recipe .jpeg')   # Saving the image as this will show up on the project side and i will be able to access it

