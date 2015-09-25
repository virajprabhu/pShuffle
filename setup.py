try:
	from setuptools import setup
except ImportError:
	from distutils import setup

config = {
	'description': 'pShuffle is a smart playlist organizer',
	'author': 'Viraj Prabhu',
	'install_requires': ['numpy', 'matplotlib'],
	'packages': ['pShuffle']
	'scripts': []
	'name': ['pShuffle']
}
setup(**config)