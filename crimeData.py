import requests
import pandas as pd
base = 'https://api.usa.gov/crime/fbi/cde/'
key = 'fuSpSFJaX1ysTXFUIjzJIa26noCsxJZGETmgEJ69' 

query = 'agency/byStateAbbr/GA?API_KEY='
response = requests.get(base + query + key)
data = response.json()
df = pd.DataFrame(data)
# print(df[df['agency_name'].str.contains('Rome')])
print(df[df['agency_type_name'].str.contains('State')])