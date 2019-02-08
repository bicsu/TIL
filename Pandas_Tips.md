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

### 

