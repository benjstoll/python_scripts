import threading
import time


def task(counter):
    time.sleep(5)
    print(f"Finished up step {counter}")



def main():

    start_time = time.time()
    thread_pool = 8
    task_counter = 0
    threads=[]

    while task_counter < 16:
        if threading.active_count() <= thread_pool:
            thread = threading.Thread(target=task,args=(task_counter,))
            threads.append(thread)
            task_counter += 1
            thread.start()
                    
    for thread in threads:
        thread.join()

    end_time = time.time() - start_time
    print(end_time)

if __name__ == "__main__":
    main()

else:
    print("Please run this module as main.")