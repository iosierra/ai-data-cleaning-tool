from data_cleaning import DataIngestion 
from data_cleaning import DataCleaning
from ai_agent import AIAgent

# database configuration 

DB_USER = "postgres"
DB_PASSWORD = "qzmpg*"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "demo_cleaningdb"

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# initiliaze components 
ingestion = DataIngestion(DB_URL)
cleaner = DataCleaning()
ai_agent = AIAgent()

# load and clean CSV Data 
df_csv = ingestion.load_csv("sample_data.csv")
if df_csv is not None: 
    print("\n Cleaning CSV Data...")
    df_csv = cleaner.clean_data(df_csv)
    df_csv = ai_agent.process_data(df_csv)
    print("\n AI-Cleaned CSV Data:\n", df_csv)

# load and clean excel data 
df_excel = ingestion.load_excel("sample_data.xlsx")
if df_excel is not None:
    print("\nCleaning Excel Data...")
    df_excel = cleaner.clean_data(df_excel)
    df_excel = ai_agent.process_data(df_excel)
    print("\n AI-Cleaned Excel Data:\n", df_excel)

# load and clean database data 
df_db = ingestion.load_from_database("SELECT * FROM people") 
if df_db is not None:
    print("\n Cleaning Database Data...")
    df_db = cleaner.clean_data(df_db)
    df_db = ai_agent.process_data(df_db)
    print("\n AI-Cleaned Database Data: \n", df_db)

# fetch and clean api data 
API_URL = "https://jsonplaceholder.typicode.com/posts"
df_api = ingestion.fetch_from_api(API_URL)

if df_api is not None: 
    print("\n Cleaning API Data...")

    # keep only first N rows to avoid token overflow
    df_api = df_api.head(30) # adjust this value based on your dataset size 

    # reduce long text fields before sending to OpenAI 
    if "body" in df_api.columns:
        df_api["body"] = df_api["body"].apply(lambda x: x[:100] + "..." if isinstance(x, str) else x) # limit text length 

    df_api = cleaner.clean_data(df_api)
    df_api = ai_agent.process_data(df_api)

    print("\n AI-Cleaned API Data:\n", df_api)
