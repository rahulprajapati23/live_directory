
# Matrix Chain Multiplication using Dynamic Programming
# Given dimensions: (5, 10, 3, 12, 5, 50, 6)
# Matrices: A1: 5x10, A2: 10x3, A3: 3x12, A4: 12x5, A5: 5x50, A6: 50x6

def matrix_chain_order(p):
	n = len(p) - 1 # number of matrices
	m = []
	for i in range(n):
		row = []
		for j in range(n):
			row.append(0)
		m.append(row)
	s = []
	for i in range(n):
		row = []
		for j in range(n):
			row.append(0)
		s.append(row)

	for l in range(2, n+1):
		for i in range(n - l + 1):
			j = i + l - 1
			m[i][j] = float('inf')
			for k in range(i, j):
				q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
				if q < m[i][j]:
					m[i][j] = q
					s[i][j] = k
	return m, s
def min_multi(s, i, j):
	if i == j:
		return f"A{i+1}"
	else:
		left = min_multi(s, i, s[i][j])
		right = min_multi(s, s[i][j]+1, j)
		return f"({left} x {right})"

dimensions = [5, 10, 3, 12, 5, 50, 6]
m, s = matrix_chain_order(dimensions)
min_mult = m[0][len(dimensions)-2]
min_req = min_multi(s, 0, len(dimensions)-2)

print("Minimum number of multiplications:", min_mult)
print("Optimal parenthesization:", min_req)

