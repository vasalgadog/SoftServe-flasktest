from dotenv import load_dotenv
import os

load_dotenv()

bind = os.environ.get('GUNICORN_HOST') + ':' + os.environ.get('GUNICORN_PORT')
workers = os.environ.get('GUNICORN_WORKERS')
threads = os.environ.get('GUNICORN_THREADS')
timeout = os.environ.get('GUNICORN_TIMEOUT')
loglevel = os.environ.get('GUNICORN_LOGLEVEL')