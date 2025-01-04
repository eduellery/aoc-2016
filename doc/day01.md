# Complex numbers as data structure

To solve [2016, day 1](https://adventofcode.com/2016/day/1) we simply need to keep track of changes to `direction` vector and visited `positions`.

The straightforward way is to keep track of a tuple `(x, y)` for visited positions and the direction that will dictate if we need to change x or y as we travel along.

But what if we make use of the [Complex Plane](https://en.wikipedia.org/wiki/Complex_plane) to support our tracking? That way the Imaginary axis represent North-South and the Real axis represent East-West. 

We can keep track of initial position and direction pointing North as:

```python
position = 0 + 0j
direction = 0 + 1j
```

As we rotate right or left to other cardinal direction, we simply multiply `direction` by `-1j` or `1j` respectively.

Quite elegant, isn't it?
