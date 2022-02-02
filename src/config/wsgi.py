"""
WSGI config for example project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys

project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
parent_dir = os.path.dirname(project_root)
site_packages = os.path.join(project_root, 'libs')

if project_root not in sys.path:
    sys.path.insert(0, project_root)

if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

if site_packages not in sys.path:
    sys.path.insert(0, site_packages)

import pymysql
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()

import dotenv
dotenv.load_dotenv(os.path.join(os.path.dirname(project_root), '.env'), True)

from django.core.wsgi import get_wsgi_application

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "example.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
