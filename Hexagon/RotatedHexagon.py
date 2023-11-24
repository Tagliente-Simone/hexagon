class RotatedHexagon:
    
    def __init__(self, origin_x, origin_y, hex_width, hex_height, vertical_side_length, angle):
        
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.hex_width = hex_width
        self.hex_height = hex_height
        self.vertical_side_length = vertical_side_length
        self.verts = [(self.origin_x, self.origin_y + self.hex_width/2),
                        (self.origin_x + self.hex_height/2, self.origin_y + self.vertical_side_length/2),
                        (self.origin_x + self.hex_height/2, self.origin_y - self.vertical_side_length/2),
                        (self.origin_x, self.origin_y - self.hex_width/2),
                        (self.origin_x - self.hex_height/2, self.origin_y - self.vertical_side_length/2),
                        (self.origin_x - self.hex_height/2, self.origin_y + self.vertical_side_length/2)
                        ]
        self.angle = angle
    
    
    
    ## Traslate the hexagon by a given slack
    def update_points(self, slack_x, slack_y):
        """
        Translates the hexagon by a given slack in the x and y directions.

        Args:
        - slack_x (float): The amount to translate the hexagon in the x direction.
        - slack_y (float): The amount to translate the hexagon in the y direction.

        Returns:
        None.
        """
        for i in range(len(self.verts)):
            self.verts[i] = (self.verts[i][0] + slack_x, self.verts[i][1] + slack_y)