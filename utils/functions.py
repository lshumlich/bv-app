"""This is the Problem Solving Code (PSC) for our API

This is an example of seperation of concern.
"""

def math(operator, parm1, parm2):
    """Simple example of the PSC for an API

    The operator can be + - followed by two numbers. 
    The operator will be performed on the two numbers.
    """

    if operator == '+':
        return parm1 + parm2
    elif operator == '-':
        return parm1 - parm2
    else:
        raise TypeError(f"Invalid operator: ${operator}. Options are - +")
