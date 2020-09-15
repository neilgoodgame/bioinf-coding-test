import os


def get_env(env_name, is_required=True, default=None):
    """
    Gets a variable from the environment.
    :param env_name: name of the environment variable
    :param is_required: True if the variable is required, False otherwise
    :param default: a default value for the variable
    :return: if the variable is set: the value of the variable
             if the variable is not set and not required: the default value
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


print('all tests pass')
