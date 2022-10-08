class Cell:
    x = 0
    y = 0
    
    price = 0
    dist = 0
    value = 0
    
    # states: field, wall, start, end
    state = ''
    
    
    neighbors = []
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []
        
    def __repr__(self):
        return repr(self.x*10 + self.y)
        