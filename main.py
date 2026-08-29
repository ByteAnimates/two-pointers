"""
Run it: python3 main.py

Two pointers instead of a nested loop. The reel's claim is that every move rules out a
whole row of pairs — which is why one sweep is enough, and why the array being sorted is
not a convenience but the entire reason it works.
"""

from two_pointers import find_pair

VALUES = [3, 8, 14, 21, 27, 34]   # the six the reel searches
TARGET = 35


def steps(a: list[int], target: int) -> int:
    """Pointer moves before the answer. At most n-1 — the two ends can only converge."""
    i, j = 0, len(a) - 1
    n = 0
    while i < j:
        s = a[i] + a[j]
        if s == target:
            return n
        n += 1
        if s < target:
            i += 1
        else:
            j -= 1
    return n


def brute_force(a: list[int], target: int):
    """The nested loop this replaces, and the count of pairs it looks at."""
    seen = 0
    for x in range(len(a)):
        for y in range(x + 1, len(a)):
            seen += 1
            if a[x] + a[y] == target:
                return (x, y), seen
    return None, seen


def main() -> None:
    found = find_pair(VALUES, TARGET)
    i, j = found
    moves = steps(VALUES, TARGET)
    _, checked = brute_force(VALUES, TARGET)

    print(f'\n  {VALUES}   target {TARGET}\n')
    print(f'  found {VALUES[i]} + {VALUES[j]} = {TARGET}  at indices {i}, {j}\n')
    print(f'  two pointers   {moves} moves')
    print(f'  nested loop    {checked} pairs examined')

    n = len(VALUES)
    print(
        f'\n  Each move discards a whole row. When the sum is too big, the largest value\n'
        f'  cannot pair with ANYTHING left — it is already too much with the smallest —\n'
        f'  so the right pointer steps in and {n - 1} pairs go with it. That is why one\n'
        f'  sweep suffices, and why it needs the array sorted: on unsorted data the sum\n'
        f'  says nothing about which way to move.\n'
    )



if __name__ == '__main__':
    main()
