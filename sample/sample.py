from invoiceparser.loader import Loader
from invoiceparser.pdfparser import PdfParser
from invoiceparser.invoice import Invoice
from invoiceparser.matcher import Matcher
from invoiceparser.templatehandler import TemplateHandler
from invoiceparser.datacollector import DataCollector


# if GUI used for the front-end below variable will be passed from it
vendorname = 'Vendor1'
templatemapping = 'TemplateMapping.json'
folder_with_pdf = 'C:/Users/user/Documents/Python/libraries/py101/invoice_pdf_parser/src'
output_folder = 'C:/Users/user/Documents/Python/libraries/py101/invoice_pdf_parser/'

#loading pdf files
files = Loader.get_pdf_files(folder_with_pdf)

#loading the template
template = TemplateHandler.load_template(templatemapping, vendorname)

#creating repository for storing parsed data
parsed_data = DataCollector()

for f in files:

    inv = Invoice(template, PdfParser.extract_raw_text(f))

    invdata = {}

    """ 
    Loaded template contains value indicator.
    It specifies if value contains regular expression or not.
    """
    for key, value in inv.template.items():
        if inv.template[key][0] == 'regex':
            invdata[key], inv.text = Matcher.find_match(inv.template[key][1], inv.text)
        else:
            invdata[key] = inv.template[key][1]
    
    parsed_data.add(invdata)

"""
parsed data can be displayed in  readable format on the console
    >>>print(parsed_data.dataframe)
"""
print(parsed_data.dataframe)
#parsed_data.save_to_excel(output_folder)