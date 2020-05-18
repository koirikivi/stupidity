from stupidity import braces
from unittest.mock import Mock

def test_braces():
    tester = Mock();
    x = 42;
    if (x == 123): {
        tester('nope')
    }
    elif (x == 42): {
        tester('yep')
    }

    tester.assert_called_once_with('yep');
