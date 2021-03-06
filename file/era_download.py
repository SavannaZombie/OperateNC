
"""
Download ERA-Interim dataset using ECMWF API.
For more detail check out User Documentation at:
https://confluence.ecmwf.int/pages/viewpage.action?pageId=116970382
"""

from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer(url='https://api.ecmwf.int/v1',
                         key='1a1867215bb6286bf24203000b1283bc',
                         email='jirawat.na61@rsu.ac.th')
# %%

# 201.128 (mx2t: Maximum temperature at 2 metres since previous post-processing)
mx2t = '201.128'

# 202.128 (mn2t: Minimum temperature at 2 metres since previous post-processing)
mn2t = '202.128'

# 228.128 (tp: Total precipitation)
tp = '228.128'

# 228.004 (mean2t: Mean temperature at 2 metres)
mean2t = '228.004'

#%%
# Get regrided dataset directly from server by passing parameters as seen below
# This will be result no post-processing required after download dataset
server.retrieve({
    'class':    'ei',
    'dataset':  'interim',
    'date':     '1998-01-01/to/2014-12-31',
    'area':     '24.5/92.5/-12.5/142.5',
    'expver':   '1',
    'grid':     '0.25/0.25',
    'levtype':  'sfc',
    'param':    'mean2t',
    'step':     '12',
    'stream':   'oper',
    'time':     '00:00:00',
    'type':     'fc',
    'interpolation': 'bilinear',
    'use':      'infrequent',
    # 'format':   'netcdf',
    'target':   r'H:\Observation\ERA-Interim\ei_mean2t_sea_025km_1979_2018.grib'
})

