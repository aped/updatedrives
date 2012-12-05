#! /usr/bin/env python

""" 
    Re-write of a drive-updating tool
    hacked together by Andrew Pedelty

    Throw it in somewhere from $PATH and 
    chmod +x, remove .py for fun and easy
    drive updating when testing or 
    swapping lots of drives on a machine.
"""

import os, sys


def test_root(): 
    """
    Makes sure we're runinng as root. 
    """
    if not os.getuid() == 0: 
        sys.exit("This script needs to be run as root.")


def test_drives(): 
    """ 
    Sends test signal to each scsi scan file.
    """
    basepath = "/sys/class/scsi_host"
    abslist = [os.path.join(basepath, hostn, 'scan') 
               for hostn in os.listdir(basepath)]
    for scanfile in abslist: 
        print "Updating scanfile %s." % scanfile
        with open(scanfile, 'w') as fh: 
            fh.write("0 0 0")
            fh.flush()
            fh.write("- - -")


if __name__ == "__main__": 
    print "Updating drives!"
    test_root()
    test_drives()
