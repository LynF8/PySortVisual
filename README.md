# PySortVisual
PySortVisual is a program which helps you visualize a variety of sorting algorithms, with any array of your choice! The visualization is color coded for a better understanding as well as fascination :)

![alt text](https://raw.githubusercontent.com/LynF8/PySortVisual/master/sample-screenshot.png "Screenshot from PySortVisual. Picture shows heap sort being executed.")

# Usage
`python plotter.py arg1 [arg2 [arg3 [arg4]]]`

- There are two possible options for `arg1`:
    - `play`: play the animation of the result.
    - `save-mp4`: save the result as an `.mp4` file. The length of the video is at most 1 minute.
- There are seven possible options for `arg2`:
    - `all`(default): Shows/Stores the visualizations of all sorting algorithms below **separately**.
    - `bubble-sort`: Only show the visualization of bubble sorting algorithm in the animation. The following arguments have similar functions.
    - `heap-sort`
    - `insertion-sort`
    - `merge-sort`
    - `selection-sort`
    - `quick-sort`
- There are five possible options for `arg3`:
    - `random`(default): the array will be shuffled.
    - `sorted`: the array will be sorted (before the algorithm is run).
    - `almost-sorted`: the array will be almost sorted.
    - `reversed`: the array will be reversed.
    - `almost-reversed`: the array will be almost reversed.
    - `custom`: the array will be specified.
- There are two possible options for `arg4`:
    - an positive integer(default 10): the sequence will be array of integers from 1 to that number.
    - a sequence of positive integers separated by commas only: only usable if `arg3` is `custom`.
