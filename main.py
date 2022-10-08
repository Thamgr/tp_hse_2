def _min(_array):
    ans = _array[0]
    for e in _array:
        ans = min(ans, e)
    return ans

def _max(_array):
    ans = _array[0]
    for e in _array:
        ans = max(ans, e)
    return ans

def _sum(_array):
    ans = 0
    for e in _array:
        ans += e
    return ans

def _mul(_array):
    ans = 1
    for e in _array:
        ans *= e
    return ans

def read_file(path):
    ans = []
    with open(path, 'r') as file:
        for line in file:
            ans += list(map(int, line.split()))
    return ans