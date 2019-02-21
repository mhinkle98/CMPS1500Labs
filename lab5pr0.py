'''lab5pr0 - ppm imaging
Max Hinkle, 02/21/2019'''
'''Test Change for github'''

red = "255 0 0 "
green = "0 255 0 "
blue = "0 0 255 "
white = "255 255 255 " 
black = "0 0 0 "

def get_header(width, height):
    ''' returns .ppm header '''
    new_header = "P3\n" + str(width)+ " " + str(height) + "\n255\n"
    return new_header


def netherlands(width, height):
    colors = [red, white, blue]
    values = []
    numcolors = len(colors)
    for color in colors:
        for i in range(height // numcolors):
            for i in range(width):
                values.append(color)
    valuestr = ''.join(values)       
    nether = open("Netherlands.ppm", 'w')
    nether.write(get_header(width, height))
    nether.write(valuestr)
    nether.close()
    nethertxt = open("Netherlands.txt", 'w')
    nethertxt.write(get_header(width, height))
    nethertxt.write(valuestr)
    return values

def main():
    '''user_width = input("Please, enter width: ")
    user_height = input("Please, enter height: ")
    file_name = input("Please, enter output file name: ")
    get_header(user_width, user_height)'''
    netherlands(40,30)
    '''print("The output has been written to", file_name +
          "\nView the result in XnView.")'''
    
main()
