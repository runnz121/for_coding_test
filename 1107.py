target = int(input())
n = int(input())
if n >= 1:
    broken = list(map(int, input().split()))
else:
    broken = []
normal = [i for i in range(10)]
uses = set(normal) - set(broken)


uses = list(uses)

start = 100

count = 0

find = ''

if len(str(target)) == 3:
    if target == start:
        count = 0
    else:
        count = target - start

else:
    # 각 자리 숫자
    for num in list(str(target)):

        find_up = int(num)
        find_down = int(num)

        if int(num) in uses:
            find += str(num)
            count += 1
        else:
            while True:
                find_up += 1
                find_down -=1

                if find_up in uses:
                    find += str(find_up)
                    count += 1
                    break
                elif find_down in uses:
                    find += str(find_down)
                    count += 1
                    break
    find1 = find
    find2 = find
    find3 = find


    print('find', find)
    max_use = max(uses)
    find1 = find1.replace('0', str(max_use))
    

    count1 = abs(target - int(find1))
    count2 = abs(target - int(find2))

    count += min(count1, count2)

print(count)