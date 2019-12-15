# PySortVisual
A visualization of sorting algorithms using matplotlib.

# Usage
To run the script, call `python plotter.py` followed by either:
- a list of numbers seperated by commas (`,`) only
- a number `N` (and a modifier)

When a list of numbers is given, it just sorts the given list.

If a number N is given, it sorts the list `[1,2,...,N]` but affected by the modifier as follows:
- random (default): shuffles the list
- fixed: just goes with it
- almost: tweaks the list slightly
- reversed: (self-explanatory)

It then generates multiple `.mp4` files for each of the common sorting methods, which are:
- Bubble sort
- Selection sort
- Insertion sort
- Quick sort
- Merge sort
- Heap sort
