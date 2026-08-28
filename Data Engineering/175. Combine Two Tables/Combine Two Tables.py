import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    #Merge dataframes on personID, returning null where no match present:
    mergedDF = person.merge(address, on="personId", how="left")
    return mergedDF[['firstName', 'lastName', 'city', 'state']]