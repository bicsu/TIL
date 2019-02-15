# *** Pandas Tips ***

#### 1. display option setting

```python
pd.set_option('display.float_format', lambda x: '%.3f' % x)	
# set the options to see all columns, rows
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('max_info_columns', 1001)
```



#### 2. pair of features correlation check

```python
corr_df = data.corr()
core = data.corr() # data is the pandas dataframe
c1 = core.abs().unstack()
pair_corr = pd.DataFrame(c1.sort_values(ascending = False),columns=['relation']).reset_index()

pair_corr = pair_corr[pair_corr['relation']!=1]

pair_corr[abs(pair_corr['relation']) >= 0.8]
```

#### 3. label encoding function

```python
from sklearn.preprocessing import LabelEncoder

object_cols = data.select_dtypes(include=['object']).columns.tolist()

def MultiLabelEncoder(columnlist,dataframe):
    for i in columnlist:
        le=LabelEncoder()
        dataframe[i] = le.fit_transform(dataframe[i])

MultiLabelEncoder(object_cols, data)
```

#### 4. Handling Missing Values

<url> https://rfriend.tistory.com/262</url>

#### 5. NaN있는 관측치 dataframe으로 가져와서 보기

```python
df[np.isnan(df.Col2)]
df2 = df[df[['col']].isnull().any(axis=1)]
```

