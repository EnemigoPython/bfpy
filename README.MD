# BFPY - a brainf*ck interpreter in Python

## What is brainf*ck?
[Brainf*ck](https://en.wikipedia.org/wiki/Brainfuck) is an [esolang](https://en.wikipedia.org/wiki/Esoteric_programming_language) with a very simple instruction set.

## What is this?
This is an interpreter for the language, allowing you to run brainf*ck programs.

## Install
You need: python & pip

`git clone https://github.com/EnemigoPython/bfpy`

(Optional - create virtual environment) `python -m venv .venv`

`pip install -r requirements.txt`

## Use
The brainf*ck program should be the first argument of the interpreter.

The project comes with an example "Hello World!" program.

To run this for example: `.../bfpy> & .../bfpy/.venv/Scripts/python.exe .../bfpy/bfinterpreter.py helloworld.bf` replacing `...` with your working dir.