#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path

def ensure_media_profile_dir():
    media_profile_path = Path(__file__).resolve().parent / 'media' / 'profile'
    media_profile_path.mkdir(parents=True, exist_ok=True)

def main():
    """Run administrative tasks."""
    ensure_media_profile_dir()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth.settings')  # Replace 'auth' with your real project folder
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
