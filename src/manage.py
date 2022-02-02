#!/usr/bin/python3.8
import os
import sys

if __name__ == "__main__":
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    site_packages = os.path.join(PROJECT_ROOT, 'libs')
    if site_packages not in sys.path:
        sys.path.insert(0, site_packages)
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    sys.path.append('..')

    import pymysql
    pymysql.version_info = (1, 3, 13, "final", 0)
    pymysql.install_as_MySQLdb()

    import dotenv
    dotenv.load_dotenv(os.path.join(os.path.dirname(PROJECT_ROOT), '.env'), True)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
