## Lisp (Scheme) Interpreter in Python
## Tests


from unittest import TestCase
from li_parser import normalize_string, parse, generate_ast
from li_interpreter import eval, standard_env

class Test(TestCase):

    def setUp(self):
        self.test_string =  "(+ 1 5)"

    def test_normalize_string(self):

        string = "(+ 1 5)"
        answer = ["(", "+", "1", "5", ")"]
        self.assertEqual(normalize_string(string), answer)

        string = " ( + 1 5 ) "
        self.assertEqual(normalize_string(string), answer)


    def general_tests(self):

        def test_expr(expr, expected_val):
            env = standard_env()
            self.assertEqual(eval(parse(expr), env), expected_val)

        # test - basic operations

        test_expr("2", 2)
        test_expr("1.123", 1.234)
        test_expr("#f", False)
        test_expr("#t", True)

        test_expr("(+ 1 7)", 8)
        test_expr("(- 3.5 1.5)", 2.0)
        test_expr("(/ 3 2)", 1.5)
        test_expr("(// 3 2)", 1)

        test_expr("(if #t 3 1)", 3)
        test_expr("(if #f 3 1)", 1)
        test_expr("(if (> 3 2) 3 2)", 3)

        test_expr("(begin 2 3 5)", 5)

        test_expr("(quote (define x 2))", ["define",  "x", 2])

        test_expr("(list 1 2 3)", [1, 2, 3])
        test_expr("(list #f 2 3.14)", [False, 2, 3.14])
        test_expr("(car (list 1 2))", 1)
        test_expr("(cdr (list 1 2 3))", [2, 3])
        test_expr("(cdr (list 1))", [])
        test_expr("(empty? (list))", True)
        test_expr("(empty? (list 1))", False)

        test_expr("(quote (list 2))", ['list', 2])

        test_expr("(begin (define x 7) x)", 7)
        test_expr("(begin (define x 3) (set! x 5) x)", 5)

        test_expr("(define_func (f x) (+ x 3))", None)
        test_expr("(begin (define_func (f x) (+ x 2)) (f 7))", 9)

        # test - recursive factorial
        test_expr("(begin (define_func (fact n) (if (<= n 1) 1 (* n (fact (- n 1))))) (fact 8))", 40320)


    def test_eval(self):
        env = standard_env()
        self.assertEqual(eval(parse(self.test_string), env), 6)
