smd = 0
n = int(input())
while n != 0:
    if n % 8 == 0 and n % 10 == 6:
        smd += n
    n = int(input())
print(smd)