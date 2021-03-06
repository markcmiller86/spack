##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class Libbson(AutotoolsPackage):
    """libbson is a library providing useful routines related to building,
    parsing, and iterating BSON documents."""

    homepage = "https://github.com/mongodb/libbson"
    url      = "https://github.com/mongodb/libbson/releases/download/1.6.3/libbson-1.6.3.tar.gz"

    version('1.6.3', 'b7bdb314197106fcfb4af105a582d343')
    version('1.6.2', 'c128a2ae3e35295e1176465be60f19db')
    version('1.6.1', '4d6779451bc5764a7d4982c01e7bd8c2')

    depends_on('autoconf', type='build', when='@1.6.1')
    depends_on('automake', type='build', when='@1.6.1')
    depends_on('libtool', type='build', when='@1.6.1')
    depends_on('m4', type='build', when='@1.6.1')

    @property
    def force_autoreconf(self):
        # 1.6.1 tarball is broken
        return self.spec.satisfies('@1.6.1')
