class PascalTriangle:
    """A class to represent Pascal's triangle"""

    def __init__(self, number_of_rows):
        """Define the triangle and its properties"""
        self.n = number_of_rows
        self.rows = []
    
    def CreateTriangle(self):
        """Create the triangle"""
        for line in range(1, self.n + 1):
            coef = 1
            row = []
            for i in range(1, line + 1):
                row.append(coef)
                coef = int(coef * (line - i) / i)
            self.rows.append(row)

    def PrintTriangle(self):
        """Print the triangle on the console"""
        for row in self.rows:
            print(row)

if __name__ == '__main__':
    pt = PascalTriangle(7)
    pt.CreateTriangle()
    pt.PrintTriangle()
