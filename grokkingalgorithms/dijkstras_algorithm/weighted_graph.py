from dataclasses import dataclass
from typing import Any


@dataclass
class Vertice:
    quickest_path: int
    parent: str
    processed: bool
    

def quickest_path(graph: dict[str, dict[str, int]]) -> str:
    graph_vertices: dict[str, Vertice] = {}
    start_keys = graph['start'].keys()
    for key in start_keys:
        graph_vertices[key] = Vertice(processed=False, quickest_path=graph['start'][key], parent='start')
    
    quickest_unprocessed_vertice = ''
    
    while _quickest_unprocessed_vertice(graph_vertices) != 'fin':
        quickest_key = _quickest_unprocessed_vertice(graph_vertices)
        cost = graph_vertices[quickest_key].quickest_path
        neighbors = graph[quickest_key]
        
        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]
            
            if not graph_vertices.get(neighbor):
                graph_vertices[neighbor] = Vertice(quickest_path=new_cost, parent=quickest_unprocessed_vertice, processed=False)
            
            elif new_cost < graph_vertices.get(neighbor).quickest_path:
                graph_vertices[neighbor].quickest_path = new_cost
                graph_vertices[neighbor].parent = quickest_key
               
        graph_vertices[quickest_key].processed = True
        
    return _format(graph_vertices)
    
    
def _quickest_unprocessed_vertice(vertices: dict[str, Vertice]) -> str:
    quickest = ''
    
    for key in vertices.keys():
        if vertices[key].processed:
            continue
        
        if not quickest:
            quickest = key
        
        if vertices[key].quickest_path < vertices[quickest].quickest_path:
            quickest = key
        
    return quickest


def _format(vertices: dict[str, Vertice]) -> str:
    vertice = 'fin'
    formatted = 'fin'
    
    while vertices.get(vertice):
        parent = vertices[vertice].parent
        formatted = f'{parent} -> {formatted}'
        vertice = parent
        
    return formatted
        