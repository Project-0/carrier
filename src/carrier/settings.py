# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'mongo'
MONGO_PORT = 27017

# Skip this block if your db has no auth. But it really should.
MONGO_USERNAME = 'root'
MONGO_PASSWORD = 'example'
# Name of the database on which the user can be authenticated,
# needed if --auth mode is enabled.
MONGO_AUTH_SOURCE = 'admin'

MONGO_DBNAME = 'carrier'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

import importlib.util
spec = importlib.util.spec_from_file_location("templates", "./templates/__init__.py")
templates = importlib.util.module_from_spec(spec)
spec.loader.exec_module(templates)

DOMAIN = templates.DOMAINS

# TODO: import *.py files from env.getstr(IMPORT_PATH) + templates/ and add
# them to the settings collection
"""
template_dict = get_template_parameters()
settings = settings.update(template_dict)
"""