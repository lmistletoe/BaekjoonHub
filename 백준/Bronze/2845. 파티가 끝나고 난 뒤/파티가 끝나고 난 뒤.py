people, area = map(int, input().split())
p_area = people * area
newspaper = list(map(int, input().split()))
for i in newspaper:
	print(i-p_area, end=' ')