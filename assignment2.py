import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing import nx_pydot
from graphviz import Source
import argparse



parser = argparse.ArgumentParser(description = "Add parameter")
parser.add_argument("-n", "--N", help = "Set the Number of vertex")
parser.add_argument("-a", "--ALPHA", help = "Set the alpha")
parser.add_argument("-c", "--CONNECT", help = "Set the connectivity of generated graph")

args = parser.parse_args()

N = 4
ALPHA = 0.8
generated = False
MAX_ITERATION = 100
CONNECTIVITY = 0.5
error = 0.0001
graph = np.array([[0, 1, 1, 1],
                  [1, 0, 0, 1],
                  [0, 0, 1, 0],
                  [0, 1, 1, 0]])

if args.N:
    N = int(args.N)
    generated = True 
if args.ALPHA:
    ALPHA = float(args.ALPHA)
if args.CONNECT:
    CONNECTIVITY = float(args.CONNECT)

def plot(graph):
    G = nx.from_numpy_array(graph,  create_using=nx.MultiDiGraph())
    pos = nx.spring_layout(G)  # Layout for positioning nodes
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=12, font_weight='bold', arrows=True)
    labels = {i: i for i in range(len(G.nodes()))}  # Assuming node labels are indices (0, 1, 2, ...)
    nx.draw_networkx_labels(G, pos, labels, font_size=12, font_color='black')
    plt.savefig("graph.png")

def generator(n, connectivity = 0.5):
    m = int(n * n * connectivity)
    graph = np.concatenate([np.ones((m,), dtype = int), np.zeros(n * n - m, dtype = int)])
    np.random.shuffle(graph)
    adj_matrix = graph.reshape((n,n))
    for i in range(n): # TO ensure the graph
        if adj_matrix[i].sum() == 0:
            adj_matrix[i][i] = 1
    return adj_matrix

if generated:
    graph = generator(N, CONNECTIVITY)

# 2 cyclic Graph
# N = 6
# graph = np.array([[0,1,0,0,0,0],
#                  [0,0,1,0,0,0],
#                  [1,0,0,0,0,0],
#                  [0,0,0,0,1,0],
#                  [0,0,0,0,0,1],
#                  [0,0,0,1,0,0]]
#                  )

# Single Path
# N = 6
# graph = np.array([[0,1,0,0,0,0],
#                  [0,0,1,0,0,0],
#                  [0,0,0,1,0,0],
#                  [0,0,0,0,1,0],
#                  [0,0,0,0,0,1],
#                  [0,0,0,0,0,1]]
#                  )

# N = 64
# graph = np.zeros((64,64))
# for i in range(N):
#     if i == N - 1:
#         graph[i][i] = 1
#     else:
#         graph[i][i + 1] = 1


# Complete Graph
# N = 6
# graph = np.array([[0,1,1,1,1,1],
#                  [1,0,1,1,1,1],
#                  [1,1,0,1,1,1],
#                  [1,1,1,0,1,1],
#                  [1,1,1,1,0,1],
#                  [1,1,1,1,1,0]]
#                 )

# N = 64
# graph = np.ones((64,64))
# for i in range(N):
#     graph[i][i] = 0

plot(graph)
graph = graph.transpose()
column_sum = np.sum(graph, axis = 0)
for i in range(N):
    if column_sum[i] == 0:
        column_sum[i] = 1
transitional = np.divide(graph, column_sum)

# O(K N^2)
# Assuming K is known (Iterate until Max iteration)
def iterative(transitional):
    v = np.ones(N)
    v /= N
    history = []
    history.append(v)
    for _ in range(MAX_ITERATION):
        v = np.matmul(ALPHA * transitional, v) + (1 - ALPHA) * np.ones(N) / N
        history.append(v)
    print(v)

# Assuming K is unknown
def iterativekunknwn(transitional):
    v = np.ones(N)
    v /= N
    vprev = np.zeros(N)
    iteration = 0
    new_transitional = ALPHA * transitional + (1 - ALPHA) * np.ones(N) / N 

    while(np.max(np.abs(v - vprev)) >= error):
        vprev = v
        v = np.matmul(new_transitional, vprev)
        # print(v, new_transitional)
        iteration += 1
    print("Iterative")
    print("Converge in", iteration)
    print(v)
    

# O(N ^2 log(k))
# Assuming K is known (Max Iteration)
def matrixexponentialrecursive(transitional):
    new_transitional = ALPHA * transitional + (1 - ALPHA) * np.ones(N) / N 

    def step(A, k):
        if( k == 0):
            return A
        
        cur = step(A, k // 2)
        if k % 2 == 1:
            return np.matmul(np.matmul(cur , A) , cur)
        else:
            return np.matmul(cur , cur)
    print(np.matmul(step(new_transitional, MAX_ITERATION), np.ones(N) / N))

# O(N ^2 log(k))
# Assuming K is unknown 
def matrixexponentialiterative(transitional):
    new_transitional = ALPHA * transitional + (1 - ALPHA) * np.ones(N) / N 
    
    
    a0 =  np.ones(N) / N
    iteration = 0
    aprev = np.matmul(new_transitional, a0)
    while True:
        new_transitional = np.matmul(new_transitional , new_transitional)
        a = np.matmul(new_transitional, a0)
        
        iteration += 1
        if np.max(np.abs(a - aprev)) < error:
            #print(np.max(np.abs(a - history[-1])) )
            break
        
        aprev = a
    print("Matrix Exponential")
    print("Converge in", iteration)
    print(a)

# O(N^3)
def theorectical(transitional):
    # R' = ALPHA T @ R' + (1- ALPHA)/N (1)
    # (I - ALPHA T) @ R' = (1 - ALPHA)/N (1)
    identity = np.zeros((N, N))
    for i in range(N):
        identity[i][i] = 1
    # print(transitional - identity)
    # print((transitional - identity) @ np.array([15/148, 19/148, 95/148, 19/148])) 
    print("Theorectical")
    print(np.linalg.solve(identity - ALPHA * transitional,  (1 - ALPHA) * np.ones(N) / N))


theorectical(transitional)
# matrixexponentialrecursive(transitional)
matrixexponentialiterative(transitional)
# iterative(transitional)
iterativekunknwn(transitional)