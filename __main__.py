#!/usr/bin/python3

import importlib
import os
import sys

cmd = [i[:-3] for i in os.listdir(__file__.rsplit('/',maxsplit = 1)[0]+'/lib') if i[-3:] == ".py"]

if len(sys.argv)<2 or sys.argv[1] not in cmd:
    sys.exit("""Brownie 0.0.1 - python based development framework for Ethereum
    
Usage:  brownie <command> [options]

Commands:
  deploy   Run a script in the /deployments folder
  init     Initialize a new brownie project
  test     Run test scripts in the /tests folder
  
Type brownie <command> --help for more information about a specific command.""")



importlib.import_module("lib."+sys.argv[1])
#if ('lib.components.network' in sys.modules and
#    sys.modules['lib.components.network'].rpc):
#    sys.modules['lib.components.network'].rpc.terminate()

    