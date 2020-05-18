from stupidity import replace_closure_variables

def test_replace_closure_variables():
    def foo():
        x = 42
        def f():
            return x
        return f
    f = foo()
    f()  # 42

    replace_closure_variables(f, x=200)
    f()  # 200
    replace_closure_variables(f, x=123)
    f()  # 123
