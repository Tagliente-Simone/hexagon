from Asymm import Asymm as t
from Asymm import RotatedAsymm as rt
from Configuration import Configuration as config


def place_asym_hexs(B, b, b_med, h_min, h_max, radius):
    
    origin = [h_max/2, B/2]
    asym_hexs = []
    
    rotate180 = True
    
    iter = 0
    
    max_origin_x = 0
    max_origin_y = 0
    
    while True:
        
        if iter % 2 == 0:
            origin[0] = h_max/2
        else:
            origin[0] = h_max - 0.25*h_max
        
        while True:
            if  rotate180:
                asym_hexs.append(t.AsymHex(B, b, b_med, h_min, h_max, origin[0], origin[1], 0))
                asym_hexs[-1].angle = 180

            else:
                asym_hexs.append(t.AsymHex(B, b, b_med, h_min, h_max, origin[0], origin[1], 0))
                asym_hexs[-1].rotate180()
                


                
            if max_origin_x < origin[0]:
                max_origin_x = origin[0]
                
            if origin[0] + h_max + h_max/2  +inter > rect_width:
                break
            else:
                origin[0] += h_max  + inter

        rotate180 = not rotate180

        if max_origin_y < origin[1]:
            max_origin_y = origin[1]
                
        if origin[1] + B + B/2 - 1.32*(B-b_med)/2 + inter > rect_height:
            break
        else:
            origin[1] += B - 1.32*(B-b_med)/2  + inter

        
            
        iter += 1
        
    
    slack_y = rect_height - max_origin_y - B/2
    slack_x = rect_width - max_origin_x - h_max/2
    
    for asym_hex in asym_hexs:
        asym_hex.update_points(slack_x/2, slack_y/2)
    

        
    
    return asym_hexs


def place_rotated_asym_hexs(B, b, b_med, h_min, h_max, radius):

    origin = [B/2, h_max/2]
    asym_hexs = []

    rotate180 = True
    
    iter = 0

    max_origin_x = 0
    max_origin_y = 0

    

    while True:
        
        if iter % 2 == 0:
            origin[1] = h_max/2
        else:
            origin[1] = h_max - 0.771*h_max

        while True:
            if rotate180:
                asym_hexs.append(rt.RotatedAsymHex(B, b, b_med, h_min, h_max, origin[0], origin[1], 0))
                asym_hexs[-1].rotate180()
                
            else:
                asym_hexs.append(rt.RotatedAsymHex(B, b, b_med, h_min, h_max, origin[0], origin[1], 0))
                asym_hexs[-1].angle = 0
                asym_hexs[-1].angle = 180

            if origin[1] + h_max + h_max/2  +inter > rect_height:
                break
            else:
                origin[1] += h_max  + inter


        if origin[0] + B + B/2 - 1.32*(B-b_med)/2 + inter > rect_width:
            break
        else:
            origin[0] += B - 1.32*(B-b_med)/2  + inter

        rotate180 = not rotate180
        iter += 1

    last_origin = [asym_hexs[-1].origin_x, asym_hexs[-1].origin_y]
    print(last_origin)

    slack_x = rect_width - last_origin[0] - B/2
    slack_y = rect_height - last_origin[1] - h_max/2

    for asym_hex in asym_hexs:
       asym_hex.update_points(slack_x/2, slack_y/2)

    return asym_hexs
    




def main(B_max, b_min, b_med, h_max, h_min, radius, config):

    global rect_height
    global rect_width
    global inter

    rect_width = config.rect_width
    rect_height = config.rect_height


    inter = config.inter
    
    asym_hexs = place_asym_hexs(B_max, b_min, b_med, h_max, h_min, radius)

    rotated_asym_hexs = place_rotated_asym_hexs(B_max, b_min, b_med, h_max, h_min, radius)

    if len(rotated_asym_hexs) > len(asym_hexs):
        return rotated_asym_hexs
    
    else:
        return asym_hexs