#!/usr/bin/env python
#
# texttable - module for creating simple ASCII tables
# Copyright (C) 2003-2015 Gerome Fournier <jef(at)foutaise.org>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

DESCRIPTION = "module for trex API"

import sys
from sys import path
from setuptools import setup

if sys.version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

setup(
    name = "trex",
    version = "0.0.1",
    author = "Ramin Najjarbashi", 
    author_email = "Y21GdGFXNHVibUZxWVhKaVlYTm9hVUJuYldGcGJDNWpiMjA9",
    url = "https://github.com/RaminNietzsche/trex",
    license = "GPL-3",
    packages = [
    	"trex", 
    	"trex.client", 
    	"trex.server", 
    	"trex.common", 
    	"trex.console", 
    	"trex.client_utils", 
   ],
    description = DESCRIPTION,
    install_requires=[
        'enum34 >= 1.1.3',
        'jsonrpclib-pelix >= 0.2.6',
        'texttable >= 0.8.4',
        'pyyaml >= 3.11',
        'pyzmq >= 14.0.1',
        'dpkt >= 1.8.7',
    ],
    platforms = "any",
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ]
)
