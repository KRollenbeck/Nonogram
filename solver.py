class Nonogram:    
    def __init__(self, rows: list[list[int]], columns: list[list[int]]):
        self.rows = rows
        self.columns = columns
        self.width = len(rows)
        self.height = len(columns)
        self.fields = [[0 for _ in range(self.width)] for _ in range(self.height)]
    
    def show(self):
        for row in self.fields:
            print(row)
    
    def solve():
        pass            

def create() -> Nonogram:
    pass

def solve(nonogram) -> Nonogram:
    pass