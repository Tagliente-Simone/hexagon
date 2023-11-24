from Hexagon import Hexagon as hx
from Hexagon import RotatedHexagon as rhx
from Hexagon import Draw as dr
from Configuration import Configuration
import math
## This function places the vertical line of hexagons




def place_vertical_hexagon(hexagons_no_rot, origin_x, origin_y, hex_width, hex_height, hex_side):
    
    last_origin_y = 0

    while True:
        hexagon = hx.Hexagon(origin_x, origin_y, hex_width, hex_height, hex_side)
        hexagons_no_rot.append(hexagon)

        if origin_y > last_origin_y:
            last_origin_y = origin_y
           
        origin_y += hex_height + inter


        ## Check if the hexagon is out of the rectangle
        if origin_y + hex_height/2 > rect_height:
            
            break
 
    return last_origin_y


def place_vertical_hexagon_rotated(hexagons_rot, origin_x, origin_y, hex_width, hex_height, hex_side):

    last_origin_x = 0

    while True:
        hexagon = rhx.RotatedHexagon(origin_x, origin_y, hex_width, hex_height, hex_side)
        hexagons_rot.append(hexagon)

        if origin_x > last_origin_x:
            last_origin_x = origin_x
        
        origin_x += hex_height + inter

        ## Check if the hexagon is out of the rectangle
        if origin_x + hex_height/2 > rect_width:
            break

    return last_origin_x





def test_no_rotation(hexagons_no_rot, hex_width, hex_height, hex_side, index):

    ## Variables for the origin of the first hexagon
    start_origin_x = hex_width/2
    start_origin_y = hex_height/2 

    origin_x = start_origin_x
    origin_y = start_origin_y

    ## Variables for the index of the line
    line_index = 1

    highest_y = 0

    ## Start placing the hexagons
    while True:

        ## Check if the line is out of the rectangle
        if origin_x + hex_width/2 > rect_width:
            break

        last_origin_y = place_vertical_hexagon(hexagons_no_rot, origin_x, origin_y, hex_width, hex_height, hex_side)

        if last_origin_y > highest_y:
            highest_y = last_origin_y

        ## Update the position of the first hexagon of the new line
        if line_index % 2 == 1:
            origin_x += hex_width - (hex_width - hex_side)/2 + inter/(math.sin(math.atan((hex_height) / ((hex_width - hex_side)))))
            origin_y = start_origin_y + hex_height/2 + inter/2

        else:
            origin_x += hex_width - (hex_width - hex_side)/2  + inter
            origin_y = start_origin_y


        line_index += 1
        
    
    ## Draw the hexagons to see the result
    len_no_rotation = len(hexagons_no_rot)
    centering_no_rotation(hexagons_no_rot, highest_y, hex_width, hex_height, hex_side)

    return len_no_rotation
    
def test_rotation(hexagons_rot, hex_width, hex_height, hex_side, index):

    ## Variables for the origin of the first hexagon
    start_origin_x = hex_height/2
    start_origin_y = hex_width/2

    origin_x = start_origin_x
    origin_y = start_origin_y

    ## Variables for the index of the line
    line_index = 1

    highest_x = 0
    
    while True:

        ## Check if the line is out of the rectangle
        if origin_y + hex_width/2 > rect_height:
            break
 
        ## Start placing the hexagons
        last_origin_x = place_vertical_hexagon_rotated(hexagons_rot, origin_x, origin_y, hex_width, hex_height, hex_side)
        
        if last_origin_x > highest_x:
            highest_x = last_origin_x

        ## Update the position of the first hexagon of the new line
        if line_index % 2 == 1:
            origin_y += hex_width - (hex_width - hex_side)/2 + inter/(math.sin(math.atan((hex_height) / ((hex_width - hex_side)))))
            origin_x = start_origin_x + hex_height/2 + inter/2

        else:
            origin_y += hex_width - (hex_width - hex_side)/2  + inter
            origin_x = start_origin_x


        line_index += 1



        

    ## Draw the hexagons to see the result
    len_rotation = len(hexagons_rot)
    centering_rotation(hexagons_rot, highest_x, hex_width, hex_height, hex_side)

    

    return len_rotation

def centering_no_rotation(hexagons_no_rot, highest_y, hex_width, hex_height, hex_side):
    
    last_origin_x = hexagons_no_rot[-1].origin_x

    extreme_point_x = last_origin_x + hex_width/2
    extreme_point_y = highest_y + hex_height/2



    ## Calculate the distance between the extreme point and the border of the rectangle
    distance_x = rect_width - extreme_point_x
    distance_y = rect_height - extreme_point_y
    
    for hexagon in hexagons_no_rot:
        hexagon.origin_x += distance_x/2
        hexagon.origin_y += distance_y/2
        hexagon.update_points(distance_x/2, distance_y/2)

def centering_rotation(hexagons_rot, highest_x, hex_width, hex_height, hex_side):

    last_origin_y = hexagons_rot[-1].origin_y
    
    extreme_point_y = last_origin_y + hex_width/2
    extreme_point_x = highest_x + hex_height/2
    
    ## Calculate the distance between the extreme point and the border of the rectangle

    distance_y = rect_height - extreme_point_y
    distance_x = rect_width - extreme_point_x

    for hexagon in hexagons_rot:
        hexagon.origin_y += distance_y/2
        hexagon.origin_x += distance_x/2
        hexagon.update_points(distance_x/2, distance_y/2)


## Main Function calls

def compute(hex_width, hex_height, hex_side, index, config):

    global rect_height
    global rect_width
    global inter

    ## Variables for the rectangle
    rect_width = config.rect_width
    rect_height = config.rect_height

    ## Variables for the hexagons
    len_no_rotation = 0
    len_rotation = 0

    inter = config.inter

    hexagons_no_rot = []
    hexagons_rot = []

    test_no_rotation(hexagons_no_rot, hex_width, hex_height, hex_side, index)
    test_rotation(hexagons_rot, hex_width, hex_height, hex_side, index)
    #dr.draw_hexagons(hexagons_no_rot)
    #dr.draw_hexagons(hexagons_rot)



    if(len(hexagons_no_rot) > len(hexagons_rot)):
        return hexagons_no_rot
    else:
        return hexagons_rot





        


        







   
