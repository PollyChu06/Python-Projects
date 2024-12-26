import imageio.v3 as iio

# Define a list of filenames for the images
filenames = ['team-pic1.png', 'team-pic2.png']

# Initialize an empty list to store the image data
images = []

# Loop through each filename in the list of filenames
for filename in filenames:
    # Read the image data from the file using imageio.imread() and append it to the images list
    images.append(iio.imread(filename))

# Write the images list to a GIF file with specified duration and loop settings
iio.imwrite('team.gif', images, duration=500, loop=0)
