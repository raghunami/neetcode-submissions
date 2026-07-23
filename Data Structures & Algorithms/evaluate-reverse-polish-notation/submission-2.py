class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operand_stack = []
        operators = ['+', '-', '/', '*']
        
        for n in tokens:
            if n not in operators:
                operand_stack.append(int(n))
            else:
                first_popped = operand_stack.pop()
                second_popped = operand_stack.pop()

                if n == '+':
                    operand_stack.append(second_popped + first_popped)
                elif n == '-':
                    operand_stack.append(second_popped - first_popped)
                elif n == '*':
                    operand_stack.append(second_popped * first_popped)
                elif n == '/':
                    operand_stack.append(int(second_popped / first_popped))
        return operand_stack[-1]