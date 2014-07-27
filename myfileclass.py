import os,re,copy,sys

class myfile(object):
    """ Main methods are
        myfile().gf() -- user query menu to get file path
        myfile().gd() -- user query menu to get directory
        myfile().get_save_path() -- which also queries user for filename
    """

    def gf(self,filepath=''):
        """ same as --- get_file_path  """ 
        return self.get_file_path(filepath)

    def gd(self,filedir=''):
        """ same as --- get_directory """ 
        return self.get_directory(filedir)

    def inp(self):
        """ user select directory to add to system path
            use before import from a given folder """
        sys.path.insert(0,self.gd())

    def mui(self):
        """ mui - MAGIC USER IMPORT
            user selects file to import
            is added to syspath and imports"""
        userfile=self.gf()
        userdir=self.file__root(userfile)
        fname=self.file__name(userfile)
        print 'import ' + fname.split('.')[0]
        sys.path.insert(0,userdir)
        

    def __reg__find_last(self,v,s):
        """ find last v in string s
            ...............................................
            find span of last instance of string v in string s
            if v not in s, returns false"""
        inds=[e.span() for e in re.finditer(v,s)]
              
        try:
              return inds[-1]
        except:
              return False


    """ print functions """
    def __print__lines(self,l):
        """ for line in l: print line """
        for line in l:
            print line

    def __print__enumerate(self,x,c=0):
        """ for n,f in enumerate(x): print n,f """
        for n,fl in enumerate(x):
            print n+c,fl

    def __file__upper(self,dir):
        """ returns parent directory or False"""
        sp=self.__reg__find_last(r'\\',dir)
        if sp:
            return dir[:sp[0]]
        else:
            return False

    def __file__rfp(self,dir):
        """ returns list of relative folder paths """
        return [x[0][len(dir):] for x in os.walk(dir)]  

    def file__InFolder(self,dir=[]):
        """ given directory dir return list
            of files and folders:
            output[0] is a list of files
            output[1] is a list of folders"""
        if dir==[]:
            dir=os.getcwd()
            
        bag=[[],[]]
        for name in os.listdir(dir):
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                bag[0].append(name)
            else:
                bag[1].append(name)
        return bag

    def walk_directory(self,dir=[]):
        """ returns file name and path for all files
            and sub directories in dir
            returns list of (name,path)"""
        
        if dir==[]:
            dir=os.getcwd()
        
        pathlist=[]
        for name in os.listdir(dir):
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                pathlist.append((name,path))
            else:
                branch=self.walk_directory(path)
                pathlist.extend(self.walk_directory(path))
                if branch==[]:
                    # add path of empty folders
                    pathlist.append(('',path))
        return pathlist  

    def file__name(self,filepath):
        """ gives file name for a given file path"""
        return filepath.split('\\')[-1]

    def file__root(self,filepath):
        """ for a file path this returns directory path
            for a directory this returns parent directory path"""
        return ('\\').join(filepath.split('\\')[:-1])

    def __list__sortInDessendingOrderOfLength(self,lst):
        """ given a list sorts list in dessending order of length""" 
        jj=[(len(ii),ii) for ii in lst]
        jj.sort()
        jj.reverse()
        kk=[ii[1] for ii in jj]
        return kk


    def file__Structure(self,dir=[]):
        """ list of subdirectories and files in them
            returns a list of tuples (a,b)
            a -- subdirectory
            b -- list of filenames"""

        if dir==[]:
            dir=os.getcwd()
            
        p2=[ii[1] for ii in self.walk_directory(dir)]
        k=self.__list__sortInDessendingOrderOfLength([dir+ii for ii in self.__file__rfp(dir)])
        k1=self.__list__sortInDessendingOrderOfLength([ii for ii in self.__file__rfp(dir)])
        bag=[[] for ii in range(len(k))]
        cp=copy.copy(p2)
        for n,ii in enumerate(k):
            for m,jj in enumerate(cp):
                if ii in jj:
                    val=jj[len(k[n])+1:]
                    if val!='':
                        bag[n].append(jj[len(k[n])+1:])
                    cp.pop(m)
        """ return list structure: ([(subdirectory,[file1,file2,..]),...])"""
        return [(k1[n],bag[n]) for n in range(len(k))]
     
    def __file__printFolderContent(self,dir):
        pathlist=walk_directory(dir)
        print '.....................'
        print 'Directory Name:'
        print dir
        print '.....................'
        B=file__Structure(dir)
        B.reverse()
        # print all files with their subfolders
        for n,ii in enumerate(B):
            for jj in ii[1]:
                if B[n][0]!='':
                    print B[n][0]+'\\'+jj
                else:
                    print jj

        # print empty folders at the end:
        for n,ii in enumerate(B):
            if ii[1]==[]:
                print B[n][0]+'\\'    
        print '.....................'


    def __user__getInput(self,inps,opt=['xx','bb']):
        """ inps is a list of accepted input strings
            by default opt  reserves: 
            'xx'-exit 'bb'-back
            xx- return 0
            bb returns 1
            all other returns are strings"""
        try:
            v=raw_input()
            if v in opt: return opt.index(v)
            elif v in inps:
                return v
            else:
                print 'please type value on list:\n'
                return __user__getInput(inps)
        except:
            __user__getInput(inps)

    def _remove_pyc_file_from_bag(self,bag):
        """ returns bag with .pyc files removed """
        return [[ii for ii in bag[0] if ii[-4:]!='.pyc'],bag[1]]

            
    def __user__fileMenu(self,dir=os.getcwd()):
        """ user file menu.""" 
        bag=self.file__InFolder(dir) # bag[0] is files, bag[1] is subfolders
        bag=self._remove_pyc_file_from_bag(bag)
        vals=[(str(n),ii) for n,ii in enumerate(bag[0]+bag[1])]
        v1=[ii[0] for ii in vals]
        print 'type \'xx\'-exit'
        print '.....................'
        print 'Directory Name:'
        print dir
        print '.....................'
        print 'files'
        print '.....................'
        self.__print__enumerate(bag[0])
        print '.....................'
        print 'folders'
        print '.....................'    
        self.__print__enumerate(bag[1],len(bag[0]))
        print '.....................'
        print '\'u\' up one file level'
        print '.....................'

        inps=v1+['u']
        x=self.__user__getInput(inps)

        if x=='u':
            # go up one level in directories
            return self.__user__fileMenu(self.__file__upper(dir))
        elif x in v1:
            if int(x)<len(bag[0]):
                # this is a file so return file path
                return os.path.join(dir,vals[int(x)][1])
            else:
                # these are sub folders.
                return self.__user__fileMenu(os.path.join(dir,vals[int(x)][1]))
        elif x in [0,1]:
            return x
        else:
            print 'error in fileMenu'

    def __user__directoryMenu(self,dir=os.getcwd()):
        bag=self.file__InFolder(dir) # bag[0] is files, bag[1] is subfolders
        bag=self._remove_pyc_file_from_bag(bag)
        vals=[(str(n),ii) for n,ii in enumerate(bag[1])]
        v1=[ii[0] for ii in vals]
        print 'type \'xx\'-exit \'bb\' - back'
        print '.....................'
        print 'Directory Name:'
        print dir
        print '.....................'
        print 'files'
        print '.....................'
        for item in bag[0]: print item,
        print '.....................'
        print 'folders'
        print '.....................'
        if len(bag[1])<1:
            print 'empty'
        self.__print__enumerate(bag[1])
        print '.....................'
        print '\'u\' up one file level'
        print '\'d\' return directory path'
        print '.....................'

        inps=v1+['u','d']
        x=self.__user__getInput(inps)

        if x=='u':
            # go up one level in directories
            return self.__user__directoryMenu(self.__file__upper(dir))
        elif x=='d':
            return dir # return directory path
        elif x in v1:
            # these are sub folders.
            return self.__user__directoryMenu(os.path.join(dir,vals[int(x)][1]))
        elif x in [0,1]:
            return x
        else:
            print 'error in __user__directoryMenu'


    def __user__fileandfolderMenu(self,dir=os.getcwd()):
        bag=self.file__InFolder(dir) # bag[0] is files, bag[1] is subfolders
        bag=_remove_pyc_file_from_bag(bag)
        vals=[(str(n),ii) for n,ii in enumerate(bag[0]+bag[1])]
        v1=[ii[0] for ii in vals]
        print 'type \'xx\'-exit \'bb\' - back'
        print '.....................'
        print 'Directory Name:'
        print dir
        print '.....................'
        print 'files'
        print '.....................'
        __print__enumerate(bag[0])
        print '.....................'
        print 'folders'
        print '.....................'    
        __print__enumerate(bag[1],len(bag[0]))
        print '.....................'
        print '\'u\' up one file level'
        print '\'d\' return directory path'
        print '.....................'

        inps=v1+['u','d']
        x=__user__getInput(inps)

        if x=='u':
            # go up one level in directories
            return __user__fileMenu(__file__upper(dir))
        elif x=='d':
            return dir # return directory path
        elif x in v1:
            if int(x)<len(bag[0]):
                # this is a file so return file path
                return os.path.join(dir,vals[int(x)][1])
            else:
                # these are sub folders.
                return __user__fileMenu(os.path.join(dir,vals[int(x)][1]))
        elif x in [0,1]:
            return x
        else:
            print 'error in fileMenu'

    ## --- note new version in tools3 which doesn't have xx,bb
    def get_file_path(self,filepath=''):
        """ menus if no file is given:

            -- if no filepath is given a file menu is called
            -- if only the file name but no directory is given
            -- -- user query --
            --    save in current directory 'y' or 'n'
            -- (also display current directory)

            -- if 'y' --- save in os.getcwd()
            -- if 'n' --- go to file menu to get directory
        """
        if filepath=='':
            filepath=self.__user__fileMenu(dir=os.getcwd())
        elif '\\' not in filepath:
            # only file name has been given
            print 'in current directory \'y\' or \'n\''
            inp=raw_input()
            if inp=='y':
                filepath=os.getcwd()+'\\'+filepath
            else:
                print 'GET DIRECTORY'
                filedir=__user__directoryMenu(dir=os.getcwd())
                filepath=filedir+'\\'+filepath
        return filepath

    def get_save_path(self):
        """ when file name doesn already exist"""
        d=self.get_directory()
        print 'enter file name'
        fname=raw_input()
        return d+'\\'+fname

    def get_directory(self,filedir=''):
        if filedir=='':
            filedir=self.__user__directoryMenu(dir=os.getcwd())
        return filedir

    def __get_directory_from_file_name(self,f):
        d = os.path.dirname(f)
        return d

    def get_copy_paths(self,fn1='',fn2=''):
        if fn1=='':
            print 'select file path to copy from'
            junk=raw_input()
            fn1=self.get_file_path()
        elif '\\' not in fn1:
            fn1=os.getcwd()+'\\'+fn1
        else:
            pass

        if fn2=='':
            print 'select directory to save in'
            junk=raw_input()
            fn2_dir=self.get_directory()
            print 'enter file name to save too'
            inp=raw_input()
            fn2=fn2_dir+'\\'+inp
        elif '\\' not in fn2:
            fn2=os.getcwd()+'\\'+fn2
        else:
            pass

        return fn1,fn2

    def get_rename_file(self,filepath=''):

        # get user query if filepath not given
        if filepath=='':
            filepath=__user__fileMenu()
            if isinstance(filepath,int):
                print 'exit...'
                return
            else:
                pass
        #######################################
        print 'current filepath: ',filepath
        print 'type new name for file:'
        newname=raw_input()
        lsf.copyfile(filepath,file__root(filepath)+'\\'+newname)
        lsf.delete_file(filepath)


    def __view_directory(self,d=''):
        if d=='':
            d=os.getcwd()
        
        bag=self.file__InFolder(d)
        bag=_remove_pyc_file_from_bag(bag)
        print 'directory: '
        print d
        print '....................'
        print 'Files:'
        print '....................'
        for item in bag[0]: print item
        print '....................'
        print 'Folders:'
        print '....................'
        for item in bag[1]: print item    
        print '....................'
     
