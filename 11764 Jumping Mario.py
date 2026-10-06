T = int(input())
Case = 0
for i in range(T):
    N = list(map(int,input().split()))
    Case += 1
    wall = list(map(int,input().split()))
    high_j = 0
    low_j = 0
    for i in range(len(wall)-1):
        if wall[i] > wall[i+1]:
            low_j += 1
        elif  wall[i] < wall[i+1]:
            high_j += 1
    print(f'Case {Case}: {high_j} {low_j}')
