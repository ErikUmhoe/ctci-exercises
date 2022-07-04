# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version > 5:
        return True
    return False

def firstBadVersion(n: int) -> int:
    return _isBadHelper(0, n)

def _isBadHelper(start, end):
    mid = ((end - start) // 2) + start
    midBad = isBadVersion(mid)
    if midBad:
        if not isBadVersion(mid - 1):
            return mid-1
        else:
            return _isBadHelper(start, mid)
    else:
        if isBadVersion(mid + 1):
            return mid
        else:
            return _isBadHelper(mid, end)
    
n = 15
print(firstBadVersion(n))
