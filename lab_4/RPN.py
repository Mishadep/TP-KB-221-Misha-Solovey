class Calculator:
    def __init__(self):
        self.digits = ('1','2','3','4','5','6','7','8','9','0')
        self.operators = ('+', '-', '*', '/', '^')

    def is_number(self, num):
        return all(char in self.digits for char in num)

    def get_priority(self, operator):
        if operator in ('+', '-'):
            return 0
        elif operator in ('*','/'):
            return 1
        elif operator == '^':
            return 2 

    def to_to_reverse(self, input):
        stack = []
        output = []
        
        for token in input:
            if self.is_number(token):
                output.append(token)
                continue
                
            if token == '(':
                stack.append(token)
                continue
            
            if token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
                continue    
            
            if token in self.operators:
                op_priority = self.get_priority(token)
                while stack and stack[-1] in self.operators and self.get_priority(stack[-1]) >= op_priority:
                    output.append(stack.pop())
                stack.append(token)
                
        while stack:
            output.append(stack.pop())
            
        return output

    def calculate(self, expression):
        stack = []
        
        for token in expression:
            if self.is_number(token):
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = 0
                
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    result = operand1 / operand2
                elif token == '^':
                    result = operand1 ** operand2
                    
                stack.append(result)
                
        return stack[0]
    

if __name__ == '__main__':
    calc = Calculator()
    input = "3+4*2/(1-5)^2"
    to_reverse = calc.to_to_reverse(input)
    
    print("Reverse : ", to_reverse)
    print("Result: ", calc.calculate(to_reverse))
