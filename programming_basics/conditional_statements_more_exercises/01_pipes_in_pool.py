pool_volume_V = int(input())
first_pipe_debit_P1 = int(input())
second_pipe_debit_P2 = int(input())
hours_worker_absent_H = float(input())

volume_filled_by_P1 = hours_worker_absent_H * first_pipe_debit_P1
volume_filled_by_P2 = hours_worker_absent_H * second_pipe_debit_P2
volume_filled_total = volume_filled_by_P1 + volume_filled_by_P2
percentage_of_pool_filled = volume_filled_total / pool_volume_V * 100

if percentage_of_pool_filled <= 100:
    print (f"The pool is {percentage_of_pool_filled}% full."
        f"Pipe 1: {volume_filled_by_P1 / volume_filled_total * 100}%."
        f"Pipe 2: {volume_filled_by_P2 / volume_filled_total * 100}%.")
else:
    print(f"For {hours_worker_absent_H} hours"
        f"the pool overflows with {volume_filled_total - pool_volume_V} liters.")