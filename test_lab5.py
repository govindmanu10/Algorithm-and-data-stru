"""Tests for Lab 5. Run: python test_lab5.py [module]  (default lab5_applications_starter)"""
import importlib, sys, random, time

mod = importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else "lab5_applications_starter")
passed = failed = 0


def check(name, fn):
    global passed, failed
    try:
        fn(); print("ok    ", name); passed += 1
    except NotImplementedError:
        print("TODO  ", name); failed += 1
    except AssertionError as e:
        print("FAIL  ", name, e); failed += 1
    except Exception as e:
        print("ERROR ", name, type(e).__name__, e); failed += 1


CITIES = ["Rabat", "Fes", "Agadir", "Oujda"]
NAMES = ["Amal", "Bilal", "Chaima", "Driss", "Esma", "Farid"]


def records(n):
    return [(random.choice(CITIES), random.choice(NAMES), i) for i in range(n)]   # i = original position


def t_key():
    assert mod.merge_sort_key(["bb", "a", "ccc"], key=len) == ["a", "bb", "ccc"]
    assert mod.merge_sort_key([], key=len) == []
    for _ in range(50):
        a = [random.randrange(-20, 20) for _ in range(random.randrange(0, 40))]
        orig = a[:]
        assert mod.merge_sort_key(a, key=lambda x: -x) == sorted(a, key=lambda x: -x)
        assert a == orig, "merge_sort_key must not change its input"


def t_key_stable():
    r = records(200)
    out = mod.merge_sort_key(r, key=lambda x: x[0])
    assert out == sorted(r, key=lambda x: x[0]), "equal keys must keep their original order (use <=)"


def t_two():
    for _ in range(20):
        r = records(random.randrange(0, 80))
        assert mod.sort_two_passes(r) == sorted(r, key=lambda x: (x[0], x[1]))


def t_one():
    for _ in range(20):
        r = records(random.randrange(0, 80))
        assert mod.sort_one_pass(r) == sorted(r, key=lambda x: (x[0], x[1]))


def dup_cases():
    yield [], False
    yield [1], False
    yield [1, 1], True
    yield [1, 2, 3, 4], False
    yield [4, 3, 2, 1, 4], True
    for _ in range(100):
        a = [random.randrange(30) for _ in range(random.randrange(0, 25))]
        yield a, len(set(a)) < len(a)


def make_dup_test(f):
    def t():
        for a, expected in dup_cases():
            orig = a[:]
            assert getattr(mod, f)(a) is expected, (f, a)
            assert a == orig, f"{f} must not change its input"
    return t


def pair_cases():
    yield [], 0, False
    yield [3], 6, False
    yield [3, 3], 6, True
    yield [1, 2, 3], 5, True
    yield [1, 2, 3], 7, False
    yield [-5, 5], 0, True
    for _ in range(200):
        a = [random.randrange(-15, 15) for _ in range(random.randrange(0, 12))]
        t = random.randrange(-20, 20)
        yield a, t, any(a[i] + a[j] == t for i in range(len(a)) for j in range(i + 1, len(a)))


def make_pair_test(f):
    def t():
        for a, target, expected in pair_cases():
            orig = a[:]
            assert getattr(mod, f)(a, target) is expected, (f, a, target)
            assert a == orig, f"{f} must not change its input"
    return t


def t_fast_pair():
    a = random.sample(range(10 ** 7), 100000)
    start = time.perf_counter()
    mod.has_pair_sorted(a, -1)
    assert time.perf_counter() - start < 5, "has_pair_sorted on 100 000 items took more than 5 s: is it really n log n?"


def t_inv_small():
    assert mod.count_inversions([]) == 0
    assert mod.count_inversions([1, 2, 3]) == 0
    assert mod.count_inversions([3, 2, 1]) == 3
    assert mod.count_inversions([3, 1, 2]) == 2
    for _ in range(100):
        a = [random.randrange(15) for _ in range(random.randrange(0, 30))]
        orig = a[:]
        assert mod.count_inversions(a) == mod.insertion_shift_count(a), a
        assert a == orig


def t_inv_fast():
    a = random.sample(range(10 ** 7), 100000)
    start = time.perf_counter()
    mod.count_inversions(a)
    assert time.perf_counter() - start < 5, "count_inversions on 100 000 items took more than 5 s: it must be n log n"


for name, fn in [("merge_sort_key", t_key), ("merge_sort_key is stable", t_key_stable),
                 ("sort_two_passes", t_two), ("sort_one_pass", t_one),
                 ("has_dup_nested", make_dup_test("has_dup_nested")),
                 ("has_dup_sort", make_dup_test("has_dup_sort")),
                 ("has_dup_set", make_dup_test("has_dup_set")),
                 ("has_pair_brute", make_pair_test("has_pair_brute")),
                 ("has_pair_sorted", make_pair_test("has_pair_sorted")),
                 ("has_pair_sorted on 100 000 items", t_fast_pair),
                 ("[stretch] has_pair_set", make_pair_test("has_pair_set")),
                 ("[stretch] count_inversions (equals insertion shifts)", t_inv_small),
                 ("[stretch] count_inversions on 100 000 items", t_inv_fast)]:
    check(name, fn)
print(f"\n{passed} passed, {failed} not yet")
