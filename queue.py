queue = []

queue.append('a')
queue.append('b')
queue.append('c')

print('initial queue')
print(queue)

print('\nElement dequeued from queue')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print('\nElement after removing elements')
print(queue)
