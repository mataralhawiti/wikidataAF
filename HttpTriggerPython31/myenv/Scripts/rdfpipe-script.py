#!D:\home\site\wwwroot\HttpTriggerPython31\myenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'rdflib==4.2.2','console_scripts','rdfpipe'
__requires__ = 'rdflib==4.2.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('rdflib==4.2.2', 'console_scripts', 'rdfpipe')()
    )
