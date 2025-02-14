friends = ['Alice', 'Bob', 'Charlie']
print(friends[2])
print(friends[-1])
print(friends[0:2])

lucky_numbers = [4, 8, 15, 16, 23, 42]
#friends.extend(lucky_numbers)
friends.append('Dora')
friends.insert(1, 'Kelly')
friends.remove('Bob')
friends.pop()
print(friends.index('Charlie'))
friends.sort()
print(friends)
friends.clear()
print(friends)