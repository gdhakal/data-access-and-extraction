# Data Wrangling & Intro to pandas

Introduction to pandas, Jupyter notebook, and matplotlib to apply basic methods for cleaning and wrangling data. Learn how to use pandas data structures, import and inspect data, and conduct operations like indexing and plotting.


# Notes

* Extract day from the given date-time string.
```python
import pandas
dt = '4/30/2014 23:22:00'
d, t = dt.split(' ')
m,d,y = d.split('/')
print(int(d))
```

* Convert date string to date-time format
```python
dt = '4/30/2014 23:22:00'
dt = pandas.to_datetime(dt)
```
