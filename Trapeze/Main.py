from Trapeze import Trapeze as t
from Trapeze import RotatedTrapeze as rt
from Configuration import Configuration

def place_trapezes(B, b, b_med, h_min, h_max, radius):
    
    origin = [h_max/2, B/2]
    trapezes = []
    
    rotate180 = True
    
    while True:
        
        
        origin[0] = h_max/2
        
        while True:
            if rotate180:
                trapezes.append(t.Trapeze(B, b, b_med, h_min, h_max, origin[0], origin[1], 0))
                trapezes[-1].rotate180()
                trapezes[-1].angle = 180
            else:
                trapezes.append(t.Trapeze(B, b, b_med, h_min, h_max, origin[0], origin[1], 0))
                
            if origin[0] + h_max + h_max/2 + inter > rect_width:
                rotate180 = not rotate180
                break
            else:
                origin[0] += h_max + inter
        if origin[1] + B + B/2 + inter - radius > rect_height:
            break
        else:
            origin[1] += B + inter - radius

    last_origin = (trapezes[-1].origin_x, trapezes[-1].origin_y)
    
    slack_y = rect_height - last_origin[1] - B/2
    slack_x = rect_width - last_origin[0] - h_max/2
    
    for trapeze in trapezes:
        trapeze.update_points(slack_x/2, slack_y/2)
    

        
    
    return trapezes


def place_rotated_trapezes(B, b, b_med, h_min, h_max, radius):

    origin = [B/2, h_max/2]
    trapezes = []

    rotate180 = True

    while True:

        origin[0] = B/2

        while True:
            if rotate180:
                trapezes.append(rt.RotatedTrapeze(B, b, b_med, h_min, h_max, origin[0], origin[1], 0))
                trapezes[-1].rotate180()
                trapezes[-1].angle = 180
                rotate180 = not rotate180
            else:
                trapezes.append(rt.RotatedTrapeze(B, b, b_med, h_min, h_max, origin[0], origin[1], 0))
                rotate180 = not rotate180

            if origin[0] + B + B/2 + inter - radius > rect_width:
                
                break
            else:
                origin[0] += B + inter - radius
        if origin[1] + h_max + h_max/2 + inter > rect_height:
            rotate180 = not rotate180
            break
        else:
            rotate180 = not rotate180
            origin[1] += h_max + inter


    last_origin = (trapezes[-1].origin_x, trapezes[-1].origin_y)

    slack_y = rect_height - last_origin[1] - h_max/2
    slack_x = rect_width - last_origin[0] - B/2

    for trapeze in trapezes:
        trapeze.update_points(slack_x/2, slack_y/2)

    return trapezes
    




def main(B_max, b_min, b_med, h_max, h_min, radius, config):

    global rect_height
    global rect_width
    global inter

    rect_width = config.rect_width
    rect_height = config.rect_height


    inter = config.inter
    
    trapezes = place_trapezes(B_max, b_min, b_med, h_max, h_min, radius)

    rotated_trapezes = place_rotated_trapezes(B_max, b_min, b_med, h_max, h_min, radius)
    
    if len(rotated_trapezes) > len(trapezes):
        return rotated_trapezes
    
    else:
        return trapezes