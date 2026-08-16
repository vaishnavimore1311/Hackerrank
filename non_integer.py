#QUE.1 The provided code stub reads an integer, n , from STDIN. For all non-negative integers i<n , print i*i 

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n):
        print(i * i)