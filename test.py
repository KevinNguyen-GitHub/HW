class Matrix:
    def __init__(self,rowsp):  #FIXME: Add necessary parameters and default values
        if len(rowsp) == 0:
            self.row = []
        self.row = rowsp
        self.col = [[row[i] for row in self.row] for i in range(len(self.row[0]))]
        return
        
    def __add__(self, other):
        if len(self.row) != len(other.row) or len(self.col) != len(other.col):
            raise ValueError("Mismatched dimensions")
        return Matrix([[self.row[i][j] + other.row[i][j] for j in range(len(self.row[0]))] for i in range(len(self.row))])
        
    def __sub__(self, other):
        if len(self.row) != len(other.row) or len(self.col) != len(other.col):
            raise ValueError("Mismatched dimensions")
        return Matrix([[self.row[i][j] - other.row[i][j] for j in range(len(self.row[0]))] for i in range(len(self.row))])
        
    def __mul__(self, other):  
        if type(other) == float or type(other) == int:
            return Matrix([[self.row[i][j] * other for j in range(len(self.row[0]))] for i in range(len(self.row))])
        elif type(other) == Matrix:
            return Matrix([[Matrix.dotProduct(row,col) for col in other.col] for row in self.row])
        elif type(other) == Vec:
            print("FIXME: Insert implementation for MATRIX-VECTOR multiplication")  #REPLACE
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def dotProduct(row,col):
        return sum(row[i] * col[i] for i in range(len(row)))
    
    def __rmul__(self, other):  
        if type(other) == float or type(other) == int:
            return Matrix([[self.row[i][j] * other for j in range(len(self.row[0]))] for i in range(len(self.row))])
        else:
            print("ERROR: Unsupported Type.")
        return
    
    def __str__(self):
        """prints the rows and columns in matrix form """
        return '\n'.join(str(e) for e in self.row)
    
    def __eq__(self, other):
        """overloads the == operator to return True if 
        two Matrix objects have the same row space and column space"""
        this_rows = self.row_space()
        other_rows = other.row_space()
        this_cols = self.col_space()
        other_cols = other.col_space()
        return this_rows == other_rows and this_cols == other_cols

    def __req__(self, other):
        """overloads the == operator to return True if 
        two Matrix objects have the same row space and column space"""
        this_rows = self.row_space()
        other_rows = other.row_space()
        this_cols = self.col_space()
        other_cols = other.col_space()
        return this_rows == other_rows and this_cols == other_cols
    
    def order(self):
        return (self.row, self.row[0])
    
    def set_col(self,j,u):
        if len(u) == len(self.col[j-1]):
            self.col[j-1] = u
        else:
            raise ValueError("Imcompatible Row Lenth")
        return
        
    def set_row(self,i,v):
        if len(v) == len(self.row[i-1]):
            self.row[i-1] = v
        else:
            raise ValueError("Imcompatible Row Lenth")
        return
    
    def set_entry(self,i,j,x):
        self.row[i-1][j-1] = x
    
    def get_col(self,j):
        return self.col[j-1]
    
    def get_row(self,i):
        return self.row[i-1]
    
    def get_entry(self,i,j):
        return self.row[i-1][j-1]
    
    def col_space(self):
        return self.col
    
    def row_space(self):
        return self.row
    
    def get_diag(self,k):
        if k == 0:
            return[self.col[i][i] for i in range(len(self.col))]
        if k > 0:
            return[self.col[i+(k)][i] for i in range(len(self.col)-k)]
        if k < 0:
            return[self.col[i][i+(-k)] for i in range(len(self.col)-(-k))] 
        
A = Matrix([[1, 2, 3], [4, 5, 6]])
print("Original Row Space:", A.row_space())
print("Original Column Space:", A.col_space())
print("Original Matrix:")
print(A)
print()


A.set_row(1, [10, 20, 30])
print("Modification #1")
print("Row Space after modification:", A.row_space())
print("Column Space after modification:", A.col_space())
print("Modified Matrix:")
print(A)
print()

A.set_col(2, [20, 50])
print("Modification #2")
print("Row Space after modification:", A.row_space())
print("Column Space after modification:", A.col_space())
print("Modified Matrix:")
print(A)
print()

A.set_row(2, [40, 50, 6])
print("Modification #3")
print("Row Space after modification:", A.row_space())
print("Column Space after modification:", A.col_space())
print("Modified Matrix:")
print(A)
print()

A.set_entry(2, 3, 60)
print("Modification #4")
print("Row Space after modification:", A.row_space())
print("Column Space after modification:", A.col_space())
print("Modified Matrix:")
print(A)
print()


print("The 2nd row is:", A.get_row(2))
print("The 3rd column is:", A.get_col(3))
print()

