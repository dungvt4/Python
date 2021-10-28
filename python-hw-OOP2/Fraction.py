import math

class Fraction:
    def __init__(self, nr, dr):
        assert  dr != 0, f"ZeroDevisonError: mẫu số {dr} ko hợp lệ"
        self.nr = nr
        self.dr = dr
        self.reduce()
    
    def __repr__(self):
        # try: 
            if self.dr != 0:
                if self.nr == 0:
                    return f"0"
                elif self.dr == 1:
                    return f"{self.nr}"
                if self.nr // self.dr <0:
                    self.nr = self.nr * (-1)
                    return(f"{self.nr}/{abs(self.dr)}")
                return f"{abs(self.nr)}/{abs(self.dr)}"
        # except Exception as e:
        #     print("Error:", e)
    
    def hcf(self):
            mins = min(abs(self.nr), abs(self.dr))
            for ucln in range (mins, 0, -1):
                if self.nr % ucln == 0 and self.dr % ucln == 0:
                    return ucln
    
    def reduce(self):
            if self.dr != 0 and self.dr != 1 and self.nr != 0:
                ucln = self.hcf()
                self.nr = int(self.nr/ucln)
                self.dr = int(self.dr/ucln)

        
    def __mul__(self, other):
        if type(other) == int:
           return Fraction(self.nr * other, self.dr) 
        return Fraction(self.nr * other.nr, self.dr * other.dr)
    
    def __add__(self, other):
        if type(other) == int:
            return Fraction(self.nr + other * self.dr, self.dr)
        return Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
    
    def __sub__(self, other):
        if type(other) == int:
            return Fraction(self.nr - other * self.dr, self.dr)
        return Fraction(self.nr * other.dr - other.nr * self.dr, self.dr * other.dr)



# x = Fraction(2,6)
# print(x)
# y = Fraction(-1,-6)
# print(y)
# print(x*y)
# print(x+y)
# print(x-y)

z = Fraction(4,0)
print(z)

