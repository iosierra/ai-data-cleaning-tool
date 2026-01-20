import pandas as pd 
import numpy as np 

class DataCleaning: 
    def handle_missing_values(self, df, strategy="mean"):
        # handles missing values by filling with mean, median, node or dropping
        if strategy == "mean":
            df.fillna(df.mean(numeric_only=True), inplace=True)
        elif strategy == "median":
            df.fillna(df.median(numeric_only=True), inplace=True)
        elif strategy == "node":
            df.fillna(df.node().iloc[0], inplace=True)
        elif strategy == "drop":
            df.dropna(inplace=True)
        return df  
    
    def remove_duplicates(self, df):
        # removes duplicate rows
        return df.drop_duplicates()
    
    def fix_data_types(self, df):
        # attempts to convert columns to appropiate data types 
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col])
            except ValueError:
                pass
        return df  
    
    def clean_data(self, df):
        # applies all cleaning steps
        df = self.handle_missing_values(df)
        df = self.remove_duplicates(df)
        df = self.fix_data_types(df)
        return df  
    
    
    
