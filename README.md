# MSCSAPPStatus
A python application to check MS CS admission results in batch without the pain of having to manually login to each website individually. 

Currently it supports the following universities:
+ Purdue
+ Arizona State 
+ Suny Stony Brook
+ Virginia Tech.
+ North Eastern

Python Requirements:
+ [Mechanize](https://pypi.python.org/pypi/mechanize/)

### Running Application

1. Just checking application status without any log. 
```python allCombined.py```

2. Application status with log.
```python allCombined.py 1```

3. Application status with log + saving html of logged in webpage.
```python allCombined.py 2```