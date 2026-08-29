# Two Pointers

**O(n)** · [Watch the reel](https://www.facebook.com/reel/1755801325456117)

The working code from the [@ByteAnimates](https://www.facebook.com/ByteAnimates) reel.

```bash
python3 two_pointers.py
python3 main.py
```

No dependencies. Python 3.9+.

### `two_pointers.py`

```python
def find_pair(a, target):
    i, j = 0, len(a) - 1
    while i < j:
        s = a[i] + a[j]
        if s == target:
            return i, j
        if s < target:
            i += 1
        else:
            j -= 1
    return None
```

### Files

| | |
| --- | --- |
| `main.py` | run this — the demo, with real inputs and the claims asserted |
| `two_pointers.py` | the reel snippet, generated from the episode |

---

The snippet above is generated from the video itself — what you read is byte-for-byte
what was typed on screen. A fix to it belongs in the episode, so open an issue and the
next reel carries it. Everything else here is hand-written and welcome as a pull request.
