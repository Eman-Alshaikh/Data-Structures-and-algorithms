from platform import node
from cd_graph.stack_and_queue import Node,Queue


class Graph:
    def __init__(self):
        self._adjacency_list={}

    
    def add_node(self,value):
        new_vertex=Vertex(value)
        self._adjacency_list[new_vertex]=[]
        return new_vertex

    def add_edge(self,start_vertex,end_vertex,weight=1):
        if start_vertex not in self._adjacency_list:
            raise KeyError('start vertex not in graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('end vertex not in graph ')
        
        new_edge=Edge(end_vertex,weight)
        adjancencies=self._adjacency_list[start_vertex]
        adjancencies.append(new_edge)

    def get_nodes(self):
        return None if not self._adjacency_list else [node.value for node in self._adjacency_list]

    def get_neighbors(self,vertex):
        if vertex not in self._adjacency_list:
            raise KeyError('vertex not in graph')
        return [{'Value': neighbor.vertex.value,'Weight':neighbor.weight} for neighbor in self._adjacency_list[vertex]]

    def size(self):
        return len(self._adjacency_list)

    def breadth_first(self,origin_vertex):
        visited_vertices=[]
        vertex_queue=Queue()
        vertex_queue.enqueue(Graph.vertex_converter(self,origin_vertex))
        

        j=0
        while j< self.size()+1:
            vertex=vertex_queue.dequeue()
            if vertex.value not in visited_vertices:
                visited_vertices.append(vertex.value)
                for neighbor in self._adjacency_list[vertex]:
                    vertex_queue.enqueue(neighbor.vertex)
            j+=1
        return visited_vertices

    def depth_first(self,origin_vertex):
        visited_vertices=[]
        known_neighbors=[]
        origin_vertex=Graph.vertex_convertor(self,origin_vertex)


        def traverse(vertex):
            visited_vertices.append(vertex.value)
            for i in self._adjacency_list[vertex]:
                if i.vertex not in known_neighbors and i.vertex.value not in visited_vertices:
                    known_neighbors.append(i.vertex)
                    traverse(i.vertex)
                    known_neighbors.pop(-1)

        traverse(origin_vertex)
        return visited_vertices

    @staticmethod
    def vertex_converter(self,selected_value):
        i=0
        for vertex in self._adjacency_list:
            if vertex.value==selected_value:
                return vertex
            i+=1
            if i==self.size():
                raise KeyError('the vertex is not in graph')


class Vertex:
    def __init__(self,value)  :
        self.value=value

    def __str__(self) :
        return self.value

class Edge:
    def __init__(self,vertex,weight=1)  :
        self.vertex=vertex
        self.weight=weight
        
    
