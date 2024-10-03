def BuscaBinaria(array, valor):
   inicio = 0
   fim = len(array) - 1
   while inicio <= fim:
      meio = (inicio + fim) // 2
      if array[meio] == valor:
         return meio
      elif array[meio] < valor:
         inicio = meio + 1
      else:
         fim = meio - 1
   return -1
            
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = BuscaBinaria(array, 5)
print(f'Valor buscado está no indice: {resultado}')
