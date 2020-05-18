# TODO: these could use a bit of better error handling
# - style the NameErrors better
# - raise error if there's no __closure__ ?


def replace_closure_variables(func, **kwargs):
    variable_names = func.__code__.co_freevars
    cells = func.__closure__
    for k, v in kwargs.items():
        try:
            pos = variable_names.index(k)
        except ValueError:
            raise NameError(k)
        cells[pos].cell_contents = v


def get_closure_variable(func, name):
    variable_names = func.__code__.co_freevars
    cells = func.__closure__
    for pos, var_name in enumerate(variable_names):
        if var_name == name:
            return cells[pos].cell_contents
    raise NameError(name)

