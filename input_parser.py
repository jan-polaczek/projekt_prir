import numpy as np
import math


class InputParser:
    def __init__(self, path):
        self.path = path
        self.vertices = []
        self.edges = None

    def parse(self):
        with open(self.path, 'r') as f:
            self.process_file(f)
        return self.edges, self.vertices
    
    def process_file(self, f):
        self.vertices = f.readline().split()
        n = len(self.vertices)
        self.edges = np.zeros((n, n), dtype='i')
        while True:
            line = f.readline()
            if not line:
                break
            self.process_line(line)
    
    def process_line(self, line):
        edge = line.split()
        v1 = self.get_index_from_vertex_name(edge[0])
        v2 = self.get_index_from_vertex_name(edge[1])
        self.edges[v1][v2] = self.edges[v2][v1] = int(edge[2])

    def get_index_from_vertex_name(self, v):
        return self.vertices.index(v)
