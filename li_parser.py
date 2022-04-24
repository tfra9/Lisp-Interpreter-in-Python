## Lisp (Scheme) Interpreter in Python
## Parser

import re

from li_lisptypes import Symbol, Boolean, Expression, Atom

def parse(lisp_string: str) -> Expression:
    "Read a Scheme expression from a string."
    ast = generate_ast(normalize_string(lisp_string))
    return ast[0]
    
def normalize_string(lisp_string: str) -> list:
    tokens = re.split('(\s+|\(|\))', lisp_string)
    
    # remove all empty or whitespace only matches, leaves only valid tokens
    return [t for t in tokens if len(t) and not t.isspace()]


# Generate abstract-syntax-tree from tokens list.
def generate_ast(tokens_list: list) -> Expression:
    ast = []
    # Go through each element in the input:
    # - open parenthesis -> find matching parenthesis and make recursive
    #   add the result as an element to the current list
    # - it's an atom -> add it to the current list
    i = 0
    while i < len(tokens_list):
        token = tokens_list[i]
        if token == '(':
            list_content = []
            paren_match = 1 # If 0, parenthesis has been matched.
            while paren_match != 0:
                i += 1
                if i >= len(tokens_list):
                    raise ValueError("Invalid input: Unmatched open parenthesis.")
                token = tokens_list[i]
                if token == '(':
                    paren_match += 1
                elif token == ')':
                    paren_match -= 1
                if paren_match != 0:
                    list_content.append(token)             
            ast.append(generate_ast(list_content))
        elif token == ')':
                raise ValueError("Invalid input: Unmatched close parenthesis.")
        else:
            ast.append(atom(token))
        i += 1
    return ast


def atom(token: str) -> Atom:
    "Numbers become numbers; every other token is a symbol."
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            # add
            if token == "#f":
                return Boolean(False)
            elif token == "#t":
                return Boolean(True)
            else:
                return Symbol(token)

