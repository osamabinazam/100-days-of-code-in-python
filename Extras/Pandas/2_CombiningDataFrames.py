# %%
import numpy as np
import pandas as pd

# %%
# Dataframe 1
dataframe_1 = pd.DataFrame(
    {
        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3'],
        'C': ['C0', 'C1', 'C2', 'C3'],
        'D': ['D0', 'D1', 'D2', 'D3'],
    },
    index=[0, 1, 2, 3]
)

# Dataframe 2
dataframe_2 = pd.DataFrame(
    {
        'A': ['A4', 'A5', 'A6', 'A7'],
        'B': ['B4', 'B5', 'B6', 'B7'],
        'C': ['C4', 'C5', 'C6', 'C7'],
        'D': ['D4', 'D5', 'D6', 'D7'],
    },
    index=[4, 5, 6, 7]
)

# Dataframe 3
dataframe_3 = pd.DataFrame(
    {
        'A': ['A8', 'A9', 'A10', 'A11'],
        'B': ['B8', 'B9', 'B10', 'B11'],
        'C': ['C8', 'C9', 'C10', 'C11'],
        'D': ['D8', 'D9', 'D10', 'D711'],
    },
    index=[8, 9, 10, 11]
)

# %% Printing Dataframes
print('DataFrame 1 :\n')
dataframe_1
# %%
print('DataFrame 2 :\n')
dataframe_2
# %%
print('DataFrame 3 :\n')
dataframe_3

# %% Concatenation of dataframes
concat_dataframe = pd.concat([dataframe_1, dataframe_2, dataframe_3])
concat_dataframe

# %% Concating dataframe and set axis=1 so rows and columns are concatenate
# Rows and columns have no corresponding values are filled with Na N
row_col_concat = pd.concat([dataframe_1, dataframe_2, dataframe_3], axis=1)
row_col_concat

# %% More Example DataFrames (Merging)
# Left Dataframe
left = pd.DataFrame(
    {
        'Key': ['K0', 'K1', 'K2', 'K3'],
        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3']
    }
)

left
# %%
# Right Dataframe
right = pd.DataFrame(
    {
        'Key': ['K0', 'K1', 'K2', 'K3'],
        'C': ['C0', 'C1', 'C2', 'C3'],
        'D': ['D0', 'D1', 'D2', 'D3'],
    }
)
right
# %% Applying Merge logic on key  values
merged_frames = pd.merge(left, right=right, how='inner', on='Key')
merged_frames

# %% SQL Joins
left_two_keys = pd.DataFrame(
    {
        'Key1': ['K0', 'K0', 'K1', 'K1'],
        'Key2': ['K0', 'K1', 'K0', 'K1'],
        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3']
    }
)

right_two_keys = pd.DataFrame(
    {
        'Key1': ['K0', 'K1', 'K1', 'K2'],
        'Key2': ['K0', 'K0', 'K0', 'K0'],
        'C': ['C0', 'C1', 'C2', 'C3'],
        'D': ['D0', 'D1', 'D2', 'D3'],
    }
)

# %% Applying inner Join
merged_frames = pd.merge(left_two_keys, right_two_keys, on=['Key1', 'Key2'])
merged_frames

# %%Applying Outer Join
merged_frames_outer = pd.merge(left_two_keys, right_two_keys, how='outer', on=['Key1', 'Key2'])
merged_frames_outer

# %% Appying Right Join
merged_frames_right = pd.merge(left_two_keys, right_two_keys, how='right', on=['Key1', 'Key2'])
merged_frames_right

# %% JOINING

left = pd.DataFrame(
    {

        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3'],

    },
    index=['K0', 'K1', 'K2', 'K3']
)

right = pd.DataFrame(
    {

        'C': ['C0', 'C1', 'C2', 'C3'],
        'D': ['D0', 'D1', 'D2', 'D3'],

    },
    index=['K0', 'K2', 'K3', 'K4']
)
# %% Applying Joining
# index is the Key
# inner Joined
joined_dataframe = left.join(right)
joined_dataframe

# %% outer join
joined_dataframe = left.join(right, how='outer')
joined_dataframe

# %%
