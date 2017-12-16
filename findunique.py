import pandas as pd 
import numpy as np
from pandas import DataFrame
from pandas import ExcelWriter
import numpy as np

screenfile = 'file:///C:/Users/B1/Desktop/MSQ/Screencompany.xlsx'
companydatabase = 'file:///C:/Users/B1/Desktop/MSQ/company_list.xlsx'
companylist = pd.read_excel(companydatabase)
screencompany=pd.read_excel(screenfile)           
duplicatelist = []
companylist1 = (np.array(companylist)).tolist()
screencompany1 = np.array(screencompany)
for value in screencompany1:
   
   if value in companylist1:
      duplicatelist.append(str(value))

   else:
      companylist1.append(str(value))
      
df ={'total company list' : pd.Series(companylist1)}
df = pd.DataFrame(df)

name = companydatabase.split('/')[-1]
writer = ExcelWriter(name)
df.to_excel(writer,'Sheet2')
writer.save()





    


