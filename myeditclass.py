import os
from myfileclass import myfile as mf
import load_save_file as lsf

class txtedit(object):
    """
        self.fs --- string list of opened file
        self.fp --- file path of opened file

        example use:
        >> tx=txtedit()
        >> tx.ur()  # to load user selected text file
        >> tx.disp() # to display entire text file
        >> tx.disp([10,20]) # to display lines 10-20
        >> tx.edline(3,'x=6') # to edit line 3 to 'x=6'
        >> tx.search('print') # to display all lines with string 'print'
        >> tx.save() # to save file to user selected file path
        >> tx.rem() # to remove/delete selected file

        # in each instance where a file path is not given and a user
        # query menu is called, an actual filepath can also be given.
        # e.g. 
        >> tx.save('C:\mysavedfile.py')
    
    """


    def ur(self,filepath=[]):
        """ user read file """
        if filepath==[]:
            filepath=mf().gf()


        self.fs=lsf.file_to_str_list(filepath)
        self.fp=filepath
            

    def disp(self,lns=[]):
        """ display file with line numbers - starting at 0
            lns - is line numbers to be displayed
            e.g. lns=[4,10]
            displays lines 4 - 10 inclusive
            
        """

        if lns==[]:
            for n,ii in enumerate(self.fs):
                print n+1,ii,

        else:    
            # print lines in range given by lns
            temp=range(lns[0],lns[1]+1)

            for n,ii in enumerate(self.fs):
                if n in temp:
                    print n+1,ii,

    def save(self,filepath=[]):
        """ save to file to filepath
            if filepath is given
            if no filepath is given
            user menu to select file path
        """
        if filepath==[]:
            filepath=mf().get_save_path()

        textString=''.join(self.fs)    
        lsf.str_to_file(textString,filepath)
        print 'saved to::',filepath

    def search(self,s):
        """ STRING SEARCH - display lines in file containing s
        """
        for n,ii in enumerate(self.fs):
            if s in ii:
                self.disp([n,n])
                

    def rem(self,filepath=[]):
        """ used to delete file at filepath """
        print "warning this action will delete file "
        print "type xx to exit"
        a=raw_input()
        if a=='xx':
            print 'did not delete file'
            return False
        
        if filepath==[]:
            filepath=mf().gf()
        os.remove(filepath)
        print 'deleted file:::',filepath

        
        

    def edline(self,n,s):
        """ n is the line number to be edited
            s is the string to insert at this line number
            automatically adds new line"""
        self.fs[n-1]=s+'\n'
