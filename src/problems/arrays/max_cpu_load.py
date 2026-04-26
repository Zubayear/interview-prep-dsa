class Endpoint:
    def __init__(self, s, l, is_start):
        self.start, self.load, self.is_start = s, l, is_start

    def __lt__(self, other):
        if self.start != other.start:
            return self.start < other.start
        return self.is_start and not other.is_start


def max_cpu_load(arr):
    endpoints = []
    for start, end, load in arr:
        endpoints.append(Endpoint(start, load, True))
        endpoints.append(Endpoint(end, load, False))
    endpoints.sort()
    count, result = 0, 0
    for endpoint in endpoints:
        if endpoint.is_start:
            count += endpoint.load
            result = max(result, count)
        else:
            count -= endpoint.load
    return result
