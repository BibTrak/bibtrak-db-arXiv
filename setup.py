"""bibtrak-db-inSPIRE

Long description goes here...
"""

from datetime import date


#-------------------------------------------------------------------------------
#   GENERAL
#-------------------------------------------------------------------------------
__name__        = "bibtrak_db_arXiv"
__version__     = "0.1.0a1"
__date__        = date(2017, 2, 12)
__keywords__    = [
    "bibliography",
]
__status__      = "Alpha"


#-------------------------------------------------------------------------------
#   URLS
#-------------------------------------------------------------------------------
__url__         = "https://github.com/BibTrak/bibtrak-api"
__download_url__= "https://github.com/BibTrak/bibtrak-api/releases/tag/{version}".format(version=__version__)
__bugtrack_url__= "https://github.com/BibTrak/bibtrak-api/issues"


#-------------------------------------------------------------------------------
#   PEOPLE
#-------------------------------------------------------------------------------
__author_list = [
    "Sharlene Mendez",
    "Brian Sandon",
    "Megan Smith",
    "Daniel Wysocki",
]

__author__      = " and ".join(__author_list)
__author_email__= "daniel.m.wysocki@gmail.com"

__maintainer__      = "Daniel Wysocki"
__maintainer_email__= "daniel.m.wysocki@gmail.com"

__credits__     = __author_list


#-------------------------------------------------------------------------------
#   LEGAL
#-------------------------------------------------------------------------------
__copyright__   = 'Copyright (c) {year} {author} <{email}>'.format(
    year=__date__.year,
    author=__author__,
    email=__author_email__
)

__license__     = 'MIT'
__license_full__= '''
Copyright {year} {author}

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''.format(year=__date__.year, author=__author__).strip()


#-------------------------------------------------------------------------------
#   PACKAGE
#-------------------------------------------------------------------------------
DOCLINES = __doc__.split("\n")

CLASSIFIERS = """
Development Status :: 3 - Alpha
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Operating System :: OS Independent
Intended Audience :: Science/Research
""".strip()

REQUIREMENTS = {
    "install": [
    ],
    "tests": [
    ]
}

ENTRYPOINTS = {
}

from setuptools import setup

metadata = dict(
    name        =__name__,
    version     =__version__,
    description =DOCLINES[0],
    long_description='\n'.join(DOCLINES[2:]),
    keywords    =__keywords__,

    author      =__author__,
    author_email=__author_email__,

    maintainer  =__maintainer__,
    maintainer_email=__maintainer_email__,

    url         =__url__,
    download_url=__download_url__,

    license     =__license__,

    classifiers=[f for f in CLASSIFIERS.split('\n') if f],

    package_dir ={"": "src"},
    packages    =["bibtrak.handlers"],
    namespace_packages = ['bibtrak.handlers'],

    install_requires=REQUIREMENTS["install"],

    entry_points=ENTRYPOINTS
)

setup(**metadata)
