import math
class Vec:
    def __init__(self, contents = []):
        """
        Constructor defaults to empty vector
        INPUT: list of elements to initialize a vector object, defaults to empty list
        """
        self.elements = contents
        return
    
    def __abs__(self):
        """
        Overloads the built-in function abs(v)
        returns the Euclidean norm of vector v
        """
        a = math.sqrt(sum(i ** 2 for i in self.elements))
        return a
        
    def __add__(self, other):
        """Overloads the + operator to support Vec + Vec
         raises ValueError if vectors are not same length
        """
        if len(self.elements) != len(other.elements):
            raise ValueError()
        add = []
        for i in range(len(self.elements)):
            add.append(int(self.elements[i] + other.elements[i]))
        return Vec(add)

    
    def __sub__(self, other):
        """
        Overloads the - operator to support Vec - Vec
        Raises a ValueError if the lengths of both Vec objects are not the same
        """
        if len(self.elements) != len(other.elements):
            raise ValueError()
        sub = []
        for i in range(len(self.elements)):
            sub.append(self.elements[i] - other.elements[i])
        return Vec(sub)
    
    
    
    def __mul__(self, other):
        """Overloads the * operator to support 
            - Vec * Vec (dot product) raises ValueError if vectors are not same length in the case of dot product
            - Vec * float (component-wise product)
            - Vec * int (component-wise product)
            
        """
        if type(other) == Vec: #define dot product
            #FIXME: IMPLEMENT
            if len(self.elements) != len(other.elements):
                raise ValueError()
            dp = []
            total = 0
            for i in range(len(self.elements)):
                if type(other) == float:
                    dp.append(self.elements[i] * other.elements[i])
                else: 
                    dp.append(int(self.elements[i] * other.elements[i]))
            for i in range(len(dp)):
                total += dp[i]
            return total
            
            
        elif type(other) == float or type(other) == int: #scalar-vector multiplication
            #FIXME: IMPLEMENT
            scalar = []
            for i in range(len(self.elements)):
                if type(other) == float:
                    scalar.append(self.elements[i] * other)
                else: 
                    scalar.append(int(self.elements[i] * other))
            return Vec(scalar)
            
    
    def __rmul__(self, other):
        """Overloads the * operation to support 
            - float * Vec
            - int * Vec
        """
        scalar = []
        for i in range(len(self.elements)):
            if type(other) == float:
                scalar.append(self.elements[i] * other)
            else: 
                scalar.append(int(self.elements[i] * other))
        return Vec(scalar)
    

    
    def __str__(self): 
        """returns string representation of this Vec object"""
        return str(self.elements) # does NOT need further implementation
    
    def norm(self,p):
        if type(p) != int: raise ValueError("must be an int")
        if type(self) == Vec: 
            return float(((i ** p)**(1/p)) for i in self.elements)
        