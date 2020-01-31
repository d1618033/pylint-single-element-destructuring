# Single Element Destructuring

![pylint_single_element_destructuring](https://github.com/d1618033/pylint-single-element-destructuring/workflows/Python%20package/badge.svg)

Some people find code like `a, = [1]` to be unreadable.
This package contains a linter that checks for such code.

## Installation

1. Run: `pip install pylint_single_element_destructuring`

2. Add to your `.pylintrc` file:

```
[MASTER]
load-plugins=
    pylint_single_element_destructuring
```


## Options

Some people find destructuring using lists to be more tolerable than destructuring
using tuples. To allow destructuring using lists simply add to your .pylintrc file:

```
[SINGLE-ELEMENT-DESTRUCTURING-CHECKER]

# Allow destructuring using lists, e.g [x] = [10]
ignore-single-element-list-destructuring=yes
```