import numpy as np

M = 0.0474
N = 0.9526

print(np.array([[-N+0.5, -M+0.5], [3*N-1.5, 3*M -1.5], [2*N-1, 2*M-1]])/4)
print(np.array([[M+2*N+1.5, -2*M+N-0.5, 2*M+N+1.5]])/4)

a = np.array([[-1, 3, 2]]).T
b = np.array([[-0.5, 0.0474, 0.9526, -0.5]])
c = np.array([[0,0], [0,1], [1,0], [1,1]])

print(np.dot(a,np.dot(b,c))/4)