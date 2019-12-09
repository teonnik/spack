# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyArrow(PythonPackage):
    """Arrow is a Python library that offers a sensible and human-friendly
    approach to creating, manipulating, formatting and converting dates,
    times and timestamps. It implements and updates the datetime type,
    plugging gaps in functionality and providing an intelligent module API
    that supports many common creation scenarios. Simply put, it helps you
    work with dates and times with fewer imports and a lot less code."""

    homepage = "https://arrow.readthedocs.io/en/latest/"
    url      = "https://pypi.io/packages/source/a/arrow/arrow-0.14.7.tar.gz"

    version('0.14.7', sha256='67f8be7c0cf420424bc62d8d7dc40b44e4bb2f7b515f9cc2954fb36e35797656')

    depends_on('python@2.7:2.8,3.5:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-backports-functools-lru-cache@1.2.1:', type=('build', 'run'), when='^python@2.7:2.8')
    depends_on('py-python-dateutil', type=('build', 'run'))
    depends_on('py-chai', type='test')
    depends_on('py-mock', type='test')
    depends_on('py-pytz@2019.0:', type='test')
