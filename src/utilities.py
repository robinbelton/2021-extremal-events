import os
import pandas as pd

def grab_budding_index(file, encoding='utf-8'):

    bud_index_bool = False
    bud_index_lines = list()

    with open(file, 'r', encoding=encoding) as f:
        for line in f.readlines():
            if 'BUDDING INDEX' in line:
                bud_index_bool = True
                continue
            if bud_index_bool:
                if 'CLOCCS PARAMETERS' in line:
                    bud_index_bool = False
                else:
                    row = line.strip().split('\t')
                    if row != ['']:
                        bud_index_lines.append(row)
    return pd.DataFrame(bud_index_lines[1:], columns=bud_index_lines[0])