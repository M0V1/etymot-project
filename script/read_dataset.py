import os
import urllib.request
import pandas as pd

URL = "https://github.com/M0V1/etymot-project/releases/download/data-v1/etymology.parquet"
PATH = "data/etymology.parquet"

if not os.path.exists(PATH):
    os.makedirs("data", exist_ok=True)
    urllib.request.urlretrieve(URL, PATH)

df = pd.read_parquet(PATH)

# read the parquet in a dataframe 
df = pd.read_parquet(PATH)
#df.info()
#print(df.shape)
#print(df.head(5))
#print(df.columns)
#columns name 'term_id', 'lang', 'term', 'reltype', 'related_term_id', 'related_lang', 'related_term', 'position', 'group_tag', 'parent_tag','parent_position'

#check the dataset
print(df["lang"].value_counts())
print(df["reltype"].value_counts())
print(df.isna().sum())
