#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#  Copyright (C) 2014 EDF SA                                                 #
#                                                                            #
#  This file is part of Clara                                                #
#                                                                            #
#  This software is governed by the CeCILL-C license under French law and    #
#  abiding by the rules of distribution of free software. You can use,       #
#  modify and/ or redistribute the software under the terms of the CeCILL-C  #
#  license as circulated by CEA, CNRS and INRIA at the following URL         #
#  "http://www.cecill.info".                                                 #
#                                                                            #
#  As a counterpart to the access to the source code and rights to copy,     #
#  modify and redistribute granted by the license, users are provided only   #
#  with a limited warranty and the software's author, the holder of the      #
#  economic rights, and the successive licensors have only limited           #
#  liability.                                                                #
#                                                                            #
#  In this respect, the user's attention is drawn to the risks associated    #
#  with loading, using, modifying and/or developing or reproducing the       #
#  software by the user in light of its specific status of free software,    #
#  that may mean that it is complicated to manipulate, and that also         #
#  therefore means that it is reserved for developers and experienced        #
#  professionals having in-depth computer knowledge. Users are therefore     #
#  encouraged to load and test the software's suitability as regards their   #
#  requirements in conditions enabling the security of their systems and/or  #
#  data to be ensured and, more generally, to use and operate it in the      #
#  same conditions as regards security.                                      #
#                                                                            #
#  The fact that you are presently reading this means that you have had      #
#  knowledge of the CeCILL-C license and that you accept its terms.          #
#                                                                            #
##############################################################################
"""
Makes torrent images and seeds them via BitTorrent

Usage:
    clara p2p status
    clara p2p restart
    clara p2p -h | --help | help

"""
import time

import docopt
from clara.utils import clush, run, getconfig, value_from_file


def main():
    dargs = docopt.docopt(__doc__)

    trackers = getconfig().get("nodes", "trackers")
    seeders = getconfig().get("nodes", "seeders")

    if dargs['status']:
        clush(trackers, "service mldonkey-server status")
        clush(seeders, "service ctorrent status")
    elif dargs['restart']:
        clush(seeders, "service ctorrent stop")
        clush(trackers, "service mldonkey-server stop")
        time.sleep(1)
        clush(trackers, "service mldonkey-server start")
        clush(seeders, "service ctorrent start")

if __name__ == '__main__':
    main()