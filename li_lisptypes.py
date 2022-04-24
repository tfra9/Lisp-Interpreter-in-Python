## Lisp (Scheme) Interpreter in Python
## Lisp types

Symbol = str          # A Lisp Symbol is implemented as a Python str
Number = (int, float) # A Lisp Number is implemented as a Python int or float
String = str
Boolean = bool
List   = list         # A Lisp List is implemented as a Python list
Atom = (Symbol, Number, Boolean, String)
Expression = (list, Atom)
