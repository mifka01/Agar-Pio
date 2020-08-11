import math

def get_distance(point1_pos: tuple, point2_pos: tuple):
    dx = point1_pos[0] - point2_pos[0]
    dy = point1_pos[1] - point2_pos[1]
    distance = math.sqrt(dx*dx + dy*dy)
    return distance