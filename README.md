# antlr4-python

## Requirements
* antlr4-python3-runtime: `pip install antlr4-python3-runtime`

## Run tests
* `python -m pytest -v`

## Parser generation from the grammar
* [install ANTLR4 and create the aliases](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md#installation)
* run `antlr4 -o parser -visitor -Dlanguage=Python3 Hello.g4`