from distutils.core import setup

setup(
    name = 'python3-coveapi',
    version = '0.2dev',
    packages = ['coveapi', ],
    author = 'Drew Engelson',
    author_email = 'dsengelson@pbs.org',
    url = 'http://github.com/pbs/python-coveapi',
    license = 'GPLv3',
    description = 'A Python3 client for the PBS COVE API service.',
    long_description = 'A Python3 client for the PBS COVE API service.',
    keywords = 'python3 pbs cove video api',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python3',
    ],
)
