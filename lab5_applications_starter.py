"""DSA S1 - G1 session 3 - Lab 5: sorting in use (records, duplicates, pairs, inversions).

Run the tests:  python test_lab5.py      Run the timings:  python lab5_applications_starter.py
Uses only what we have seen: loops, recursion, insertion / bubble / merge sort, sets as a black box.
Fill in every TODO. Do not call sorted() or list.sort() in Tasks 1 to 4: use merge_sort / merge_sort_key.
"""
import random
import timeit


# ---------------------------------------------------------------------------
# Given: the merge sort of Lab 4 (stable, returns a NEW list). Do not edit.
# ---------------------------------------------------------------------------
def merge_sort(a):
    if len(a) <= 1:
        return list(a)
    mid = len(a) // 2
    left, right = merge_sort(a[:mid]), merge_sort(a[mid:])
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out


# ---------------------------------------------------------------------------
# Task 1: sort records by one or several keys
# A record is a tuple (city, name, age).
# ---------------------------------------------------------------------------
def merge_sort_key(a, key):
    """Task 1a: like merge_sort, but compare key(x) instead of x. Return a NEW list, stable.

    Example: merge_sort_key(["bb", "a", "ccc"], key=len) == ["a", "bb", "ccc"]
    Hint: copy merge_sort and replace each comparison of two items by a comparison of their keys.
    Keep the <= so that equal keys stay in their original order.
    """
    # TODO
    raise NotImplementedError


def sort_two_passes(records):
    """Task 1b: sort by city, then by name inside each city, using TWO stable passes of merge_sort_key.

    Think about the ORDER of the passes: which key must be sorted first?
    """
    # TODO
    raise NotImplementedError


def sort_one_pass(records):
    """Task 1c: the same result with ONE pass, using a key that returns a tuple."""
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Task 2: does a list contain a duplicate? Three ways, three costs.
# ---------------------------------------------------------------------------
def has_dup_nested(a):
    """Task 2a: compare every pair with two nested loops. Cost: ?"""
    # TODO
    raise NotImplementedError


def has_dup_sort(a):
    """Task 2b: sort a COPY with merge_sort, then compare neighbours. Do not modify `a`. Cost: ?"""
    # TODO
    raise NotImplementedError


def has_dup_set(a):
    """Task 2c: one pass, remembering the items already seen in a set. Cost: ?"""
    # TODO
    raise NotImplementedError


def dup_timings(sizes=(1000, 2000, 4000, 8000)):
    """Task 2d: print a table of times (ms) for the three versions on lists WITHOUT duplicates (worst case).

    Then write down the doubling ratio of each column.
    """
    print(f"{'n':>7} {'nested':>9} {'sort':>8} {'set':>8}")
    for n in sizes:
        a = random.sample(range(10 * n), n)   # n distinct values
        t_nested = min(timeit.timeit(lambda: has_dup_nested(a), number=1) for _ in range(2))
        # TODO: time has_dup_sort and has_dup_set in the same way
        print(f"{n:>7} {t_nested * 1000:>9.1f}  ...")


# ---------------------------------------------------------------------------
# Task 3: is there a pair of items (at two different positions) with a given sum?
# ---------------------------------------------------------------------------
def has_pair_brute(a, target):
    """Task 3a: two nested loops over positions i < j. Cost: ?"""
    # TODO
    raise NotImplementedError


def has_pair_sorted(a, target):
    """Task 3b: sort a COPY with merge_sort, then walk two indices lo (start) and hi (end) towards each other.

    If a[lo] + a[hi] is too small move lo right, if too large move hi left. Cost: ?
    """
    # TODO
    raise NotImplementedError


def has_pair_set(a, target):
    """Task 3c (stretch): one pass with a set of the items already seen. Cost: ?"""
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Task 4 (stretch): count inversions with divide and conquer.
# An inversion is a pair of positions i < j with a[i] > a[j].  [3, 1, 2] has 2 inversions.
# ---------------------------------------------------------------------------
def insertion_shift_count(a):
    """Given: run insertion sort on a COPY of a and return the number of shifts it makes."""
    a = list(a)
    shifts = 0
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = x
    return shifts


def count_inversions(a):
    """Task 4: return the number of inversions of a in O(n log n). Do not modify `a`.

    Idea: split in two halves, count the inversions inside each half recursively, then count the
    inversions BETWEEN the halves during the merge. When you take an item from the right half, every
    item still waiting in the left half is larger than it: that is len(left) - i inversions.
    Hint: write a helper that returns (sorted_list, number_of_inversions).
    """
    # TODO
    raise NotImplementedError


if __name__ == "__main__":
    dup_timings()
