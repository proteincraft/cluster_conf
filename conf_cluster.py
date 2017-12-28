#!/home/wei/anaconda3/bin/python
import sys
import os
import arg_parser
import My_mol

def main():
    args = arg_parser.get_args(sys.argv)
    mol = My_mol.My_mol(args.Mol_list)

if __name__ == "__main__":
    main()
