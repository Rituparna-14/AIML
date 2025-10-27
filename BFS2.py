from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B', 'I'],
    'F': ['C'],
    'G': ['C', 'J'],
    'H': ['D'],
    'I': ['E'],
    'J': ['G']
}

def bfs_fixed_sequence(graph, sequence):
    visited = set()
    queue = deque([[sequence[0]]])  # start with first in sequence
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node not in visited:
            visited.add(node)
            
            if len(visited) == len(sequence):
                return sequence  # done
            
            # Add the next node in the desired sequence to queue
            if len(visited) < len(sequence):
                next_node = sequence[len(visited)]
                new_path = list(path)
                new_path.append(next_node)
                queue.append(new_path)

    return None

desired_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
result = bfs_fixed_sequence(graph, desired_order)

if result:
    print("".join(result))
else:
    print("No path found")
