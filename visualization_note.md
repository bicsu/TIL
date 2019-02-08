# <center>시각화</center>

```python
# correlation + heatmap
plt.figure(figsize=(10,6))
sns.heatmap(dataset.corr(),cmap = 'coolwarm',linewidth = 1,annot= True, annot_kws={"size": 9})
plt.title('Variable Correlation')


# from : https://www.kaggle.com/stephaniestallworth/melbourne-housing-market-eda-and-regression
```

### 2. Binary variable visualization

A binary variable, we can see the distribtution of housing pric is quite different for the two groups. So it is likely to be a good predictor.

```python
wf = train.waterfront.unique()
for i in wf:
    temp_x=train.loc[train.waterfront==i,'log_price']
    ax = sns.kdeplot(temp_x,shade=True)
plt.title('Distribution of log_price by waterfront')
```

![1548722592144](/home/pirl/.config/Typora/typora-user-images/1548722592144.png)

#### 3. plt label size & font 조절

```python
plt.rc('ytick',labelsize=15)
# To use 한글 font in graphs
plt.rc('font', family='NanumBarunGothic')
plt.rcParams['axes.unicode_minus']=False
```



#### 4. distplot에서 정규분포 확인하기

```python
from scipy.stats import norm
sns.distplot(df["LSTAT"], fit=norm) #fit = norm을 추가
```

![1548910962498](/home/pirl/.config/Typora/typora-user-images/1548910962498.png)

