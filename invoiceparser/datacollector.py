import pandas as pd
import os
from typing import Dict

class DataCollector(object):

    invoicedata = []
    
    """ The 'Data Collector' object serves as a repository of all invoice parsed during the session

    ### Overview:
    ----  
    The data from each parsed invoice is stored as a dictionary, such as {name: value}.
    The "Data Collector" object collects dictionaries from all invoices and stores them
    for further processing  

    ### Usage:
    ---  
        >>> parsed_invoices = DataCollector()

    """

    def add(self, data: Dict)-> None:

        """ Appends data from each invoice to the list 
   
        ### Parameters:
        ----
        data (Dict): dictionary with invoice data  

        """

        self.invoicedata.append(data)
    
    @property
    def dataframe(self):
        """ Formats collected data analysis purpose. Provides better readability.

        ### Returns:
        pandas DataFrame object

        """

        return pd.DataFrame.from_dict(self.invoicedata)

    
    def save_to_excel(self, folderpath) -> None:

        """ Saves colleceted data to Excel"""

        # checks if folder for saving excel file exists
        # can be checked at the source if Invoice Parser used with GUI
        
        try:
            os.path.isdir(folderpath)
        except OSError as e:
            print("OS error {0}".format(e))
        else:

            #appends backslash to the end of the folder path string, if not present
            folderpath = folderpath + '\\' if folderpath[len(folderpath)-1:] != '\\' or '//' else folderpath +''

            fileName = folderpath + 'invoiceslines.xlsx'

            #initializes the instance of the ExcelWriter object
            xlwriter = pd.ExcelWriter(fileName)

            #gets dataframe object

            data = self.dataframe

            #saves data to excel
            data.to_excel(xlwriter, index=False)

            xlwriter.close()