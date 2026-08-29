# Two Pointers — O(n)
# As shown in the reel: https://www.facebook.com/reel/1755801325456117
# Generated from the episode; edits here are overwritten. See the README.

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
