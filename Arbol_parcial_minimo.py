import heapq
import matplotlib.pyplot as plt
import networkx as nx

def prim_minimum_spanning_tree(graph):
    # Nodo inicial
    start_node = list(graph.keys())[0]
    visited = set([start_node])
    min_heap = [(weight, start_node, dest) for weight, dest in graph[start_node]]
    heapq.heapify(min_heap)
    
    mst_edges = []  
    total_weight = 0  
    
    step = 1
    print("Simulación del Árbol Parcial Mínimo (APM) de Prim:")
    while min_heap and len(visited) < len(graph):
        weight, frm, to = heapq.heappop(min_heap)
        
        if to not in visited:
            visited.add(to)
            mst_edges.append((frm, to, weight))
            total_weight += weight
            print(f"Paso {step}: Agregando arista ({frm}, {to}) con peso {weight}")
            step += 1
            
            for next_weight, next_to in graph[to]:
                if next_to not in visited:
                    heapq.heappush(min_heap, (next_weight, to, next_to))

    print(f"\nPeso total del Árbol Parcial Mínimo: {total_weight}")
    return mst_edges, total_weight

def draw_graph(graph, mst_edges, filename="prim_mst.jpg"):
    G = nx.Graph()
    
    for node, edges in graph.items():
        for weight, to in edges:
            G.add_edge(node, to, weight=weight)

    pos = nx.spring_layout(G)  
    plt.figure(figsize=(10, 8))
    
    nx.draw_networkx(G, pos, edge_color='gray', node_size=700, font_size=14, font_color='white', node_color='blue')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    mst_G = nx.Graph()
    mst_G.add_edges_from([(frm, to) for frm, to, weight in mst_edges])
    nx.draw_networkx_edges(G, pos, edgelist=mst_G.edges(), edge_color='red', width=2)
    
    plt.title("Árbol Parcial Mínimo usando el algoritmo de Prim")
    plt.savefig(filename)
    plt.show()
    print(f"Gráfica guardada como {filename}")

# Ejemplo de uso
graph = {
    'A': [(1, 'B'), (3, 'C')],
    'B': [(1, 'A'), (2, 'C'), (4, 'D')],
    'C': [(3, 'A'), (2, 'B'), (5, 'D')],
    'D': [(4, 'B'), (5, 'C')]
}

# Ejecutar el simulador
mst_edges, total_weight = prim_minimum_spanning_tree(graph)
draw_graph(graph, mst_edges, filename="prim_mst.jpg")