# Game of Life  

should be deleted

Game of Life implemented on PyQT5.
It can run in 3 ways (1.random state, 2. state initialized described in file, 3. process N th generation then dump last state)
> random state will be initialized below conditions. (row : 40 ~ 80, col : 80 ~ 120)

## Prerequisites

- Python 3.6

## How to run through python

1. install python package with ```install.sh```

2. Run with random state 
``` python game_of_life.py```

3. Run with declared state file 
```python game_of_life.py plus.txt```

4. Run with declared state file & dump N th generation state 
```python game_of_life.py plus.txt 10``` 
- dump N th generation state into ```result.txt``` file

## How to run through exec file

Download & Unzip this[https://drive.google.com/file/d/1Zqjo77ZCLVs9-1J-gwann6NO-1XSP5fS/view?usp=sharing]

1. Run with random state 
``` ./game_of_life```

2. Run with declared state file 
```./game_of_life plus.txt```

3. Run with declared state file & dump N th generation state 
```./game_of_life.py plus.txt 10``` 
- dump N th generation state into ```result.txt``` file

## State file schema

```
40 80 # row, col size 
5 # N th initial cells count
19 19 # initial cell #1
20 18 # ...
20 19 # ...
20 20 # ...
21 19 # initial cell N
```
