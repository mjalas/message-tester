from setuptools import setup, find_packages
from codecs import open
from os import path
import test_messaging.metadata as metadata

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
# TODO: Currently not working because of markdown to reStructuredText conversion not added.
long_description = ""
if path.exists(path.join(here, 'README.rst')):
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name=metadata.NAME,
    version=metadata.VERSION,
    description=metadata.DESCRIPTION,
    long_description=long_description,
    url=metadata.URL,
    author=metadata.AUTHOR,
    author_email=metadata.AUTHOR_EMAIL,
    license=metadata.LICENSE,
    keywords=metadata.KEYWORDS,
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    data_files=[('scenarios', ['scenarios/test.json'])],
    entry_points={
        'console_scripts': [
            'test-messaging=__main__:main',
        ],
    },
)
