import subprocess
import sys

def bash(cmd, cwd='.'):
    popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, cwd=cwd)
    print ("waiting for", cmd)
    return popen.stdout.read()
