# convert-base
The convert-base library in Python!


## Installation

Install from PyPI:

```zsh
$ pip install base-x-converter
```

## From the command line

Use the `convert` command.

```zsh
$ convert ABC 16 2
101010111100
```

### Arguments

It takes three positional arguments:
* `number`: The number to convert
* `fbase`: The base to convert from
* `tbase`: The base to convert to

It also has one optional argument:
* `-g`: Group the digits?

### Grouping

Just use the `-g` flag to group your digits in groups of 4

```zsh
$ convert ABC 16 2 -g
1010 1011 1100
```

Or, specify a number after `-g` to group it in groups of that number

```zsh
$ convert ABC 16 2 -g 5
00010 10101 11100
```

Note: it will automatically fill the left group with zeros to match the grouping.

## From Python

### Import library

```python
from convert_base import convert
```

### Convert from base X to base Y

```python
print(convert('ABC', 16, 2))
```

### Use your own alphabet

```python
print(convert('ABC', 16, 2, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
```

Note: it defaults to `'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-'`
