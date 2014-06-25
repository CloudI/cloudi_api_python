#-*-Mode:python;coding:utf-8;tab-width:4;c-basic-offset:4;indent-tabs-mode:()-*-
# ex: set ft=python fenc=utf-8 sts=4 ts=4 sw=4 et:
import setuptools
from distutils.core import setup, Command, Extension

class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import sys, pkgutil
        directory = 'test'
        for importer, package_name, _ in pkgutil.iter_modules([directory]):
            full_package_name = '%s.%s' % (directory, package_name)
            if full_package_name not in sys.modules:
                importer.find_module(package_name
                ).load_module(full_package_name)

setup(
    name='cloudi',
    py_modules=['cloudi', 'cloudi_c'],
    ext_modules=[
        Extension(
            name='libcloudi_py',
            sources=[
                'cloudi_py.cpp',
                'assert.cpp',
                'timer.cpp',
                'cloudi.cpp',
            ],
            depends=[
                'config.h',
                'assert.hpp',
                'copy_ptr.hpp',
                'realloc_ptr.hpp',
                'timer.hpp',
                'cloudi.h',
                'cloudi.hpp',
            ],
            libraries=[
                'ei',
                'rt',
                'stdc++',
            ],
            # cloudi.py can be used if this compilation fails
            # (Python 3 doesn't work yet due to all the changes)
            optional=True,
        ),
    ],
    cmdclass = {'test': PyTest},
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
    ],
    version='1.3.2',
    description='Python CloudI API',
    author='Michael Truog',
    author_email='mjtruog@gmail.com',
    url='http://cloudi.org',
    install_requires=['erlang_py==1.3.2'],
)
