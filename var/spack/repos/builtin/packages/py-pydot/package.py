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


class PyPydot(PythonPackage):
    """Python interface to Graphviz's Dot language"""

    homepage = "https://github.com/erocarrera/pydot/"
    url      = "https://pypi.io/packages/source/p/pydot/pydot-1.2.3.tar.gz"

    version('1.2.3', '5b50fd8cf022811d8718562ebc8aefb2')
    version('1.2.2', 'fad67d9798dbb33bb3dca3e6d4c47665')

    depends_on('py-setuptools', type='build')
    depends_on('py-pyparsing@2.1.4:', type=('build', 'run'))
    depends_on('graphviz', type=('build', 'run'))
