import os
from os.path import join, dirname
from dotenv import dotenv_values


def load_config():
    dotenv_path = join(
        dirname(__file__),
        'env',
        '.env.{0}'.format(os.getenv('PY_ENV', 'local'))
    )
    return dotenv_values(dotenv_path)
