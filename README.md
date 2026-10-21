# Case Study 5: Dijkstra's Algorithm and Huffman Coding

## Unit V: Graph Algorithms and Data Compression

**Subject:** Data Structures and Algorithms  
**Language:** Python 3

## Aim
To implement Dijkstra's Shortest Path Algorithm and Huffman Coding to understand graph traversal and lossless data compression.

## Objectives
- Find shortest distances from a source vertex using Dijkstra's algorithm.
- Generate Huffman codes based on character frequencies.
- Understand weighted graphs and priority queues.
- Learn the basic concept of lossless compression.

## Theory

### 1. Dijkstra's Algorithm
Dijkstra's algorithm finds the shortest distances from a source vertex to other vertices in a weighted graph with non-negative edge weights.

It repeatedly processes the vertex with the smallest known distance and updates distances to its neighboring vertices.

### 2. Huffman Coding
Huffman Coding is a lossless compression technique. It assigns variable-length binary codes to characters based on their frequencies. More frequent characters generally receive shorter codes.

## Sample Output

```text
Shortest distances from A:
A to A = 0
A to B = 3
A to C = 1
A to D = 4
```

The program also displays Huffman codes for the characters in `hello`. The exact binary codes can vary when character frequencies tie.

## Complexity

**Dijkstra's Algorithm**
- Time complexity using a priority queue: `O((V + E) log V)` for a standard adjacency-list implementation.
- Space complexity: `O(V)` for distances and the priority queue, excluding graph storage.

**Huffman Coding**
- Time complexity: `O(k log k)` for building the Huffman tree, where `k` is the number of distinct characters.
- Space complexity: `O(k)` for the tree and code table, excluding the input text and output.

## Applications

- GPS navigation and route planning.
- Network routing.
- Lossless file compression.
- Efficient data transmission and storage.

## Technologies Used
- Python 3
- Graphs and priority queues
- Greedy algorithms
- Binary trees
- Frequency counting

## How to Run
```bash
python main.py
```

No external libraries are required.

## Conclusion
Dijkstra's algorithm calculates shortest distances in weighted graphs with non-negative weights. Huffman Coding generates variable-length binary codes for lossless compression. Both techniques are important applications of algorithmic problem-solving.
