try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Jeff Rankin',
    'url': 'url',
    'download_url': 'download_url',
    'author_email': 'rankin6@llnl.gov',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'project name'
}

setup(**config)