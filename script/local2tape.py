#!/usr/bin/env python3
#
# G. Mazzitelli 2022
# versione DAQ LNGS/LNF per midas file2cloud 
# cheker and sql update Nov 22 
#

def main(verbose):
    #

    import os,sys

    import numpy as np
    import cygno as cy
    import time
    import subprocess

    script_path = os.path.dirname(os.path.realpath(__file__))
    start = end = time.time()
    tmp_token = '/tmp/tapetoken'
    in_dir = '/root/data/'
    out_tape = 'prova2/' # da aggiornare per quax
    tape_path = 'davs://xfer-archive.cr.cnaf.infn.it:8443/cygno/' # mettere quax
    files=os.listdir(in_dir)
    nfile = len(files)
    print("Numebr of files", nfile)
    
    for i, file in enumerate(files):
        if (not file.startswith('.')):
            if (end-start)>3000 or (start-end)==0:
                output = subprocess.check_output("source "+script_path+"/oicd-setup.sh > "+tmp_token, shell=True)
                with open(tmp_token) as f:
                    lines = [line.rstrip() for line in f]
                os.environ["BEARER_TOKEN"] = lines[1]
                if (verbose): print(lines[1])
                start = time.time()
            end = time.time()
            print (">>> coping file: "+file)
            if verbose: print("gfal-copy "+in_dir+file+" "+tape_path+out_tape+file)
            tape_data_copy = subprocess.check_output("gfal-copy "+in_dir+file+" "+tape_path+out_tape+file, shell=True)
            print ("File ", file, " ok")


    exit(0)
    
    
if __name__ == "__main__":
    from optparse import OptionParser
    #
    # deault parser value
    #

    parser = OptionParser(usage='usage: %prog n')
    parser.add_option('-v','--verbose', dest='verbose', action="store_true", default=False, help='verbose output')
    (options, args) = parser.parse_args()
    if options.verbose: 
        print ("options", options)
        print ("args", args)
     
    main(options.verbose)
