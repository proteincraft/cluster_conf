from bash import *
import My_conf
import numpy
import cluster
class My_mol():
    def __init__(self, conformerlist):
        if check_conformers(conformerlist):
            self.conformerfile_list = conformerlist
        else:
            raise IOError
        self.path = '/'.join(conformerlist[0].split('/')[0:-1])
        self.name = '_'.join(conformerlist[0].split('/')[-1].split('_')[0:-1])
        self.conformers = []
        for file in self.conformerfile_list:
            self.conformers.append(My_conf.My_conf(file))

    def cluster(self):
        get_dis_mat(self.conformers)

    def __repr__(self):
        pass

def check_conformers(list):
    for name in list:
#        print(name)
#        print (name[-4:])
        assert(name[-4:] == ".sdf")
        assert('_'.join(list[0].split('_')[0:-1]) == '_'.join(name.split('_')[0:-1]))
    return 1

def get_dis_mat(conformerlist):
    pass