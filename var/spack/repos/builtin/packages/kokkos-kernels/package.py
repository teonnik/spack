# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class KokkosKernels(MakefilePackage):
    """Kokkos C++ Performance Portability Programming EcoSystem: Math Kernels -
    Provides BLAS, Sparse BLAS and Graph Kernels."""

    homepage = "https://github.com/kokkos/kokkos-kernels"
    url      = "https://github.com/kokkos/kokkos-kernels/archive/2.7.00.tar.gz"

    version('2.9.00', sha256='dafa9ebcdbcdc95641a986a80fcd3e532f1d80692c80a51cb08182c02c1added')
    version('2.8.00', sha256='c9648dbf5b9cbddf2aa72f6d214a2c40e23e51660f903b83743617251574fe06')
    version('2.7.00', sha256='adf4af44eadbdfbeb9ec69dd5fae4e2852bd1fbe4a69213efd199e49f4098254')
    version('2.6.00', sha256='14ebf806f66b9ca73949a478b8d959be7fa1165a640935760a724d7cc0a66335')
    version('2.5.00', sha256='2c2289da3a41dafd97726e90507debafbb9f5e49ca5b0f5c8d1e044a5796f000')
    version('develop', git='https://github.com/kokkos/kokkos-kernels',
            branch='develop')

    # make sure kokkos kernels version matches kokkos
    depends_on('kokkos@2.5.00', when='@2.5.00')
    depends_on('kokkos@2.6.00', when='@2.6.00')
    depends_on('kokkos@2.7.00', when='@2.7.00')
    depends_on('kokkos@develop', when='@develop')
    depends_on('kokkos@2.8.00', when='@2.8.00')
    depends_on('kokkos@2.9.00', when='@2.9.00')

    patch('makefile.patch')

    def edit(self, spec, prefix):
        makefile = FileFilter("src/Makefile")
        makefile.filter('CXX = .*', 'CXX = ' + env['CXX'])

    def build(self, spec, prefix):
        with working_dir('build', create=True):
            makefile_path = '%s%s' % (self.stage.source_path, '/src/Makefile')
            copy(makefile_path, 'Makefile')
            make_args = [
                'KOKKOSKERNELS_INSTALL_PATH=%s' % prefix,
                'KOKKOSKERNELS_PATH=%s' % self.stage.source_path,
                'KOKKOS_PATH=%s' % spec['kokkos'].prefix
            ]

            make('build', *make_args)

    def install(self, spec, prefix):
        with working_dir('build', create=False):
            make_args = [
                'KOKKOSKERNELS_INSTALL_PATH=%s' % prefix,
                'KOKKOSKERNELS_PATH=%s' % self.stage.source_path,
                'KOKKOS_PATH=%s' % spec['kokkos'].prefix
            ]
            make('install', *make_args)
