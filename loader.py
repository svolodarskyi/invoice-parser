import os
from typing import List

class Loader(object):

    """ Handles the load of pdfs from the source folder """

    @staticmethod
    def get_pdf_files(folderpath) -> List:
        """ Searches pdf files in a source folder
        
        ### Parameters:
        ----
        folderpath (str): the source folder path

        ### Returns
        ----
        List of the filepaths of all the pdfs

        """

        # checks if folder for saving excel file exists
        # can be checked at the source if Invoice Parser used with GUI
        try:
            os.path.isdir(folderpath)
        except OSError as e:
            print("OS error {0}".format(e))
        else:
            #appends backslash to the end of the folder path string, if not present
            folderpath = folderpath + '\\' if folderpath[len(folderpath)-1:] != '\\' or '//' else folderpath +''
            
            all_files = os.listdir(folderpath)
            
            #outputs the list of the filepaths
            return [folderpath + a_file for a_file in all_files if a_file[len(a_file)-3:] == "pdf"]