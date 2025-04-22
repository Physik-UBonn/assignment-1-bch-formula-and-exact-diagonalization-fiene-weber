import numpy as np

'Exercise c)'
# L = 2
# open boundaries
H2_open = 1/4*np.array([[1,0,0,0],[0,-1,2,0],[0,2,-1,0],[0,0,0,1]])
# periodic boundaries
H2_per = 1/2*np.array([[1,0,0,0],[0,0,1/2,0],[0,1/2,0,0],[0,0,0,1]])


# L = 3
H3 = np.array([[2,0,0,0,0,0,0,0],[0,0,2,0,0,0,0,2],[0,2,-2,2,0,0,0,0],[0,0,2,0,0,0,0,2],[0,0,0,0,0,0,2,0],[0,0,0,0,0,0,2,0],[0,0,0,0,2,2,-2,0],[0,2,0,2,0,0,0,2]])
def diagonalize(H):
    values, _ = np.linalg.eigh(H)
    return np.diag(values)

H2_open_diag = diagonalize(H2_open)
H2_per_diag = diagonalize(H2_per)
H3_diag = diagonalize(H3)
print("L = 2 with open boundaries: \n", H2_open_diag)
print("L = 2 with periodic boundaries: \n", H2_per_diag) 
print("L = 3 with open boundaries: \n", H3_diag)




'Exercise d)'
def time_evolution_operator(H, t):
    return np.exp(-1j*H*t)
