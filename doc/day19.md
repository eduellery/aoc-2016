# The importance of patterns

While solving [2016, Day 19](https://adventofcode.com/2016/day/19), I realized I didn't need to count the presents at all. Instead, I could represent the elves as a linked list, where each elf points to their next victim. Eliminating an elf and taking their present involved reassigning the pointer of the taker to skip over the victim. This simple approach worked efficiently. When an elf's next victim pointed back to themselves, it signified they were the last one standing.

Here’s the core logic in Python:

```python
while self.elves[i] != i:
    self.elves[i]  = self.elves[self.elves[i]]
    i = self.elves[i]
```

## The challenge of part 2

The complexity increased in Part 2 due to the new rules, which required dynamic resizing of the list. Using basic math and modular operations, I identified the next victim in front of the current elf. Although the solution worked, it took around 5 minutes for the large input. I suspected a better data structure could improve the efficiency, but this exploration unexpectedly led to an optimized solution for Part 1 instead.

## Discovering the Josephus Problem

While researching, I came across the [Josephus problem](https://en.wikipedia.org/wiki/Josephus_problem), beautifully explained in [this Numberphile video](https://www.youtube.com/watch?v=uCsD3ZGzMgE). What fascinated me was not just the solution but the empirical approach of testing different inputs to uncover patterns. The formula itself emerges from these observations:

```python
int(bin(self.size)[3:] + "0", 2) + 1
```

## Observing patterns for part 2

Exploring the second part revealed intriguing patterns in the first 100 inputs and their results:

| input | result | input | result | input | result | input | result | input | result |
|-------|--------|-------|--------|-------|--------|-------|--------|-------|--------|
|  1    |  1     |  21   |  12    |  41   |  14    |  61   |  34    |  81   |  54    |
|  2    |  1     |  22   |  13    |  42   |  15    |  62   |  35    |  82   |  1     |
|  3    |  3     |  23   |  14    |  43   |  16    |  63   |  36    |  83   |  2     |
|  4    |  1     |  24   |  15    |  44   |  17    |  64   |  37    |  84   |  3     |
|  5    |  2     |  25   |  16    |  45   |  18    |  65   |  38    |  85   |  4     |
|  6    |  3     |  26   |  17    |  46   |  19    |  66   |  39    |  86   |  5     |
|  7    |  4     |  27   |  18    |  47   |  20    |  67   |  40    |  87   |  6     |
|  8    |  5     |  28   |  1     |  48   |  21    |  68   |  41    |  88   |  7     |
|  9    |  6     |  29   |  2     |  49   |  22    |  69   |  42    |  89   |  8     |
|  10   |  1     |  30   |  3     |  50   |  23    |  70   |  43    |  90   |  9     |
|  11   |  2     |  31   |  4     |  51   |  24    |  71   |  44    |  91   |  10    |
|  12   |  3     |  32   |  5     |  52   |  25    |  72   |  45    |  92   |  11    |
|  13   |  4     |  33   |  6     |  53   |  26    |  73   |  46    |  93   |  12    |
|  14   |  5     |  34   |  7     |  54   |  27    |  74   |  47    |  94   |  13    |
|  15   |  6     |  35   |  8     |  55   |  28    |  75   |  48    |  95   |  14    |
|  16   |  7     |  36   |  9     |  56   |  29    |  76   |  49    |  96   |  15    |
|  17   |  8     |  37   |  10    |  57   |  30    |  77   |  50    |  97   |  16    |
|  18   |  9     |  38   |  11    |  58   |  31    |  78   |  51    |  98   |  17    |
|  19   |  10    |  39   |  12    |  59   |  32    |  79   |  52    |  99   |  18    |
|  20   |  11    |  40   |  13    |  60   |  33    |  80   |  53    |  100  |  19    |

(And so on...)

A connection emerged between the input and the nearest lower power of 3 (1, 3, 9, 27, 81...). This insight led to the following algorithm, excluding corner cases for very low inputs:

```python
winner = 1
while winner * 3 < self.size:
    winner *= 3
return self.size - winner
```

## From minutes to milliseconds

With this optimized algorithm, the solution time dropped from 5 minutes to mere milliseconds—a striking improvement. This experience underscored the power of pattern recognition and empirical problem-solving in algorithm design.
