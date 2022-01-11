from flask import Flask
from database import session
import pandas as pd

app = Flask(__name__)





@app.route('/')
def home():
    return 'API works'


@app.route('/list_tables')
def list_tables():
    query = "SELECT * FROM INFORMATION_SCHEMA.TABLES"
    tables_df=pd.read_sql(query, session)
    tables_json = tables_df.to_json(orient = 'records')
    return tables_json


@app.route('/get_sell_invoices')
def get_sell_invoices():
    query = "SELECT * FROM dim.DocumentItems_hm_dp"
    if session:
        tables_df=pd.read_sql(query, session)
    else:
        tables_df = pd.read_json('invoices.json')
    tables_json = tables_df.to_json(orient = 'records')
    return tables_json
