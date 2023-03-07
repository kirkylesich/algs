import heapq
from collections import defaultdict

def huffman_encode(s):
    freq = defaultdict(int)
    for c in s:
        freq[c] += 1

    heap = [[f, [c, ""]] for c, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huffman_dict = dict(sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))
    encoded = ''.join(huffman_dict[c] for c in s)
    avg_length = sum(len(huffman_dict[c]) * freq[c] for c in freq) / len(s)

    return avg_length


print("{:.6f}".format(huffman_encode(input())))