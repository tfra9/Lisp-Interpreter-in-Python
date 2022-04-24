# Lisp-Interpreter-in-Python
Small Lisp (Scheme) Interpreter in Python

This is an implementation of Lisp interpreter (specifically a subset of Scheme dialect) written in Python.

## Files

The repository contains the following files:

`li_interpreter.py`: Interpreter main part with `eval` definition, 

`li_parser.py`: Lisp parser for converting input character string to list of tokens and then into an abstract syntax tree,

`li_lisptypes.py`: List of Lisp types definitions,

`li_tests.py`: Basic tests.


## Features

### Supported types :

integers, floats, booleans.

### Supported Lisp operators :

Seven Primitive Operators:
- `quote`
- `symbol?` (`atom`)
- `eq?`
- `car`
- `cdr`
- `cons`
- `cond`

Other Operators:
- `define`
- `lambda`
- `set!`
- `(define_func (f x) (expr))` : shortcut to `(define f (lambda (x) (expr)))`


## Turing Completeness issue


From the ["LISP 1.5 Programmers Manual"](http://www.softwarepreservation.org/projects/LISP/book/LISP%201.5%20Programmers%20Manual.pdf) article by the Lisp authors it follows that it is enough to use the **Seven Primitive Operators** mentioned above to define the function `eval` (formula on page 13), a function that takes as an argument any Lisp expression and returns its value - in consequence, using it we can define any additional function we want.

Adding to the above:
- lambda function,
and basic elements:
- symbol-evaluation,
- function-dispatch,
- function read,
- function write.

we get the set provided Turing Completeness.


### postscript

In the literature I have read (but not studied details) that there is a more advanced path to proving the Lisp language is Turing Complete - based on the lambda calculus (which is Turing Complete). Based on the lambda calculus, it can be shown that set is sufficient:

- lambda function,
- variable references,
- function calls.

