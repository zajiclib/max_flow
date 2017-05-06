"""From Taha 'Introduction to Operations Research', example 6.4-2."""

from __future__ import print_function
from ortools.graph import pywrapgraph

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

Z = [[None, 4, 6, None, 8, None],
     [0, None, 2, 3, None, None],
     [0, 2, None, 5, 3, None],
     [None, 0, 0, None, 2, 5],
     [0, None, 0, 4, None, 3],
     [None, None, None, 0, 0, None],]

# convert for rendering
R = []
for row in Z:
    new_row = list(row)
    for i, value in enumerate(new_row):
        new_row[i] = 0 if value is None else value + 1
    R.append(new_row)

G = nx.from_numpy_matrix(np.array(R), create_using=nx.MultiDiGraph())
pos = nx.circular_layout(G)
nx.draw_circular(G)
labels = {i : i + 1 for i in G.nodes()}
nx.draw_networkx_labels(G, pos, labels, font_size=15)
plt.show()

start_nodes = []
end_nodes = []
capacities = []
for i, row in enumerate(Z):
    for j, cell in enumerate(row):
        if cell > 0:
            start_nodes.append(i)
            end_nodes.append(j)
            capacities.append(cell)

def main():
  """MaxFlow simple interface example."""

  # Define three parallel arrays: start_nodes, end_nodes, and the capacities
  # between each pair. For instance, the arc from node 0 to node 1 has a
  # capacity of 20.
  """
  start_nodes = [0, 0, 0, 1, 1, 2, 2, 3, 3]
  end_nodes = [1, 2, 3, 2, 4, 3, 4, 2, 4]
  capacities = [20, 30, 10, 40, 30, 10, 20, 5, 20]
  """
  # Instantiate a SimpleMaxFlow solver.
  max_flow = pywrapgraph.SimpleMaxFlow()
  # Add each arc.
  for i in range(0, len(start_nodes)):
    max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])

  if max_flow.Solve(0, len(Z) - 1) == max_flow.OPTIMAL:
    print('Max flow:', max_flow.OptimalFlow())
    print('')
    print('  Arc    Flow / Capacity')
    for i in range(max_flow.NumArcs()):
      print('%1s -> %1s   %3s  / %3s' % (
          max_flow.Tail(i),
          max_flow.Head(i),
          max_flow.Flow(i),
          max_flow.Capacity(i)))

  else:
    print('There was an issue with the max flow input.')

if __name__ == '__main__':
  main()