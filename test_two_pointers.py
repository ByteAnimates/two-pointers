"""
Run it: python3 test_two_pointers.py   (or: pytest)
"""

from main import TARGET, VALUES, brute_force, steps
from two_pointers import find_pair


def test_it_finds_a_pair_that_really_sums_to_the_target():
    i, j = find_pair(VALUES, TARGET)
    assert VALUES[i] + VALUES[j] == TARGET


def test_one_sweep_is_enough():
    # The claim the episode is about: the pointers only ever converge, so the work is
    # bounded by the length rather than by the number of pairs.
    assert steps(VALUES, TARGET) < len(VALUES)
    assert brute_force(VALUES, TARGET)[1] > steps(VALUES, TARGET)


def test_a_miss_walks_the_pointers_all_the_way_together():
    assert steps(VALUES, 99) == len(VALUES) - 1


def test_it_agrees_with_the_nested_loop_on_every_target():
    for t in range(0, 70):
        fast = find_pair(VALUES, t)
        slow = brute_force(VALUES, t)[0]
        assert (fast is None) == (slow is None), t
        if fast:
            assert VALUES[fast[0]] + VALUES[fast[1]] == t


def test_a_value_is_never_paired_with_itself():
    assert find_pair([4, 9], 8) is None


def test_edge_cases():
    assert find_pair([], 5) is None
    assert find_pair([5], 5) is None
    assert find_pair([2, 3], 5) == (0, 1)


if __name__ == '__main__':
    passed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print(f'  ok  {name}')
            passed += 1
    print(f'\n{passed} tests passed\n')
