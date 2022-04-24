## Lisp (Scheme) Interpreter in Python
# Interpreter with Eval function


import operator as op
import math
from li_parser import parse
from li_lisptypes import Symbol, Number, String, Boolean, List, Atom, Expression


# Environments

def standard_env():
    "An environment with Lisp (Scheme) standard procedures expressed in Python"
    env = Env()
    env.update(vars(math))
    env.update({
        '+':    lambda *a: sum(a), 
        '-':    op.sub, 
        '*':    op.mul, 
        '/':    op.truediv, 
        '>':    op.gt, 
        '<':    op.lt, 
        '>=':   op.ge, 
        '<=':   op.le, 
        '=':    op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   lambda func, args: func(*args),
        'begin':   lambda *a: a[-1],
        'car':     lambda a: a[0],
        'cdr':     lambda a: a[1:], 
        'cons':    lambda a,b: [a] + b,
        'eq?':     op.is_, 
        'equal?':  op.eq, 
        'empty?':  lambda a: a == [],
        'length':  len, 
        'list':    lambda *a: list(a), 
        'list?':   lambda a: isinstance(a,list), 
        'map':     map,
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'number?': lambda a: isinstance(a, Number),   
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda a: isinstance(a, Symbol)
    })
    return env

class Env(dict):
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer
    def find(self, var):
        return self if (var in self) else self.outer.find(var)


global_env = standard_env()

  
# Lambda

class Lambda:
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args): 
        return eval(self.body, Env(self.parms, args, self.env))


# eval

def eval(x: Expression, env=global_env):
    "Evaluate an expression in an environment."
    if isinstance(x, Number):
        return x
    elif isinstance(x, Boolean):
        return x    
    if isinstance(x, Symbol):      # variable reference
        return env.find(x)[x]
    elif not isinstance(x, List):  # constant literal
        return x
    elif x[0] == 'cond':            # (cond (p1 e1) ... (pn en))
        for (p, e) in x[1:]:
            if eval(p, env): 
                return eval(e, env)                
    elif x[0] == 'quote':          # (quote exp)
        (_, exp) = x
        return exp
    elif x[0] == 'if':             # (if test conseq alt)
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == "define":
        symbol = x[1]
        value = eval(x[2], env=env)
        env[symbol] = value
        return None
    elif x[0] == 'set!':           # (set! var exp)
        (_, var, exp) = x
    elif x[0] == "lambda":
        parameters = x[1]
        value = x[2]
        return Lambda(parameters, value, env=env)
    elif x[0] == "define_func":
        func_and_args = x[1]
        expression = x[2]
        func = func_and_args[0]
        args = func_and_args[1:]
        env[func] = Lambda(args, expression, env=env)
    else:                          # (proc arg...)
        proc = eval(x[0], env)
        args = [eval(exp, env) for exp in x[1:]]
        return proc(*args)
    
    
    
    
