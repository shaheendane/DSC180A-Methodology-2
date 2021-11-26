import sys
import json
import pandas as pd
import numpy as np

from eda import basic_eda

def main(targets):
        
    if 'test' in targets:
        data = pd.ExcelFile('test/testdata/Smarr PeerJ Data.xlsx')
        basic_eda(data)
        
        
        
if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
