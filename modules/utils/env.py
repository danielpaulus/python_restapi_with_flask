import os


def get_env_or_default(name, default):
    env = os.environ.get(name)
    if env is None:
        return default
    return env
