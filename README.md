# Game of Life  

## Prerequisites

- Python 3.6

## How to run

1. Run with random state 
```python game_of_life.py```

2. Run with declared state file 
```python game_of_life.py plus.txt```

3. Run with declared state file & dump N th generation state 
```python game_of_life.py plus.txt 10``` 
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
