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
# missing data percentage 구하기
def get_percentage_missing(series):
    num = series.isnull().sum()
    den = len(series)
    return (num/den * 100)

#특정 column Nan값의 관측치만 dropna하기
train = train.dropna(subset=['room_count', 'bathroom_count'], how='all')
```

#### 6. describe data형태별로 보기

```python
df.describe(include=[np.number]) #np.object
```

#### 7. Pandas datetime method 활용

```python
df['date'] = pd.to_datetime(df['date'])
df['date'].dt.weekday_name
df['date'].dt.month
df['date'].dt.day
```

#### 8. loc 활용

```python
#
data.loc[data['시력(우)'] > 9, '시력(우)'] = data['시력(좌)']

```

#### 9. str.split & expanding columns with renaming

```python
df['string'].str.split(',', expand=True).rename(columns = lambda x: "string"+str(x+1))

concat(sort=False, axis = 0)
```

#### 10. 시계열 분석(Seasonal ARIMA)

```python
from pyramid.arima import auto_arima
stepwise_model = auto_arima(data, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())
```

<https://medium.com/@josemarcialportilla/using-python-and-auto-arima-to-forecast-seasonal-time-series-90877adff03c>



