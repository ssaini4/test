# -*- coding: utf-8 -
#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.

import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

# read long description
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
    long_description = f.read()

# read dev requirements
fname = os.path.join(os.path.dirname(__file__), 'requirements_test.txt')
with open(fname) as f:
    tests_require = [l.strip() for l in f.readlines()]

class PyTestCommand(TestCommand):
    user_options = [
        ("cov", None, "measure coverage")
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.cov = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests']
        if self.cov:
            self.test_args += ['--cov', 'test']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


install_requires = [
    # We depend on functioning pkg_resources.working_set.add_entry() and
    # pkg_resources.load_entry_point(). These both work as of 3.0 which
    # is the first version to support Python 3.4 which we require as a
    # floor.
    'setuptools>=3.0',
]

setup(
    name='test',

    description='WSGI HTTP Server for UNIX',
    long_description=long_description,
    author='Benoit Chesneau',
    author_email='benoitc@e-engura.com',
    license='MIT',
    url='http://gunicorn.org',

    python_requires='>=3.4',
    install_requires=install_requires,
    zip_safe=False,
    packages=find_packages(exclude=['examples', 'tests']),
    include_package_data=True,

    tests_require=tests_require,
    cmdclass={'test': PyTestCommand},
)