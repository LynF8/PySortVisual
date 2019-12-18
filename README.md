# PySortVisual
A visualization of sorting algorithms using matplotlib.

# Usage
`python plotter.py arg1 [arg2 [arg3 [arg4]]]`

- There are two possible options for `arg1`:
    - `play`: play the animation of the result.
    - `save-mp4`: save the result as an `.mp4` file.
- There are five possible options for `arg2`:
    - `random`(default): the array will be shuffled.
    - `fixed`: the array will be sorted (before the algorithm is run).
    - `almost`: the array will be almost sorted.
    - `reversed`: the array will be reversed.
    - `custom`: the array will be specified.
- There are two possible options for `arg3`:
    - an positive integer(default 10): the sequence will be array of integers from 1 to that number.
    - a sequence of positive integers separated by commas only: it will be the sequence.
- There are seven possible options for `arg4`:
    - `all`(default): Shows/Stores the visualizations of all sorting algorithms below **separately**.
    - `bubble-sort`: Only show the visualization of bubble sorting algorithm in the animation. The following arguments have similar functions.
    - `heap-sort`
    - `insertion-sort`
    - `merge-sort`
    - `selection-sort`
    - `quick-sort`