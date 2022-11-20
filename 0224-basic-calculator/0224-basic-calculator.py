class Solution:
    def calculate(self, s: str) -> int:
        result,current,sign,stack = 0,0,1,[]
        
        for c in s:
            if c.isdigit():
                current = current * 10 + int(c)
            elif c in  "+-":
                result += (current * sign)
                current = 0
                if c =="-":
                    sign = -1
                else:
                    sign  = 1
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ")":
                result += (current * sign)
                result *= stack.pop()
                result += stack.pop()
                current = 0
        return result + (current * sign)
            