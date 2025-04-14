#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

if __name__ == "__main__":
    # Activate the virtual environment
    activate_env = os.path.join(os.getcwd(), "venv", "Scripts", "activate_this.py")
    if os.path.exists(activate_env):
        with open(activate_env) as f:
            exec(f.read(), {'__file__': activate_env})
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "octofit_tracker.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django or a required module. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment? If the error is related to 'rest_framework', "
            "you can install it by running 'pip install djangorestframework'."
        ) from exc
    execute_from_command_line(sys.argv)