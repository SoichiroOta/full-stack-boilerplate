import os

from . import local, testing, staging, production


if os.environ.get('PY_ENV') == 'local':
    config = local.load_config()
else:
    config = dict()
