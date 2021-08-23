import numpy as np
import matplotlib.pyplot as plt

# 1-D Lattice (1 atom basis)

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
E = np.sort(E)

# Plotting E vs k 

E_ = np.concatenate((np.flip(E),E))
k = np.linspace(-1*np.pi/a, np.pi/a, 2*N)

fig, ax = plt.subplots()
ax.set_xlim(-np.pi/a, np.pi/a)
ax.set_title('Tight Binding Model (1D Lattice, 1 atom basis), $N='+str(N)+', a='+str(a)+'$')
ax.set_ylabel('$E$')
ax.set_xlabel('$k$')
ax.axvline(x=0,color='black')
ax.plot(k, E_, 'ro', label='Eigenvalues of H')
ax.set_xticks(k)
xlabels = ['' for x in k]
xlabels[0] = '$-\\frac{\pi}{a}$'
xlabels[-1] = '$\\frac{\pi}{a}$'
ax.set_xticklabels(xlabels)
ax.grid(True)
fig.savefig('1D TB plot.png')
