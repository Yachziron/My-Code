def find_min_scans(n, L, coordinates):
    scans = 0
    current_position = coordinates[0]

    for i in range(1, n):
        if coordinates[i] > current_position + L:
            scans += 1
            current_position = coordinates[i]

    return scans + 1

n, L = map(int, input().split())
coordinates = list(map(int, input().split()))

result = find_min_scans(n, L, coordinates)
print(result)
