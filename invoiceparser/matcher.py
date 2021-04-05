import  re
from typing import Tuple

class Matcher(object):
    """ The 'Matcher' object handles the search of vaues based on regex pattern"""

    @staticmethod
    def find_match(reg_ex: str, text: str) -> Tuple:
        """Finds the match
        
        ### Overview

        On each call the 'Matcher' object will start the search from the position it finished 
        the search on the previous call.
        The 'Matcher' object will return the text for next search.

        """
        #match object
        match = re.compile(reg_ex).search(text)
        
        #matched value and text for the next search
        return match.group(), text[match.end():]