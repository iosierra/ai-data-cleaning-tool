import sys 
import os 
import pandas as pd 
import io 
import aiohttp 
from fastapi import FastAPI, UploadFile, File, Query, HTTPException
from sqlalchemy import create_engine
from pydantic import BaseModel 
import requests

# ensure the scripts folder is in python path 
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from scripts.ai_agent import AIAgent # import AI agent 
from scripts.data_cleaning import DataCleaning # import rule-based data cleaning 

app = FastAPI()

ai_agent = AIAgent()
cleaner = DataCleaning()

# CSV / Excel Cleaning Endpoint 
@app.post("/clean-data")
async def clean_data(file: UploadFile = File(...)):
    # receives file from UI, cleans it using rule-based & ai methods and returns cleaned JSON
    try:
        contents = await file.read()
        file_extension = file.filename.split(".")[-1]

        # load file into Pandas DataFrame 
        if file_extension == "cvs":
            df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
        elif file_extension == "xlsx":
            df = pd.read_excel(io.BytesIO(contents))
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format. Use CSV or Excel.")
        
        # step 1: rule-based cleaning 
        df_cleaned = cleaner.clean_data(df)

        # step 2: ai-powered cleaning 
        df_ai_cleaned = ai_agent.process_data(df_cleaned)

        # ensure AI output is a DataFrame 
        if isinstance(df_ai_cleaned, str):
            from io import StringIO
            df_ai_cleaned = pd.read_csv(StringIO(df_ai_cleaned))

        return {"cleaned_data": df_ai_cleaned.to_dict(orient="records")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

# Database Query Cleaning Endpoint 
class DBQuery(BaseModel):
    db_url: str  
    query: str  

@app.post("/clean-db")
async def clean_db(query: DBQuery):
    # fetches data from a database, cleans it using AI and returns cleaned JSON
    try:
        engine = create_engine(engine(query.db_url))
        df = pd.read_sql(query.query, engine)

        # step 1: rule-based cleaning
        df_cleaned = cleaner.clean_data(df)

        # step 2: ai-powered cleaning 
        df_ai_cleaned = ai_agent.process_data(df_cleaned)

        # convert ai cleaned data to dataframe
        if isinstance(df_ai_cleaned, str):
            from io import StringIO
            df_ai_cleaned = pd.read_csv(StringIO(df_ai_cleaned))

        return {"cleaned_data": df_ai_cleaned.to_dict(orient="records")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from database: {str(e)}")
    
# API Data Cleaning Cleaning Endpoint 
class APIRequest(BaseModel):
    api_url: str  

@app.post("/clean-api")
async def clean_api(api_request: APIRequest):
    try: 
        async with aiohttp.ClientSession() as session:
            async with session.get(api_request.api_url) as response:
                if response.status != 200:
                    raise HTTPException(status_code=400, detail="Failed to fetch data from API.")
                
                data = await response.json()
                df = pd.DataFrame(data)

                # step 1: rule-based cleaning 
                df_cleaned = cleaner.clean_data(df)

                # step 2: ai-powered cleaning 
                df_ai_cleaned = ai_agent.process_data(df_cleaned)

                # convert ai cleaned data to dataframe 
                if isinstance(df_ai_cleaned, str):
                    from io import StringIO 
                    df_ai_cleaned = pd.read_csv(StringIO(df_ai_cleaned))

                return {"cleaned_data": df_ai_cleaned.to_dict(orient="records")}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing API data: {str(e)}")

# run server 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True) 


