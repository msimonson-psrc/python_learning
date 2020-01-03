#  Taken from https://datatofish.com/read_excel/

import pandas as pd


df = pd.read_excel ("C:\mhs_workfiles\ofm_april1_housing.xlsx"
                    , sheetname = "Sheet2"
                    ,skiprows = range(0,3)
                    ,index_col=3
                    ,usecols = [0,1,2,3,4,8,12,16,20,24,28,32,36,40,44]
                    )
                    
# OFM's latest Housing Unit estimates at https://www.ofm.wa.gov/washington-data-research/population-demographics/population-estimates/april-1-official-population-estimates

print (df.head())

