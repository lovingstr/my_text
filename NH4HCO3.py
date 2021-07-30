from random import shuffle
n = 6 # 人数
list1 = [x for x in range(1, n + 1)]

list_people = ["狼", "狼", "预言", "猎人", "女巫", "白狼"] # 神职
shuffle(list_people)

result = {}
for x in range(n):
    result[list1[x]] = list_people[x]

print(result)


##
##

quit()
