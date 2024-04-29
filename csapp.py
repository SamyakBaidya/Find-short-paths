from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample graph data (you can replace this with your own data)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def dijkstra(graph, start, end):
    # Initialization
    shortest_distance = {node: float('inf') for node in graph}
    shortest_distance[start] = 0
    visited = set()

    while True:
        # Find the node with the shortest distance
        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None or shortest_distance[node] < shortest_distance[min_node]:
                    min_node = node

        if min_node is None:
            break

        # Update shortest distances
        for neighbor, distance in graph[min_node].items():
            if shortest_distance[min_node] + distance < shortest_distance[neighbor]:
                shortest_distance[neighbor] = shortest_distance[min_node] + distance

        visited.add(min_node)

    return shortest_distance[end]

@app.route('/shortest-path', methods=['POST'])
def shortest_path():
    data = request.get_json()
    start = data['start']
    end = data['end']
    shortest_distance = dijkstra(graph, start, end)
    return jsonify({'shortest_distance': shortest_distance})

if __name__ == '__main__':
    app.run(debug=True)
