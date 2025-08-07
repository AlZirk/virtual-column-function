%%writefile solution.py
import pandas as pd

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    try:
        if not isinstance(new_column, str) or not new_column.isidentifier():
            return pd.DataFrame()

        role_clean = role.strip()

        tokens = role_clean.replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ").split()
        valid_tokens = set(["+", "-", "*", "/"])
        for token in tokens:
            if token not in valid_tokens and token not in df.columns:
                return pd.DataFrame()

        df_copy = df.copy()
        df_copy[new_column] = eval(role_clean, {}, df_copy.to_dict(orient='series'))

        return df_copy

    except Exception:
        return pd.DataFrame()
