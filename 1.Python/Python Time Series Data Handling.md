### Python Time Series Data Handling

* 년월일 데이터 바꾸기

```python
#1
train['date'] = pd.to_datetime(train['date'], dayfirst=True)
#2
train['date'] = pd.to_datetime(train.date,format="%d.%m.%Y")
```

