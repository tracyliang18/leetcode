class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        num = []
        for t in tokens:
            if t == '+' or t == '-' or t == '*' or t == '/':
                b= num.pop()
                a = num.pop()
                num.append(self.calc(t,a,b))
            else:
                num.append(self.tonum(t))
        return num[0]


    def tonum(self,s):
        try:
            return int(s)
        except ValueError:
            return float(s)

    def calc(self,op, a, b):
        if op == '+':
            return a+b
        if op == '-':
            return a-b
        if op == '*':
            return a*b
        if op == '/':
            return int(a*1.0/b)


su = Solution()
tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print su.evalRPN(tokens)
print(int(-0.7))


