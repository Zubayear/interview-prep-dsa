class Endpoint:
    def __init__(self, s, l, isStart):
        self.start, self.load, self.isStart = s, l, isStart

    def __lt__(self, other):
        if self.start != other.start:
            return self.start < other.start
        return self.isStart and not other.isStart


def max_cpu_load(arr):
    endpoints = []
    for start, end, load in arr:
        endpoints.append(Endpoint(start, load, True))
        endpoints.append(Endpoint(end, load, False))
    endpoints.sort()
    count, result = 0, 0
    for endpoint in endpoints:
        if endpoint.isStart:
            count += endpoint.load
            result = max(result, count)
        else:
            count -= endpoint.load
    return result
