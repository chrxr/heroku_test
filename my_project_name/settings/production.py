from .base import *


DEBUG = False
TEMPLATE_DEBUG = False

env = os.environ.copy()

SECRET_KEY = env['SECRET_KEY']

try:
    from .local import *
except ImportError:
    pass
