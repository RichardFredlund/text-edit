import math
import string
import os
import pickle

""" functions for loading and saving, files, strings and objects """

def copyfile(fname1,fname2):
    """copy file (fname1,fname2)
       example:
       >> copyfile('example.txt','output.txt')
    """
    fp=open(fname1)

    fout = open(fname2, 'w')

    for line in fp:
        fout.write(line)

    fout.close()

def str_to_file(s,fname):
    """(s,fname) save string s to file fname"""
    fout = open(fname, 'w')

    for line in s:
        fout.write(line)

    fout.close()

def file_to_str(fname):
    """(fname) load file to string """
    fp=open(fname)
    l=[]
    for line in fp:
        l.append(line)
    s=''.join(l)
    return s

def file_to_str_list(fname):
    """ (fname) loads file into list of strings each containing one line"""
    fp=open(fname)
    l=[]
    for line in fp:
        l.append(line)
    return l
        

def obj_to_file(obj,fname):
    """ (obj,fname) pickled obj to file fname"""
    s=pickle.dumps(obj)
    str_to_file(s,fname)

def file_to_obj(fname):
    """ (fname) load pickled obj from fname - returns obj"""
    s=file_to_str(fname)
    obj=pickle.loads(s)
    return obj

def catapillar(fname1,fname2,f):
    """
        same as copyfile but calls
        a function f to process each line
        in some way before saving
        example usage
        catapillar('example1.txt','output.txt',line_strip)
    """
    lsen=[]
    fp=open(fname1)

    fout = open(fname2, 'w')
    ii=0
    for line in fp:
        #if ii==20:
        #    break
        line=f(line)
        if len(line)>1:
            ii+=1
        fout.write(line)
        lsen.append(line)
    fout.close()
    print('number of lines processed:',ii)
    return lsen


def line_strip(line):
    """ strip white space and \n from line in text"""
    return line.strip()

def line_remove_hyphens(line):
    """ replace hyphens with space in line"""
    line=line.replace('-',' ')
    return line










