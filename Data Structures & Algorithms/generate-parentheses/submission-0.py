class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add parenthesis if open < n
        # only add closing parenthesis if closedN < openN
        # valid if openN == closedN == n

        stack = []
        res = []

        def backtrack(openN , closeN):
            # base case
            if openN == closeN == n:
                res.append("".join(stack))
            
            # recursion
            if openN < n :
                stack.append('(')
                backtrack(openN +1 , closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(')')
                backtrack(openN , closeN +1)
                stack.pop()
        
        backtrack(0,0)
        return res