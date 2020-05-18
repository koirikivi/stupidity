# Inspiration:
# - https://github.com/rfk/withhacks
# - https://code.google.com/archive/p/ouspg/wikis/AnonymousBlocksInPython.wiki
# - https://billmill.org/multi_line_lambdas.html
import functools
import sys
import threading


class StopSwitch(Exception):
    pass


class SkipCase(Exception):
    pass


_switch_lock = threading.Lock()

class case:
    def __init__(self, b, context):
        self.b = b
        self._context = context
        self._trace_func = None
        self._orig_sys_trace = None

    def __enter__(self):
        if not self:
            with _switch_lock:
                orig_trace = self._orig_sys_trace = sys.gettrace()
                if orig_trace is None:
                    self._trace_func = sys.settrace(lambda *a, **kw: None)
                frame = sys._getframe(1)
                frame.f_trace = self._trace_func = self.skip

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is SkipCase:
            if self._trace_func:
                with _switch_lock:
                    sys.settrace(self._orig_sys_trace)

            return True
        elif _is_break_exception(exc_type, exc_value):
            raise StopSwitch

    def skip(self, frame, event, arg):
        raise SkipCase

    def __bool__(self):
        if self._context.found:
            return True
        self._context.found = self._context.a == self.b
        return self._context.found


class switch:
    def __init__(self, a):
        self.a = a
        self.found = False

    def __iter__(self):
        yield functools.partial(case, context=self)

    def __enter__(self):
        return functools.partial(case, context=self)

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is StopSwitch:
            return True
        elif _is_break_exception(exc_type, exc_value):
            return True


def _is_break_exception(exc_type, exc_value):
    return exc_type is NameError and \
        'break' in str(exc_value).lower()


def main():
    print('\nTest 1, for/if:')
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

    print('\nTest 2, for/with:')
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


    print('\nTest 3, with/with:')
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


if  __name__ == '__main__':
    main()
