# Invoice Parser for Account Payable Automation

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Templates](#templates)
- [Usage](#usage)

## Overview

This library was developed for a purpose of accounts payable automation in a real-life company.
It can be used as a standalone solution or as a part of a workflow.

At this point it is working only with machine generated pdf files. 

OCR functionality will added on the next iterations.



## Setup

To use the project you need to install the dependencies listed in the `requirements.txt` file.
Dependencies can be installed by running the following command:

```console
pip install -r requirements.txt
```

## Templates
This library supposes that each vendor will have a separate template. 

Templates are the collection of patterns (regular extressions) and other parameters stored in JSON file. 
Patterns are used for extracting data from the invoice.

Template JSON file can store any other parameters. The libary is not restricted to any specific format of the templates. 

#### Steps for adding vendor template:
1. Creating JSON file with a template.
2. Adding created template to the Template Mapping JSON file.

To see the example of template handling, refer to the section `Usage` below and `sample` folder of the repository. 

## Usage

Below is an example of using the `invoice-parser` library.

```python
from invoiceparser.loader import Loader
from invoiceparser.pdfparser import PdfParser
from invoiceparser.invoice import Invoice
from invoiceparser.matcher import Matcher
from invoiceparser.templatehandler import TemplateHandler
from invoiceparser.datacollector import DataCollector


# if GUI used for the front-end below variable will be passed from it
vendorname = 'Vendor1'
templatemapping = 'TemplateMapping.json'
folder_with_pdf = 'C:/Users/user/invoiceparser/src'
output_folder = 'C:/Users/user/invoiceparser/'

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

print(parsed_data.dataframe)
parsed_data.save_to_excel(output_folder)
```



