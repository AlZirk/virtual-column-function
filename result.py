from solution import add_virtual_column
import pandas as pd

df = pd.DataFrame({
    "first_column": [1, 2, 3],
    "second_column": [4, 5, 6]
})

df_result = add_virtual_column(df, "first_column + second_column", "result")
print(df_result)
