import csv
import networkx as nx
import pickle

def main():
    graph = nx.MultiDiGraph()
    with open('transactions.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        headings = next(csv_reader)
        print(headings)
        for row in csv_reader:
            graph.add_edge(row[2], row[3], timestamp=row[1], value=row[4])
    
    with open('graph.pickle', 'wb') as file:
        pickle.dump(graph, file)

if __name__ == '__main__':
    main()