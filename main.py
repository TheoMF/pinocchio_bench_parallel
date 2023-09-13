import matplotlib.pyplot as plt

def plot_results(results_file_name):
    file_name_prefix = results_file_name.split(".")[0]
    algo_name = file_name_prefix.split("_")[1]
    with open(results_file_name) as f:
        initial_val = float(f.readline())
        threads = ["1"]
        executions_time = [initial_val]
        expected_executions_time = [initial_val]
        executions_time_times_nb_threads = [initial_val]
        for nb_threads in range(2,21):
            execution_time = float(f.readline())
            threads.append(str(nb_threads))
            executions_time.append(execution_time)
            expected_executions_time.append(initial_val/nb_threads)
            executions_time_times_nb_threads.append(execution_time*nb_threads)

        #plot executions_time and expected_executions_time
        plt.clf()
        plt.bar(threads, executions_time,label="execution time", color="g")
        plt.bar(threads, expected_executions_time,label="expected execution time",color="b")
        plt.ylabel("execution time (us)")
        plt.xlabel("number of threads")
        plt.legend()
        plt.title("execution time with pool for "+algo_name)
        plt.ylim([0,initial_val+0.5])
        plt.savefig("execution_time_"+file_name_prefix+".png")

        #plot executions_time*nb_threads
        plt.clf()
        plt.bar(threads, executions_time_times_nb_threads,color="g")
        plt.ylabel("execution time*number of threads")
        plt.xlabel("number of threads")
        plt.title("execution time*number of threads for "+algo_name)
        plt.savefig("execution_time*nb_threads_"+file_name_prefix+".png")

if __name__=="__main__":
    plot_results("ibukidake_rnea.txt")
    plot_results("ibukidake_aba.txt")
