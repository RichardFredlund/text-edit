Functions for use at the command prompt in
python shell. 

myeditclass -  provides methods for viewing and editing text files directly from the command prompt. 

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
    
myfileclass - provides text menu at command prompt for getting file or directory paths

	 ff=myfile()

        ff.gf() -- user query menu to get file path
        ff.gd() -- user query menu to get directory
        ff.get_save_path() -- which also queries user for filename

load_save_file - provides functions for loading and saving files/objects 

     these can be used with the user menu system from file class

     example:
		load_save_file.str_to_file(myfile().gf())

     would query the user for file path. 
