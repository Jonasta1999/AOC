from itertools import chain

with open("/Users/jonasahooei/Library/CloudStorage/GoogleDrive-jonasahooei@gmail.com/Mit drev/Advent_of_code/2023/input5.txt") as f:
    data = f.read().split("\n\n")

data = [section.splitlines() for section in data]

n = len(data)

for i in range(n):
    m = len(data[i])

    for j in range(m):
        if i == 0:
            data[i] = data[i][0].split(":")
            data[i] = data[i][1]

for i in range(n):
    if i == 0:
        continue
    else:
        data[i] = data[i][1:]

seeds = data[0].split()
map = data[1:]

seeds = data[0].split()
map = data[1:]

n = len(seeds)
m = len(map)

seeds_new = []
print(n)

for i in range(0, n, 2):
    print(i)
    start = int(seeds[i])
    end = int(seeds[i]) + int(seeds[i+1])

    seeds_new.append(list(range(start, end)))
seeds = list(chain(*seeds_new))

for i in range(n):
    #print(i)
    seed = int(seeds[i])

    for j in range(m):
        v = len(map[j])

        for k in range(v):
            temp = map[j][k].split()
            map_start = int(temp[0])
            map_end = map_start + int(temp[2])
            source_start = int(temp[1])
            source_end = source_start + int(temp[2])

            #source_range = list(range(source_start, source_start + seq_len))
            #map_range = list(range(map_start, map_start + seq_len))

            if seed >= source_start and seed <= source_end:
                #index = source_range.index(seed)
                seed = seed - source_start + map_start
                break
    seeds[i] = seed

min(seeds)
