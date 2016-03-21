#!/home/stirling/anaconda3/bin/python3
# Matrix Algebra
import numpy as np

A = np.matrix( [[1,2,3],[2,7,4]] )
B = np.matrix( [[1,-1],[0,1]] )
C = np.matrix( [[5,-1],[9,1],[6,0]] )
D = np.matrix( [[3,-2,-1],[1,2,3]] )
u = np.matrix( [[6,2,-3,5]] )
v = np.matrix( [[3,5,-1,4]] )
w = np.matrix( [[1],[8],[0],[5]] )

print("1.1) A ", A.shape)
print("1.2) B ", B.shape)
print("1.3) C ", C.shape)
print("1.4) D ", D.shape)
print("1.5) u ", u.shape)
print("1.6) w ", w.shape)

print("2.1) u + v = ", u+v)
print("2.2) u - v = ", u-v)
print("2.3) au = ", 6*u)
print("2.4) u * v = ", np.inner(u,v))
print("2.5) ||u|| = ", np.linalg.norm(u))

# print("3.1) A + C = ", A+C) #throws an error
print("3.1) A + C = not defined")
print("3.2) A - C^T = ", A - C.transpose())
print("3.3) C^T + 3D = ", C.transpose() + 3*D)
print("3.4) B A = ", np.dot(B,A))
# print("3.5) B A^T = ", np.dot(B,A.transpose())) #throws an error
print("3.5) B A^T = not defined")
# print("3.6) B C = ", np.dot(B,C)) #throws an error
print("3.6) B C = not defined")
print("3.7) C B = ", np.dot(C,B))
print("3.8) B^4 = ", np.dot(B,np.dot(B,np.dot(B,B))))
print("3.9) A A^T = ", np.dot(A, A.transpose()))
print("3.10) D^T D = ", np.dot(D.transpose(), D))
