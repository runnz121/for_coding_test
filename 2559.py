N, K = map(int, input().split())
tem_list = list(map(int, input().split()))

part_sum = sum(tem_list[:K])
result_list = [part_sum]

for i in range(0, len(tem_list)-K):
    part_sum = part_sum - tem_list[i] + tem_list[i+K]
    result_list.append(part_sum)

print(max(result_list))

# 투포인터로 구현하면 시간초과남
# 처음 k만큼 더해준 후 앞을 빼주고 뒤를 더해주는 식으로 하면 시간초과를 줄일 수 있음