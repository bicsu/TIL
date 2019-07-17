### python print 서식

```python
print('빈칸 10개, 1자리까지: %10.1f' % 0.12345)

```

### python 정규표현식

```python
import re
def cleanText(data):
    #텍스트에 포함되어 있는 특수 문자 제거
    text= re.sub('[-=+,#/\?:^%$.@*\'\(\(\[\]\<\>]','', data)
    return text

```

### python 

```python
for i, j in zip(list, list[1:]):
    d = i + j # list 앞 뒤 원소 접근해서 사용할 수 있어서 꿀
```

