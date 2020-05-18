from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='stupidity',
    version='0.0.1',
    url='https://github.com/koirikivi/stupidity.git',
    author='Rainer Koirikivi',
    author_email='rainer@koirikivi.fi',
    description='Collection of stupid python modules',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    extras_require={
        'testing': [
            'pytest',
            'pytest-watch',
        ]
    },
    keywords=['stupid', 'stupidity', 'idiocy'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
