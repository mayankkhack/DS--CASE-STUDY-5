
import heapq
from collections import Counter
import heapq as hq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)

        if distance > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(
                    priority_queue, (new_distance, neighbor)
                )

    return distances


class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def huffman_coding(text):
    if not text:
        return {}

    frequencies = Counter(text)
    heap = [
        HuffmanNode(char, freq)
        for char, freq in frequencies.items()
    ]
    hq.heapify(heap)

    if len(heap) == 1:
        return {heap[0].char: "0"}

    while len(heap) > 1:
        left = hq.heappop(heap)
        right = hq.heappop(heap)

        merged = HuffmanNode(
            None, left.frequency + right.frequency
        )
        merged.left = left
        merged.right = right

        hq.heappush(heap, merged)

    root = heap[0]
    codes = {}

    def generate_codes(node, code):
        if node.char is not None:
            codes[node.char] = code
            return

        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    generate_codes(root, "")
    return codes


def main():
    graph = {
        "A": [("B", 4), ("C", 1)],
        "B": [("A", 4), ("C", 2), ("D", 1)],
        "C": [("A", 1), ("B", 2), ("D", 5)],
        "D": [("B", 1), ("C", 5)]
    }

    print("Shortest distances from A:")
    distances = dijkstra(graph, "A")

    for node, distance in distances.items():
        print("A to", node, "=", distance)

    text = "hello"
    codes = huffman_coding(text)

    print("\nHuffman Codes:")
    for char, code in sorted(codes.items()):
        print(repr(char), ":", code)


if __name__ == "__main__":
    main()
