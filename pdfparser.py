import pdfplumber

class PdfParser(object):
    """ The 'Pdfparser' handles extraction of raw text from pdf """

    @staticmethod
    def extract_raw_text(filepath: str) -> str:
        """ Handles the parsing and extracting of raw text from the machine generated pdf
            
        ###Overview:
        pdfplumber library is used to perform the task.
        source: https://github.com/jsvine/pdfplumber

        ###Parameters:
        ----
        filepath(str) - filepath of the pdf file

        """

        return pdfplumber.open(filepath).pages[0].extract_text()








