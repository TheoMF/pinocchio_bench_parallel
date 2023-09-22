import matplotlib.pyplot as plt
import json
from subprocess import check_call


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
    plt.bar(threads, executions_time, label="execution time", color="g")
    plt.bar(
        threads, expected_executions_time, label="expected execution time", color="b"
    )
    plt.ylabel("execution time (us)")
    plt.xlabel("number of threads")
    plt.legend()
    plt.title(
        "execution time with pool for " + algo_name + " with machine " + machine_name
    )

    plt.ylim([0, initial_val + 0.5])
    file_name = machine_name + "_" + algo_name + "_execution_time.png"
    plt.savefig(file_name)
    check_call(["mv", file_name, "plots/" + machine_name])
    plt.close()

    # plot executions_time*nb_threads
    plt.clf()
    plt.figure(figsize=figsize)
    plt.bar(threads, executions_time_times_nb_threads, color="g")
    plt.ylabel("execution time*number of threads")
    plt.xlabel("number of threads")

    plt.title(
        "execution time*number of threads for "
        + algo_name
        + " with machine "
        + machine_name
    )
    file_name = machine_name + "_" + algo_name + "_execution_time*nb_threads.png"
    plt.savefig(file_name)
    check_call(["mv", file_name, "plots/" + machine_name])
    plt.close()


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
        plot_results(nb_max_threads, data["rnea_2"], "pirovano", "rnea_2", (20, 6))
        plot_results(nb_max_threads, data["aba_2"], "pirovano", "aba_2", (20, 6))
