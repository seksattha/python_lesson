
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
file_path = 'atm-report (7).xlsx'
df = pd.read_excel(file_path)
df.rename(columns={'Test Cycle.OS version': 'os_version',
                   'Test Cycle.Mobile model': 'mobile_model',
                   'Test Cycle.Brand': 'mobile_brand',
                   'Test Cycle.Unit Type': 'ac_group',
                   'Test Cycle.Unit Model': 'ac_model',
                   'Execution.Result': 'test_result',
                   'Test Case.Name': 'test_program'
                   },
          inplace=True

          )
selected_columns = ['os_version', 'mobile_model', 'mobile_brand', 'ac_group', 'ac_model', 'test_result',
                    'test_program']

df2 = df.loc[:, selected_columns]
df2['ac_group_model'] = df2.ac_group + " (" + df.ac_model + ")"
g = df2.groupby(['mobile_model', 'ac_group_model'])['test_result']


def check_result(g):
    try:
        if g.str.contains('Pass').all():
            return 'Pass'
        else:
            return 'fail'

    except Exception as e:
        return np.nan

result = g.get_group(('Mi Pad 4 Plus', 'RA (FTXM60UVMZ)')).apply(check_result)
