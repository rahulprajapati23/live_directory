import heapq

def build_huffman_tree(chars, freqs):
    heap = []
    for c, f in zip(chars, freqs):
        heapq.heappush(heap, (f, c, None, None))
    while len(heap) > 1:
        f1, c1, l1, r1 = heapq.heappop(heap)
        f2, c2, l2, r2 = heapq.heappop(heap)
        new_node = (f1 + f2, None, (f1, c1, l1, r1), (f2, c2, l2, r2))
        heapq.heappush(heap, new_node)
    return heap[0]

def generate_codes(node, code="", codes=None):
    if codes is None:
        codes = {}
    freq, char, left, right = node
    if char is not None:
        codes[char] = code
        return codes
    generate_codes(left, code + "0", codes)
    generate_codes(right, code + "1", codes)
    return codes

def encode_text(text, codes):
    return "".join(codes[ch] for ch in text)

def decode_text(encoded, root):
    decoded = ""
    node = root
    for bit in encoded:
        freq, char, left, right = node
        node = left if bit == "0" else right
        f, c, l, r = node
        if c is not None:
            decoded += c
            node = root
    return decoded

characters = ['A', 'B', 'C', 'D', 'E', '-']
frequencies = [0.5, 0.35, 0.5, 0.1, 0.4, 0.2]

root = build_huffman_tree(characters, frequencies)
codes = generate_codes(root)
print("Huffman Codes:", codes)

text = "CAD-BE"
encoded = encode_text(text, codes)
print("Encoded:", encoded)

decoded = decode_text(encoded, root)
print("Decoded:", decoded)
