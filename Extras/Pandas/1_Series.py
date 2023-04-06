#%%
print("Hello")
# %%
import numpy as np
import pandas as pd

#%% Creating numpy array with label
# four different python objects
labels = ['A', 'B', 'C']                # labels list
my_data =[10,20,40]                     # data list
numpy_array = np.array(my_data)         # convert data list into numpy array
dict = {'A':10,'B':20,'C':40}           # dictionary with key as label and value as data

#%%
# Printing objects
print(labels)
print(my_data)
print(numpy_array)
print(dict)
# %% Creating Series using pandas
# index as labels
# passing list
pd_list_series = pd.Series(data=my_data, index=labels)
# passing numpy array
pd_numpy_series = pd.Series(numpy_array, index=labels)
#passing dictionary
pd_dict_seriies = pd.Series(data=dict)

# Printing series
print('Python list and Labels\n',pd_list_series)
print('Numpy Array and Label:\n',pd_numpy_series)
print('Dictionary\n',pd_dict_seriies)
# %% working with series

Ser1 = pd.Series([1,2,3,4] , ['USA', 'Germany', 'USSR', 'Japan'])
Ser2 = pd.Series([1,2,5,4] , ['USA', 'Germany', 'Italy', 'Japan'])
print('Series 1 :\n', Ser1)
print('Series 2 :\n', Ser2, end='\n\n')

# label indexing in pandas
print ('Data of Italy is : ',Ser2['Italy'])
print ('Data of Series 1\'s Germany is : ', Ser1['Germany'])

# %% Operations on pandas

# Perform subtraction of matched values
print('\nAddition :\n',Ser1 + Ser2)
# Perform subtraction of matched values
print('\nSubtraction :\n',Ser1 - Ser2)

# %%
