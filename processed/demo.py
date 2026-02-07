import pandas as pd
import numpy as np
import datetime as dt
import logging
import decimal
df =pd.read_csv('demo5.csv')


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler("logs/pipeline.log"), logging.StreamHandler()]
    )
    return logging.getLogger(__name__)

# Load Configuration
def load_config(config_path='C:/Users/Eithar/OneDrive/Desktop/week1/etl/config.json'):
    with open(config_path, 'r') as f:
        return  config_path.json.load(f)

# Main ETL Class
class CSVETLPipeline:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger()
        self.df = None

df['CPI'] = df['CPI'].round(2)

df['Temperature']=df['Temperature'].fillna('unknowm')
df['Walmart_Sales_Test']=df['Walmart_Sales_Test'].fillna('unknowm')
df['Holiday_Flag']=df['Holiday_Flag'].str.strip() 
df['Holiday_Flag']=df['Holiday_Flag'].map({'F':'FALSE','T':'TRUE','TRUE':'TRUE','FALSE':'FALSE'})                                           
df=pd.DataFrame(df)

df =df.drop_duplicates(df)
#numeric_cols=df.select_dtypes(include='object').columns[2]
#print(numeric_cols)
#df[numeric_cols]=df[numeric_cols].apply(pd.to_numeric)
#df['Weekly_Sales']=pd['Weekly_Sales'].str.map({'$':'',',':''})

#type(data.columns["CPI"])
df=df.to_csv('demo5_clean.csv',index=False)