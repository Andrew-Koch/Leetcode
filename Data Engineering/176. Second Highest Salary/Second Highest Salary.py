import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    #Drop duplicates and sort values for easy access to nth highest value:
    df = employee.drop_duplicates(subset=["salary"]).sort_values("salary", ascending=False)
    #If df is too small pad rows:
    if len(df) < 2:
        df = df.reindex(range(2))
    return df[["salary"]].iloc[1:2].rename(columns={"salary": "SecondHighestSalary"})