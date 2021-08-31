import numpy as np
import matplotlib.pyplot as plt

1# 1-D Lattice (1 atom basis)

a = float(input("Distance between atoms: "))
N = int(input("Number of atoms: "))
e = float(input("On-site parameter: "))
t = float(input("Hopping parameter: "))

# Constructing the Hamiltonian

H = np.zeros((N,N))
for i in range(N):
  for j in range(N):
    if i==j:
      H[i][j] = e
    if j == i-1 or j == i+1:
      H[i][j] = t

# Determining Eigen Values and Eigen Vectors from the Hamiltonian Matrix

E,P = np.linalg.eig(H)
idx = np.argsort(E)[::-1][:N]
E = E[idx]
P = P[:,idx]

# Plotting E vs k 

k = np.linspace(0,N-1,N)
fig, ax = plt.subplots()
ax.set_title('Tight Binding Model (1D Lattice, 1 atom basis), $N='+str(N)+', a='+str(a)+'$')
ax.set_ylabel('$E$')
ax.set_xlabel('$k$')
ax.plot(k,P[:,0])
ax.grid(True)
fig.savefig('1D TB (1) plot.png')
