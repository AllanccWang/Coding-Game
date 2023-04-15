#https://www.codingame.com/training/medium/paving-with-bricks
#PAVING WITH BRICKS
#https://stackoverflow.com/questions/31354624/number-of-ways-to-tile-a-w-x-h-grid-with-2-x-1-and-1-x-2-dominos

memo={}

def tilings_recursive(uncovered):
    if len(uncovered) & 1:
        return 0
    if not uncovered:
        return 1
    if uncovered not in memo:
        i, j = min(uncovered)
        memo[uncovered] = tilings_recursive(uncovered - {(i, j), (i, j + 1)}) + tilings_recursive(uncovered - {(i, j), (i + 1, j)})
    return memo[uncovered]


def count_tilings(m, n):
    return tilings_recursive(frozenset((i, j) for i in range(max(m, n)) for j in range(min(m, n))))

w = int(input())
h = int(input())

print(count_tilings(w,h))
