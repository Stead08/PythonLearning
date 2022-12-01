def bubble_sort(a, n):
    for i in range(0, n - 1):
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]

        print(*a)


n = int(input())
a = list(map(int, input().split()))

bubble_sort(a, n)
