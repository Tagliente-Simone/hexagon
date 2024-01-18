import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Polygon
import Configuration.Configuration as config
import numpy as np
import random
import string
import uuid


def draw_trapezes(trapezes, config):
    
    # Create a rectangle object with width=120 and height=100
    rect = Rectangle((0, 0), config.rect_width, config.rect_height, facecolor='blue', edgecolor='black', linewidth=2)
    


    # Create a figure and axes object
    fig, ax = plt.subplots()
    
    # Add the rectangle to the axes
    ax.add_patch(rect)

    # Set the limits of the axes

    rect_1 = Rectangle((config.start_originx, config.start_originy), 1200, 1000, linewidth=1, facecolor='green')

    ax.add_patch(rect_1)
    
    for trapeze in trapezes:
        verts = trapeze.verts
        trapeze_polygon = Polygon(verts, fill=True, facecolor='#D3D3D3', edgecolor='black', linewidth=0)
        ax.add_patch(trapeze_polygon)
        # Plotting the dot
        plt.scatter(trapeze.origin_x, trapeze.origin_y, color='black', marker='o')
        
        

            
    rect_2 = Rectangle((config.start_originx, config.start_originy), 1200, 1000, linewidth=1, facecolor='none', edgecolor='red', linestyle='--')
    ax.add_patch(rect_2)

    ax.set_xlim(0, config.rect_width)
    ax.set_ylim(0, config.rect_height)
    
    axis = plt.gca()
    
    # Set the desired step length for the x-axis
    step = 50

    # Generate new tick positions based on the step length for the x-axis
    new_xticks = np.arange(0, config.rect_width, step)
    new_yticks = np.arange(0, config.rect_height, step)
    

    # Set the new tick positions
    axis.set_xticks(new_xticks)
    axis.set_yticks(new_yticks)
    
    # Decrease the font size of x-axis labels
    axis.set_xticklabels(axis.get_xticklabels(), fontsize=5)

    # Decrease the font size of y-axis labels
    axis.set_yticklabels(axis.get_yticklabels(), fontsize=5)


    
    # Set the aspect ratio to 'equal'
    ax.set_aspect('equal')
    
    
    uuid = gen_uuid()
    #plt.axis('off')
    # Display the plot
    #plt.show()
    #if (index == 9999):
    plt.savefig(config.images_path + uuid + "trap.png", dpi=300)
    ##plt.savefig(config.images_path + str(index) + 'hexagon' + str(hex_width) + str(hex_height) + str(hex_side) + rotation + '.png', dpi=300)

    plt.close()

    return uuid

def gen_uuid():
    # Generate a UUID4
    uuid_obj = uuid.uuid4()
    
    # Convert the UUID to a hexadecimal string and remove hyphens
    uuid_hex = str(uuid_obj).replace('-', '')
    
    # Ensure the hexadecimal string is exactly 32 characters long
    if len(uuid_hex) != 32:
        raise ValueError("Generated UUID is not 32 characters long.")
    
    # Generate a random 32-character string
    random_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
    
    # Combine the UUID and random string to make it 64 characters long
    uuid_64 = uuid_hex + random_str
    
    return uuid_64