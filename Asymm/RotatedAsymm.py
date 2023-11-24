class RotatedAsymHex:
    
    def __init__(self, a, b, b_med, h_min, h_max, origin_x, origin_y):
        self.a = a
        self.b = b
        self.b_med = b_med
        self.h_min = h_min
        self.h_max = h_max
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.verts = [(self.origin_x - b_med/2, self.origin_y - (self.h_max/2)),
                        (self.origin_x + b_med/2, self.origin_y - self.h_max/2),
                        (self.origin_x + a/2, self.origin_y - (self.h_max/2 - self.h_min)),
                        (self.origin_x + b/2, self.origin_y + self.h_max/2),
                        (self.origin_x - b/2, self.origin_y + self.h_max/2),
                        (self.origin_x - a/2, self.origin_y - (self.h_max/2 - self.h_min))
                      ]
        
        
        
    def update_points(self, slack_x, slack_y):
        
        self.origin_x += slack_x
        self.origin_y += slack_y
        
        for i in range(len(self.verts)):
            self.verts[i] = (self.verts[i][0] + slack_x, self.verts[i][1] + slack_y)
             
        
        
    def rotate180(self):
        
                self.verts = [(self.origin_x + self.b_med/2, self.origin_y + self.h_max/2),
                                (self.origin_x - self.b_med/2, self.origin_y + self.h_max/2),
                                (self.origin_x - self.a/2, self.origin_y + (self.h_max/2 - self.h_min)),
                                (self.origin_x - self.b/2, self.origin_y - self.h_max/2),
                                (self.origin_x + self.b/2, self.origin_y - self.h_max/2),
                                (self.origin_x + self.a/2, self.origin_y + (self.h_max/2 - self.h_min)),
                                ]