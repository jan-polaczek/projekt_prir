from mpi4py import MPI
import sys
from math import inf
import numpy as np

from worker_process import WorkerProcess
from master_process import MasterProcess

MIN_IMPROVEMENT = 1
MIN_ITER = 1
MAX_ITER = 10000


def main():
    comm = MPI.COMM_WORLD
    proc_id = comm.Get_rank()
    proc_count = comm.Get_size()
    input_path = sys.argv[1] if len(sys.argv) > 1 else 'data.dat'
    vertex_count = int(sys.argv[2]) if len(sys.argv) > 2 else 50

    if proc_id == 0:
        process = MasterProcess(comm, vertex_count, proc_count, input_path)
        process.read_data()
        process.initialize_random_result()
        print(process.graph)
    else:
        process = WorkerProcess(comm, vertex_count)

    comm.Bcast(process.graph, root=0)
    process.result = comm.bcast(process.result, root=0)

    improvement = inf
    i = 0
    best_score = 0
    while (improvement < 0 or improvement > MIN_IMPROVEMENT) and i < MAX_ITER or i < MIN_ITER:
        best_result = None
        process.work()
        all_results = comm.gather(process.result, root=0)
        if proc_id == 0:
            scores = [process.score_result(result) for result in all_results]
            improvement = best_score - min(scores)
            best_score = min(scores)
            best_score_idx = scores.index(best_score)
            best_result = all_results[best_score_idx]
            #print(improvement)
        process.result = comm.bcast(best_result, root=0)
        improvement = comm.bcast(improvement, root=0)
        i += 1

    if proc_id == 0:
        print(f'Best path: {process.print_result()}, length: {best_score}, calculated in {i} iterations')


main()
