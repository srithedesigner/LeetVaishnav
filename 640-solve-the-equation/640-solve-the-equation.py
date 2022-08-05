class Solution:
    def solveEquation(self, equation: str) -> str:
        
        exp = equation.replace("=", "-(")
        exp += ")"
        
        exp = exp.replace("x", "j")
        
        
        
        exp = eval(exp, {"j" : 1j})
        
        r, i = int(exp.real),int(exp.imag)
        
        
        if i == 0 and r == 0:
            return "Infinite solutions"
        
        if i == 0 or r%i != 0:
            return "No solution"
        
        return f"x={-1*(r//i)}"
    