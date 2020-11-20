Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

1: [1, 1]
3: [1, 1], [3, 3]
7: [1, 1], [3, 3], [7, 7]
2: [1, 3], [7, 7]
6: [1, 3], [6, 7]
4: [1, 4], [6, 7]
10: [1, 4], [6, 7], [10, 10]
