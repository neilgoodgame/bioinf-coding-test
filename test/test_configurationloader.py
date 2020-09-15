"""TODO: module doc..."""

from os import environ
import pytest
from configurationloader.configurationloader import get_env


# pylint: disable=invalid-name


def helper(is_required, is_bool, expected_value, set_in_env, default=None):
    """
    TODO function doc
    :param is_required:
    :param is_bool:
    :param expected_value:
    :param set_in_env:
    :param default:
    """
    if set_in_env:
        if isinstance(expected_value, bool):
            env_value = '1' if expected_value else '0'
        else:
            env_value = expected_value
        environ['ENV_VAR'] = env_value
    assert get_env('ENV_VAR', is_required=is_required,
                   is_bool=is_bool, default=default) == expected_value
    environ.pop('ENV_VAR', None)


def helpex(is_required, is_bool, expected_value, set_in_env):
    """
    TODO function doc
    :param is_required:
    :param is_bool:
    :param expected_value:
    :param set_in_env:
    """
    with pytest.raises(Exception) as excinfo:
        helper(is_required, is_bool, expected_value, set_in_env)


def helpdf(expected_value):
    """
    help default. if we're setting a default there's pretty much one pattern to the method call
    :param expected_value:
    """
    helper(is_required=False, is_bool=False, set_in_env=False, expected_value=expected_value,
           default=expected_value)


def test_is_required_notbool_set():
    """
    Test required non-bool env vars
    """
    helper(is_required=True, is_bool=False, set_in_env=True, expected_value='server_name')


def test_is_required_notbool_notset():
    """
    TODO function doc
    """
    helpex(is_required=True, is_bool=False, set_in_env=False, expected_value='WHAT')


def test_is_required_bool_set():
    """
    Test required bool env vars
    """
    helper(is_required=True, is_bool=True, set_in_env=True, expected_value=True)


def test_is_required_bool_notset():
    """
    TODO function doc
    """
    helpex(is_required=True, is_bool=True, set_in_env=False, expected_value=True)


def test_not_required_notbool_set():
    """
    Test optional non-bool env vars
    """
    helper(is_required=False, is_bool=False, set_in_env=True, expected_value='server_name')


def test_not_required_notbool_notset():
    """
    TODO function doc
    """
    helper(is_required=False, is_bool=False, set_in_env=False, expected_value=None)


def test_not_required_notbool_default():
    """
    TODO function doc
    """
    helpdf('1')


def test_not_required_bool_set():
    """
    Test optional bool env vars
    """
    helper(is_required=False, is_bool=True, set_in_env=True, expected_value=True)


def test_not_required_bool_notset():
    """
    TODO function doc
    """
    helper(is_required=False, is_bool=True, set_in_env=False, expected_value=False)


def test_not_required_bool_default():
    """
    TODO function doc
    """
    helper(is_required=False, is_bool=True, set_in_env=False, expected_value=True, default=True)


def test_is_required_bool_looking_vals_are_not_converted_1():
    """
    Test that things that look like bools aren't converted when they are not explicitly set to be
    bools
    """
    helper(is_required=True, is_bool=False, set_in_env=True, expected_value='1')


def test_is_required_bool_looking_vals_are_not_converted_0():
    """
    TODO function doc
    """
    helper(is_required=True, is_bool=False, set_in_env=True, expected_value='0')


def test_not_required_default_bool_looking_vals_are_not_converted_3():
    """
    TODO function doc
    """
    helpdf('1')


def test_not_required_default_bool_looking_vals_are_not_converted_4():
    """
    TODO function doc
    """
    helpdf('0')
