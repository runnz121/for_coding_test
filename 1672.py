k = int(input())

dna = str(input())

n = k
while True:

    if dna[n-1:n] == 'AA':
        dna = dna[n-2:n-1] + 'A'

    if dna[n-1:n] == 'GA':
        dna = dna[n-2:n-1] + 'c'