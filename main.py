from mpi4py import MPI
import sys

from worker_process import WorkerProcess
from master_process import MasterProcess


def main():
    comm = MPI.COMM_WORLD
    proc_id = comm.Get_rank()
    proc_count = comm.Get_size()
    input_path = sys.argv[1] if len(sys.argv) > 1 else 'data.dat'
    vertex_count = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    if proc_id == 0:
        process = MasterProcess(comm, vertex_count, proc_count, input_path)
        process.read_data()
        process.initialize_random_result()
        print(process.graph)
        print(process.result)
        print(process.score_result(process.result))
    else:
        process = WorkerProcess(comm, vertex_count)

    comm.Bcast(process.graph, root=0)


main()
