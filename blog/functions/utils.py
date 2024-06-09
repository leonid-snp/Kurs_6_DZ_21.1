import environ


def get_db_login(keys):
    env = environ.Env()
    environ.Env.read_env()
    return env(keys)
