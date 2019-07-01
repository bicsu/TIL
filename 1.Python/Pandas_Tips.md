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

#### 9. pandas resample rule

```python
'''
B         business day frequency
C         custom business day frequency (experimental)
D         calendar day frequency
W         weekly frequency
M         month end frequency
SM        semi-month end frequency (15th and end of month)
BM        business month end frequency
CBM       custom business month end frequency
MS        month start frequency
SMS       semi-month start frequency (1st and 15th)
BMS       business month start frequency
CBMS      custom business month start frequency
Q         quarter end frequency
BQ        business quarter endfrequency
QS        quarter start frequency
BQS       business quarter start frequency
A         year end frequency
BA, BY    business year end frequency
AS, YS    year start frequency
BAS, BYS  business year start frequency
BH        business hour frequency
H         hourly frequency
T, min    minutely frequency
S         secondly frequency
L, ms     milliseconds
U, us     microseconds
N         nanoseconds
'''
```

#### 10. pandas specific value row deleting

```python
i = new[(new.name == '공 종')].index
new = new.drop(i)
```

