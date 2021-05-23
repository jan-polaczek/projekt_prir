from worker_process import WorkerProcess
from input_parser import InputParser
import random


class MasterProcess(WorkerProcess):
    def __init__(self, comm, vertex_count, proc_count, input_path):
        super().__init__(comm, vertex_count)
        self.proc_count = proc_count
        self.input_path = input_path
        self.vertex_count = vertex_count

    def read_data(self):
        input_parser = InputParser(self.input_path)
        self.graph = input_parser.parse()

    def initialize_random_result(self):
        not_chosen = set([i for i in range(self.vertex_count)])
        for i in range(self.vertex_count):
            v = random.choice(list(not_chosen))
            not_chosen.remove(v)
            self.result.append(v)
        self.result.append(self.result[0])

    def score_result(self, result):
        score = 0
        for i in range(len(result) - 1):
            v1 = result[i]
            v2 = result[i + 1]
            score += self.graph[v1][v2]
        return score
