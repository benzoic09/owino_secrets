import sys
import os
import site

# Add your virtualenv site-packages
site.addsitedir('/home/owinosec/virtualenv/owino_secrets/3.10/lib/python3.10/site-packages')

# Add your project path
sys.path.insert(0, '/home/owinosec/owino_secrets')

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'owino_secrets.settings')

from django.core.management import execute_from_command_line

# Run tasks
execute_from_command_line(['manage.py', 'migrate'])
execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])