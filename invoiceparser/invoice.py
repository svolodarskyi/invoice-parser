from typing import List, Dict

class Invoice(object):
    
    """ The 'Invoice' object handles storage of the invoice attributes  """

    def __init__(self, template: Dict, text:str):

        """Initializes Invoice Instance        
        
        The 'Invoice' object may store various invoice parameters which will be usefull for further parsing

        ### Arguments:
        ----
        template(Dict): json file converted to a dictionary with the 'TemlateHandler' Object. contains 
        collection of key-value pairs such as {invoice field: static value or regex for matching} 

        text(str): text extracted with the 'Parser' object.
        
        ### Usage:
        ---  
            >>> inv = Invoice(template, extracted_from_pdf_text)
        """
        
        self._template = template
        self._text = text

    @property
    def template(self) -> Dict:
        """Getter for template attribute"""
        
        return self._template

    @property
    def text(self) -> str:
        """Getter for text attribute"""
        
        return self._text
        
    @text.setter
    def text(self, newtext) -> None:
        """Setter for text attribute
        
        ### Overview

        Text attribute is intended to be used by the 'Matcher' object for searching needed value.
        On each call the 'Matcher' object will start the search from the position it finished search on the previous call.
        The 'Matcher' object will define the text for next search and return its value.
        Text setter is used to reassign the text attribute of the current 'Invoice' object instance. 

        """

        if newtext == "":
            raise ValueError("Valid text should be assigned")
        
        self._text = newtext