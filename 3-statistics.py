import statistics as st

# 1 - Aplicando média
print(st.mean([3,2,3,8,9]))

# 2 - Aplicando a mediana
print(st.median([3,2,3,8,9]))
print(st.median([3,2,3,8,9,10])) # Soma os dois do meio e divide por 2

# 3 - Aplicando a moda
print(st.mode([2,5,3,2,8,3,9,4,2,5,6]))

# 4 - Desvio padrão
"""
Quanto mais próximo de 0 for o devio padrão, siginifica que os dados do conjunto estão menos dispersos
"""
print(f"{st.stdev([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]):.2f}")