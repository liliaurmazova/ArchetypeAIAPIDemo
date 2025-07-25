import random
import operator

class ArithmeticExpressionGenerator:
    OPERATORS = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
        ('/', operator.truediv)
    ]

    def generate_expression(self, num_terms=3, min_value=1, max_value=20):
        """
        Generates a random algebraic expression with variable x.
        Example: "2x^2 + 3x + 5" or "x^3 - 4x + 1"
        """
        expression = []
        
        for i in range(num_terms):
            # Generate coefficient (can be 1 and omitted for cleaner look)
            coeff = random.randint(min_value, max_value)
            
            # Generate power for x (0 means constant term, 1 means x, 2+ means x^power)
            power = random.randint(0, 3)
            
            # Build the term
            term = ""
            
            if power == 0:
                # Constant term
                term = str(coeff)
            elif power == 1:
                # Linear term (x)
                if coeff == 1:
                    term = "x"
                else:
                    term = f"{coeff}x"
            else:
                # Higher power term (x^2, x^3, etc.)
                if coeff == 1:
                    term = f"x^{power}"
                else:
                    term = f"{coeff}x^{power}"
            
            expression.append(term)
            
            # Add operator between terms (except for last term)
            if i < num_terms - 1:
                op = random.choice(['+', '-'])
                expression.append(op)
        
        return ' '.join(expression)