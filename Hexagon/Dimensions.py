import math
from Hexagon import Main as m

def calculate_hexagon_dimensions(radius, n_rows, rows_array, index, config):
    """
    Calculates the dimensions of a hexagonal shape based on the input parameters.

    Args:
        radius (float): The radius of the hexagon.
        n_rows (int): The number of rows in the hexagon.
        rows_array (list[int]): An array of integers representing the rows in the hexagon.
        index (int): An index used by the `m.compute` function.

    Returns:
        int: The total number of tubes in the hexagon.

    Raises:
        None.

    """
    
    
    # Calculate the minimum width of the hexagon
    B_min = 2 * radius * (max(rows_array) - 1)
    b_min = 2 * radius * (min(rows_array) - 1)
    obl_min = int(n_rows / 2) * radius * 2
    temp = (B_min - b_min) / 2
    h_min = math.sqrt(obl_min ** 2 - temp ** 2)

    # Calculate the maximum width of the hexagon
    h_max = h_min + radius
    k = h_max / h_min
    B_max = B_min * k
    b_max = b_min * k

    # Compute the total number of tubes in the hexagon

    # 3-4-3 B_max = 8.32, h_max = 5.472, b_max = 5.161
    # 6-7-8-9-8-7-6 B_max = 18.312 h_max = 12.392, b_max = 11.156
    # 4-5-6-5-4 B_max = 12.312, h_max = 8.93, b_max = 7.156
    # 5-6-7-8-7-6-5 B_max = 16.314, h_max = 12.394, b_max = 9.158

    if len(rows_array) == 7:
        if rows_array[0] == 5:
            frame = m.compute(radius * 16.312, radius * 12.392, radius * 9.156, index, config)
            return frame
        else:
            frame = m.compute(radius * 18.312, radius * 12.392, radius * 11.156, index, config)
            return frame
        
    if len(rows_array) == 5:
        if rows_array[0] == 4:
            frame = m.compute(radius * 12.312, radius * 8.93, radius * 7.156, index, config)
            return frame
        else:
            frame = m.compute(radius * 10.312 , radius * 8.93, radius * 5.156, index, config)
            return frame

    if len(rows_array) == 3:
        
        frame = m.compute(radius * 8.32, radius * 5.472, radius * 5.156, index, config)
        return frame
          
    return frame
