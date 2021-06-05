import numpy as np
import math
import random

TRIES_PER_ITERATION = 3


class WorkerProcess:
    def __init__(self, comm, vertex_count):
        self.comm = comm
        self.graph = np.full([vertex_count, vertex_count], math.inf, dtype='i')
        self.result = []
        self.temperature = 5
        self.cooling_factor = 0.99

    def work(self):
        for i in range(TRIES_PER_ITERATION):
            new_result = self.roll_new_result()
            if self.accept_new_result(new_result):
                self.result = new_result
        self.temperature *= self.cooling_factor

    def accept_new_result(self, new_result):
        current_score = self.score_result(self.result)
        new_score = self.score_result(new_result)
        if new_score <= current_score or self.accept_worse_result(current_score, new_score):
            return True

    def accept_worse_result(self, current_score, new_score):
        d_score = current_score - new_score
        prob = math.exp(d_score / self.temperature)
        rand = random.random()
        #print(f'Current score: {current_score}, new score: {new_score}, probability: {prob}')
        return rand <= prob

    def roll_new_result(self):
        idx = random.randint(1, len(self.result) - 2)
        new_idx = random.randint(1, len(self.result) - 2)
        new_result = self.result.copy()
        val = new_result.pop(idx)
        new_result.insert(new_idx, val)
        return new_result

    def score_result(self, result):
        score = 0
        for i in range(len(result) - 1):
            v1 = result[i]
            v2 = result[i + 1]
            score += self.graph[v1][v2]
        return score
