import pickle
import networkx as nx

graph = None

hash_to_int_map = dict()
next_node_id = 0

with open('graph.pickle', 'rb') as file:
    graph = pickle.load(file)

file = open('transactions.txt', 'w')

for i in graph.edges.data('timestamp'):
    sender = None
    receiver = None
    timestamp = i[2]
    if(i[0] in hash_to_int_map):
        sender = hash_to_int_map[i[0]]
    else:
        hash_to_int_map[i[0]] = next_node_id
        sender = next_node_id
        next_node_id += 1
    
    if(i[1] in hash_to_int_map):
        receiver = hash_to_int_map[i[1]]
    else:
        hash_to_int_map[i[1]] = next_node_id
        receiver = next_node_id
        next_node_id += 1
    file.write(f'{sender} {receiver} {timestamp}\n')

file.close()

with open('hash_to_int.pickle', 'wb') as file:
    pickle.dump(hash_to_int_map, file)