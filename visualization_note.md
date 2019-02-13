# <center>시각화</center>

```python
# correlation + heatmap
plt.figure(figsize=(10,6))
sns.heatmap(dataset.corr(),cmap = 'coolwarm',linewidth = 1,annot= True, annot_kws={"size": 9})
plt.title('Variable Correlation')


# from : https://www.kaggle.com/stephaniestallworth/melbourne-housing-market-eda-and-regression
```

#### 2. Binary variable visualization

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

#### 5. Feature Importance Visualization

```python
def plot_feature_importances(model):
    cols = X.columns
    importances = model.feature_importances_
    indices = np.argsort(model.feature_importances_)
    plt.barh(range(len(indices)), importances[indices], align="center", color='r')
    plt.yticks(range(len(indices)), [cols[i] for i in indices])
    plt.xlabel("설명변수 중요도")
    plt.ylabel('설명변수')
    plt.ylim(-1, len(cols))

# 설명 변수 중요도 그래프 함수 실행
plt.figure(figsize=(10,8))
plot_feature_importances(<모델명>)
```

#### 6. ROC Curve

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_curve, roc_auc_score
from matplotlib import pyplot as plt

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = tree.predict_proba(X_test)

print roc_auc_score(y_test, predict_proba[:,1])

fpr, tpr, _ = roc_curve(y_test, predictions[:,1])

plt.clf()
plot.plot(fpr, tpr)
plt.xlabel('FPR')
plt.ylabel('TPR')
plt.title('ROC curve')
plt.show()
```

#### 7. Scatter plot with continuous hue

https://stackoverflow.com/questions/44641669/scatterplot-with-point-colors-representing-a-continuous-variable-in-seaborn-face

#### 8. for loop box plot

```python
rows = 4
if((((len(num_col) + 1) // rows) % rows) == 0): 
    cols = (len(num_col)+1) // rows
else:
    cols = ((len(num_col)+1) // rows) + ((len(num_col) // rows) % rows)

fig, axs = plt.subplots(rows, cols, figsize=(20,20))
fig.subplots_adjust(hspace = 0.05, wspace=0.3)
axs = axs.ravel()
for j,k in enumerate(num_col):
    b = sns.boxplot(y = k, data=raw_data,ax = axs[j],)
    b.set_ylabel(k,fontsize=20)

```

#### subplot example

```python
Z_ward = linkage(x, method='ward', metric='euclidean')
Z_average = linkage(x, method='average', metric='euclidean')
Z_Minkowski = linkage(x, method='average', metric='minkowski')

plt.figure(figsize = (10,20))
ax = plt.subplot(311)
dendrogram(Z_ward, leaf_font_size=10, orientation='right')
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("distance")
plt.ylabel("sample index")
ax = plt.subplot(312)
dendrogram(Z_average, leaf_font_size=10, orientation='right')
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("distance")
plt.ylabel("sample index")
ax = plt.subplot(313)
dendrogram(Z_Minkowski, leaf_font_size=10, orientation='right')
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("distance")
plt.ylabel("sample index")
# plt.subplots_adjust(hspace = 0.3)
```

#### several scatter plot with for loop

```python
num_col = list(plot_data.columns)
rows = len(num_col)-2

fig, axs = plt.subplots(rows, 1, figsize=(6,30))
fig.subplots_adjust(hspace = 0.23)
axs = axs.ravel()
for j,k in enumerate(num_col[2:]):
    b = sns.scatterplot(x='Prin1',y = k, data=plot_data,ax = axs[j],hue='diagnosis')
    b.set_ylabel(k,fontsize=10)
    b.set_title('Prin1 vs'+ ' '+ k,fontsize=15, color='r')
```

![scatters](/home/pirl/Pictures/scatters.png)