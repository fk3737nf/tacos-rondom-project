from  PIL import Image, ImageDraw, ImageFont  # this imports the image and image font when i'm doing my project for the image part

#  Brian Hullan ITEC 1150-60. This is my final project code tha will generate a recipe book of taco recipes including a rondom pictur of a tco and three rondomly genrated recipes.



# my first step is to open the image that i'll use for my poject. to do that i'm using image = image.open to open it.
image = Image.open('christine-siracusa-vzX2rgUbQXM-unsplash.jpg')    # this opens the image that will use for the project.

# the next step i'm going to resize my picture not more than 800 or less
image.thumbnail((800, 800))                  # resizing image to 800 using image.thubnall this will resize it and use   (()) to put the numbers between


# the next step is going to be image .show()  so that it shows my image when i run it



# next step i'm going  to draw a text around my image

draw = ImageDraw.Draw(image)

# for next one i'm going to use font color for text on the image. so i downloaded DjaVusans from the website

font = ImageFont.truetype('DejaVuSans (1).ttf', 40)    # this will create the font text on the image and choose 40 for the font size


# 40 as for font size

# for the draw text around my image i'm using draw.text to draw text on my image
draw.text([10,475], 'Random Taco Cookbook', fill= 'red', font = font)   # for that is going to be Random Taco Cookbook
# use 10, 475 to draw the text and the text will show on the image.
# for the color i choose red.


image.show()  # this shows the image when every thing is typed and resized the picture it will show the outcome

#  since i finished everything i'm going to go head and save my picture so that it appears on the project side

image.save('Rondom tacos recipe .jpeg')   # Saving the image as this will show up on the project side and i will be able to access it




