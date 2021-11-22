from helper_functions import *
#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = "/Users/suvoj/Desktop/BTH/assgn1code/images/"
imgpath = datafolder + "1.jpg" 
#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels 
pixel_values = read_colorimg(imgpath)
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
numb_rows = len(pixel_values) - 2
numb_colns = len(pixel_values[0]) - 2
#
#----------------------------------------WRITE YOUR CODE HERE----------------------------------------
# Create a data structure to store updated pixel information

new_pixel_values = [[0 for col in range(numb_colns)] for row in range(numb_rows)]
# Define the 3 x 3 mask as a tuple of tuples
mask = ((-1,-1,-1), (-1,8,-1), (-1,-1,-1))

# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(pixel_values,row,col):
    local_pixels = [p[(col-1):(col+2)] for p in pixel_values[(row-1):(row+2)]]   
    return local_pixels

# Implement a function to flatten a 2D list or a 2D tuple
def flatten(input):
    output = [x for y in input for x in y]
    return output
    

# For each of the pixel values, excluding the boundary values
    # Create little local 3x3 box using list slicing
for row in range(1, numb_rows+1):
        for col in range(1, numb_colns+1):
            neighbour_pixels = get_slice_2d_list(pixel_values, row, col)
            # Apply the mask
            new_mask = flatten(mask)
            new_neighbour_pixels = flatten(neighbour_pixels)
            mult_result = map(lambda x,y: x*y , new_neighbour_pixels,new_mask)
            # Sum all the multiplied values and set the new pixel value
            new_pixel_values[row-1][col-1] = sum(list(mult_result))

   
#        
#----------------------------------------END YOUR CODE HERE----------------------------------------
# Verify your result
verify_result(pixel_values, new_pixel_values, mask)
# View the original image and the edges of the image
view_images(imgpath, new_pixel_values)