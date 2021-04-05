import json
import os
from typing import Dict

class TemplateHandler(object):
    """ The 'TemplateHandler' object handles the templates containing patterns for values matching 
    
    ### Overview:
    Invoice parser is using regular expressions for extracting values from the invoices.

    Patterns are loadign from JSON file, rather typed in the code of the program.
    JSON file can have additional parameters inherent for a specific vendor.
    Therefore JSON file can serve as a settings file for each vendor.
    
    """

    @staticmethod
    def load_template(mapping_location: str, vendorname: str) -> Dict:
        """ Loads the template and converts to a dictionary for further processing
            
        ### Parameters:
        ----
        mapping_location (str) - location of the mapping file
        vendorname (str) - name of the vendor which invoices are being parsed

        ### Returns:
        ----
        data(Dict) - template in a dictionary format

        """

        location = mapping_location

        #check if template mapping file exists
        # can be checked at the source if Invoice Parser used with GUI
        
        try:
            os.path.exists(location)
        except Exception as e:
            print("{0}. File not found".format(e))
        else:
            with open(location) as t:
                mapping = json.load(t)

            #checking if mapping has vendorname
            try:
                mapping[vendorname]
            except KeyError as e:
                print("KeyError {0}. Vendor does not have a template".format(e))
            else:

                template_file_location = mapping[vendorname]

                #checking if template file exists
                try:
                    os.path.exists(template_file_location)
                except Exception as e:
                    print("{0}. File not found".format(e))
                else:
                    with open(template_file_location) as templ:
                        data = json.load(templ)
                
        return data