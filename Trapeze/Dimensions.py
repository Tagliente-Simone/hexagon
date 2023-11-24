from Trapeze import Main as m

def calculate_trapeze_dimensions(radius, compo, config):


    #compos = ["4-3", "5-4-3", "6-5-4", "8-7-6-5", "9-8-7-6"]
    
        
    if compo == "4-3":
        B_max = 8.314 * radius
        b_min = 5.158 * radius
        b_med = 7.163 * radius
        h_max = 3.723 * radius
        h_min = 1 * radius

        return m.main(B_max, b_min, b_med, h_min, h_max, radius, config)
    
    if compo == "5-4-3":
        B_max = 10.312 * radius
        b_min = 5.156 * radius
        b_med = 9.156 * radius
        h_max = 5.654 * radius
        h_min = 1 * radius

        return m.main(B_max, b_min, b_med, h_min, h_max, 2*radius, config)
    
    if compo == "6-5-4":
        B_max = 12.312 * radius 
        b_min = 7.156 * radius
        b_med = 11.156 * radius
        h_max = 5.465 * radius
        h_min = 1 * radius

        return m.main(B_max, b_min, b_med, h_min, h_max, 2*radius, config)
    
    if compo == "8-7-6-5":
        B_max = 16.312 * radius
        b_min = 9.156 * radius
        b_med = 15.156 * radius
        h_max = 7.197 * radius
        h_min = 1 * radius

        return m.main(B_max, b_min, b_med, h_min, h_max, 3*radius, config)
    
    if compo == "9-8-7-6":
        B_max = 18.312 * radius
        b_min = 11.156 * radius
        b_med = 17.156 * radius
        h_max = 7.197 * radius
        h_min = 1 * radius
        return m.main(B_max, b_min, b_med, h_min, h_max, 3*radius, config)
    
        
    
    