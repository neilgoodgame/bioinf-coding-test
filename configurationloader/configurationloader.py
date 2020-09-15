from os import environ

def get_env(env_name, is_required=True, is_bool=False, default=None):
    """
    Gets a variable from the environment.
    :param env_name: name of the environment variable
    :param is_required: True if the variable is required, False otherwise
    :param is_bool: True if the variable is a boolean variable (represented by integer values 0 or 1)
    :param default: a default value for the variable
    :return: if the variable is set and not a boolean: the value of the variable
             if the variable is set and a boolean: False for a value of 0 and True otherwise
             if the variable is not set and not required and a default value is specified: the default value
             if the variable is not set and not required and no default value is specified and the variable is boolean: False
             if the variable is not set and not required and no default value is specified and the variable is not boolean: None
    :raises Exception: if the variable is required but not set
    """
    pass
