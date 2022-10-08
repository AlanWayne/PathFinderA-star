class Cell:
    x = 0
    y = 0
    
    # states: field, wall, start, end
    state = ''
    
    
    neighbors = []
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        