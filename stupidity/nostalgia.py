# TODO
import ast
import inspect
import textwrap


def nostalgia(func):
    # Is there way to parse ast directly from func.__code__ without
    # inspect.getsource()??
    source = textwrap.dedent(inspect.getsource(func))
    source = source.lstrip('@nostalgia')  # err...
    #print(source)
    tree = ast.parse(source)
    tree = NostalgiaTransformer().visit(tree)
    tree = ast.fix_missing_locations(tree)
    print(ast.dump(tree).replace('(', '\n('))
    compiled_module = compile(tree, '<nostalgia>', 'exec')
    locals_ = {}
    exec(compiled_module, globals(), locals_)
    print(compiled_module, locals_)
    return locals_[func.__name__]


class NostalgiaTransformer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        # Replace x / y with x // y if x and y are integers
        if isinstance(node.op, ast.Div) and \
                isinstance(node.left, ast.Num) and \
                isinstance(node.right, ast.Num) and \
                isinstance(node.left.n, int) and \
                isinstance(node.right.n, int):
            node.op = ast.FloorDiv()
        return node


def main():
    @nostalgia
    def foo():
        import sys
        from . import foobar
        x = 3 / 2
        return x

    assert foo() == 1

if __name__ == '__main__':
    main()
