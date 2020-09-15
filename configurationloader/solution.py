"""TODO: module doc..."""

import os


def get_env(env_name, is_required=True, is_bool=False, default=None):
    """
    TODO function doc
    :param env_name:
    :param is_required:
    :param is_bool:
    :param default:
    :return:
    """
    env_val = os.environ.get(env_name)
    is_set = env_val is not None  # To match other is_ vars, for readability and symmetry

    if is_set:
        if is_bool:
            return bool(int(env_val))
        else:
            return env_val
    else:
        if is_required:
            msg = 'Environment missing required key {}'.format(env_name)
            raise ConfigurationException(msg)
        else:
            if default is not None:
                return default
            elif is_bool:
                return False
            else:
                return None
