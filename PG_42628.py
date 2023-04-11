import heapq


def solution(operations):
    heap = []

    for o in operations:
        if o[:1] == 'I':
            heapq.heappush(heap, int(o[2:]))
        elif o[:1] == 'D' and heap:
            if o[2:] == '-1':
                heapq.heappop(heap)
            elif o[2:] == '1':
                idx = heap.index(max(heap))
                heap.pop(idx)

    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]
