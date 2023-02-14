import sys, os

# Ensure this path is writable by the user the WSGI daemon runs as
os.environ['OGD_FLASK_APP_LOG_FILE'] = '/var/log/flask-apps/data-app.log'

if not "/var/www/wsgi-bin" in sys.path:
    sys.path.append("/var/www/wsgi-bin")
from data_app import application