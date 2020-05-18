# stupidity.py - toolkit for stupid Python code

[![Build Status](https://travis-ci.org/koirikivi/stupidity.svg?branch=master)](https://travis-ci.org/koirikivi/stupidity)

## Installation

`pip install stupidity`

## Switch statement

Ever miss the classic switch statement in Python?

```python
from stupidity import switch

for case in switch('b'):
    if case('a'):
        print('this is not printed')
    if case('b'):
        print('this is printed')
    if case('c'):
        print('fallthrough is also supported')
        break
    if case('d'):
        print('this is not printed either')
    print('default value at bottom, but this is not reached')
```

Think `if`-statements are stupid? We've got you covered!

```python
from stupidity import switch

for case in switch('b'):
    with case('a'):
        print('this is not printed')
    with case('b'):
        print('this is printed')
    with case('c'):
        print('fallthrough is also supported')
        break
    with case('d'):
        print('this is not printed either')
    print('default value at bottom, but this is not reached')
```

Think `for`-loops are stupid too? We can get rid of those as well:

```python
from stupidity import switch

with switch('b') as case:
    with case('a'):
        print('this is not printed')
    with case('b'):
        print('this is printed')
    with case('c'):
        print('fallthrough is also supported')
        BREAK  # NOTE: We have to yell here
    with case('d'):
        print('this is not printed either')
    print('default value at bottom, but this is not reached')
```


## Dealing with closure variables

Ever get annoyed at those pesky variables inside closures that are seemingly just outside your reach? Fear no more!

```python
from stupidity import replace_closure_variables

def foo(): 
    x = 42 
    def f(): 
        return x 
    return f 

f = foo()
f()  # 42

replace_closure_variables(f, x=123)
f()  # 123
```

## Braces

Everyone knows that importing `braces` from `__future__` fails miserably:

```python
from __future__ import braces
#   File "<stdin>", line 1
# SyntaxError: not a chance
```

Luckily, we provide a working implementation:

```python
from stupidity import braces

x = 42;
if (x == 123): {
    print('nope')
}
elif (x == 42): {
    print('yep')
}
# prints 'yep'
```
