#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
# if sys.version_info.major!=3 or sys.version_info.minor!=10:
#     raise RuntimeError(f"this app requires python 3.10 exactly, but you have {sys.version_info}")
if sys.version_info.major!=3 or sys.version_info.minor!=11:
    raise RuntimeError(f"this app requires python 3.11 exactly, but you have {sys.version_info}")

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'halo.settings.dev')
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
