import sys
import os
import argparse

def get_args(arg_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('--Mol_list', nargs='+', help='list of sdf file to cluster.')
    parser.add_argument('--cutoff', nargs='+', help='cutoff for clustering.')
    args = parser.parse_args()
    return args
