#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
""" accède au code dans un autre module par le processus d'importation """

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '')



if __name__ == '__main__':
    main()
