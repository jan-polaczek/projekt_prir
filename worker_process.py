import numpy as np
import math


class WorkerProcess:
    def __init__(self, comm, vertex_count):
        self.comm = comm
        self.graph = np.full([vertex_count, vertex_count], math.inf, dtype='i')
        self.result = []

    def work(self):
        pass    # tu będziemy liczyć
