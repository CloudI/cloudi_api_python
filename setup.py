#-*-Mode:python;coding:utf-8;tab-width:4;c-basic-offset:4;indent-tabs-mode:()-*-
# ex: set ft=python fenc=utf-8 sts=4 ts=4 sw=4 et:
from distutils.core import setup, Extension

long_description = open('README.markdown', 'r').read()
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
            optional=True,
        ),
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
    ],
    version='1.7.5',
    description='Python CloudI API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Michael Truog',
    author_email='mjtruog@protonmail.com',
    url='https://cloudi.org',
    install_requires=['erlang_py==1.7.5'],
)
