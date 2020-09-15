import os


def get_env(env_name, is_required=True, default=None, is_bool=False):
    """
    Gets a variable from the environment.
    :param env_name: name of the environment variable
    :param is_required: True if the variable is required, False otherwise
    :param is_bool: True if the variable is a boolean variable
                    (represented by integer values 0 or 1)
    :param default: a default value for the variable
    :return: if the variable is set and not is_bool: the value of the variable
             if the variable is set and is_bool: False for a value of 0 and True for a value of 1
             if the variable is not set and not required: the default value
             if the variable is not set and not required and no default value is specified and is_bool: False
             if the variable is not set and not required and no default value is specified and not is_bool: None
    :raises Exception: if the variable is required but not set
    """
    pass


# TESTS

os.environ['USERNAME'] = 'sam'

assert get_env('USERNAME') == 'sam'
assert get_env('USERNAME', is_required=False) == 'sam'
assert get_env('DOES_NOT_EXIST', is_required=False) is None
assert get_env('DOES_NOT_EXIST', is_required=False, default='default_value') == 'default_value'
assert get_env('DOES_NOT_EXIST', is_required=False, default=False) is False

try:
    get_env('DOES_NOT_EXIST', is_required=True)
except BaseException as e:
    pass
else:
    raise AssertionError('get_env should have raised an exception')

try:
    get_env('DOES_NOT_EXIST', is_required=True, default='shouldnt_matter')
except BaseException as e:
    pass
else:
    raise AssertionError('get_env should have raised an exception')

os.environ['ZERO'] = '0'
os.environ['ONE'] = '1'

assert get_env('ZERO', is_bool=True) is False
assert get_env('ZERO', is_bool=False) == '0'
assert get_env('ZERO', is_bool=True, is_required=True) is False
assert get_env('ZERO', is_bool=True, is_required=True, default=True) is False


assert get_env('ONE', is_bool=True) is True
assert get_env('ONE', is_bool=False) == '1'
assert get_env('ONE', is_bool=True, is_required=True) is True
assert get_env('ONE', is_bool=True, is_required=True, default=False) is True

assert get_env('DOES_NOT_EXIST', is_bool=True, is_required=False) is False
assert get_env('DOES_NOT_EXIST', is_bool=True, is_required=False, default=True) is True

os.environ['EMPTY'] = ''
assert get_env('EMPTY', is_required=True, default='some_value') == ''

print('all tests pass')
