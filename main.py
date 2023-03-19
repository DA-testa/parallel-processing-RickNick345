def parallel_processing(n, m, data):
    output = []
    threads = []
    for i in range(n):
        pair = [0,i]
        threads.append(pair)
    for x in range(m):
        nThread = min(threads)
        output.append((nThread[1], nThread[0]))
        t = data[x]
        nThread[0] = nThread[0] + t
    return output
    


def main():
    key = list(map(int, input().split()))
    n = key[0]
    m = key[1]
    # n - thread count 
    # m - job count
    data = list(map(int, input().split()))
    # data consist of time for each job 

    
            
    assert len(data) == m
    
    result = parallel_processing(n, m, data)
    for i, j in result:
        print(str(i) + " " + str(j))


if __name__ == "__main__":
    main()
