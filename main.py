import matplotlib.pyplot as plt
import json


def plot_results(nb_max_threads, values, machine_name, algo_name, figsize):
    initial_val = values[0]
    threads = []
    executions_time = []
    expected_executions_time = []
    executions_time_times_nb_threads = []
    for nb_threads in range(1, nb_max_threads + 1):
        execution_time = values[nb_threads - 1]
        threads.append(str(nb_threads))
        executions_time.append(execution_time)
        expected_executions_time.append(initial_val / nb_threads)
        executions_time_times_nb_threads.append(execution_time * nb_threads)

    # plot executions_time and expected_executions_time
    plt.clf()
    plt.figure(figsize=figsize)
    plt.bar(
        threads,
        executions_time,
        label="execution time",
        width=0.6,
        color="g",
    )
    plt.bar(
        threads,
        expected_executions_time,
        label="expected execution time",
        width=0.6,
        color="b",
    )
    plt.ylabel("execution time (us)")
    plt.xlabel("number of threads")
    plt.legend()
    plt.title(
        "execution time with pool for " + algo_name + " with machine " + machine_name
    )

    plt.ylim([0, initial_val + 0.5])
    plt.savefig(machine_name + "_" + algo_name + "_execution_time.png")

    # plot executions_time*nb_threads
    plt.clf()
    plt.figure(figsize=figsize)
    plt.bar(
        threads,
        executions_time_times_nb_threads,
        width=0.6,
        color="g",
    )
    plt.ylabel("execution time*number of threads")
    plt.xlabel("number of threads")

    plt.title(
        "execution time*number of threads for "
        + algo_name
        + " with machine "
        + machine_name
    )
    plt.savefig(machine_name + "_" + algo_name + "_execution_time*nb_threads.png")


if __name__ == "__main__":
    with open("askew.json") as f:
        data = json.load(f)
        nb_max_threads = data["nb_max_threads"]
        plot_results(nb_max_threads, data["rnea"], "askew", "rnea", (10, 6))
        plot_results(nb_max_threads, data["aba"], "askew", "aba", (10, 6))
    with open("ibukidake.json") as f:
        data = json.load(f)
        nb_max_threads = data["nb_max_threads"]
        plot_results(nb_max_threads, data["aba"], "ibukidake", "aba", (10, 6))
        plot_results(nb_max_threads, data["rnea"], "ibukidake", "rnea", (10, 6))
    with open("pirovano.json") as f:
        data = json.load(f)
        nb_max_threads = data["nb_max_threads"]
        plot_results(nb_max_threads, data["rnea"], "pirovano", "rnea", (20, 6))
        plot_results(nb_max_threads, data["aba"], "pirovano", "aba", (20, 6))
