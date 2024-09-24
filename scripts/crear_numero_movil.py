import itertools

# codigos de area en venezuela
codigos = [[0,4,2,4],[0,4,1,4],[0,4,2,6],[0,4,1,6],[0,4,1,2]]


#creamos una funcion de numeros primos
def isprime(n):
    return (all(False for i in range(2,n) if n % i == 0) and not n < 2)



#Creamos todas las combinaciones posibles con el número y aplicamos las condiciones 
def preprocessing(vector:list, codigo=list):
    """ 
    vector : lista de numeros con 11 valores 

    return: lista de valores combinados con patron telefonico de venezuela 
    """

    condicion_1 = []
    condicion_2 = []
    condicion_3 = []
    condicion_4 = []
    num_completo = []
    condicion_5 = []
    condicion_6 = []

    
    for permutacion in itertools.permutations(vector):
        # condicion 1, que los valores 8 esten juntos. 
        if all([
            all(permutacion[i] == 8 for i in range(permutacion.index(8), permutacion.index(8) + vector.count(8)))]):
                condicion_1.append(permutacion)
    print("######## condicion 1 lista \n")    
                
    for iterador_movil in condicion_1:
        # condicion 2. itera sobre los números de la lista cuando la posición este sobre el 9 y sus extremos sean los valores i en posición antes y despues del 9.
        if all([len(set(iterador_movil[i-1:i+2])) == 3 for i in range(1, len(iterador_movil)-1) if iterador_movil[i] == 9]):
            condicion_2.append(iterador_movil)

    print("######## condicion 2 lista \n")  
    for iterador_movil in condicion_2:
        # condicion 3. valores al lado de los 8 sean distintos
        #ubicamos los valores 8 en la lista y condicionamos
        if all((iterador_movil[i-1] != iterador_movil[-1]) or (iterador_movil[i-1] != iterador_movil[i+2]) for i in range(1, len(iterador_movil)-1) if iterador_movil[i] == 8):
            condicion_3.append(iterador_movil)

    print("######## condicion 3 lista \n")  
    for iterador_movil in condicion_3:
        # condicion 4. itera sobre los números cuando la posición sea 8 y sera verdadero cuando los números entre el 8 sean diferentes
        if all(iterador_movil[i-1] == iterador_movil[i+1] for i in range(1, len(iterador_movil)-1) if iterador_movil[i] == 3):
            condicion_4.append(iterador_movil)
    num_completo = []
    for i in condicion_4:   
        num_completo.append(codigo + (list(i)))

        
    print("######## condicion 4 lista \n")  
    for iterador_movil in num_completo:
        #condicion 4 las posiciones 5 al 7 deben ser divisible entre 
        if iterador_movil[4] == 0:
            continue
        elif all(iterador_movil[i] % iterador_movil[4] == 0 for i in range(5, 8)):        
            condicion_5.append(iterador_movil)

    print("######## condicion 5 lista \n")  
    for iterador_movil in condicion_5:
        # no consideramos valores divibles entre 0
        if iterador_movil[-1] == 0:
            continue
        # penultimo divisible entre el ultimo
        elif iterador_movil[-2] % iterador_movil[-1] == 0:
            condicion_6.append(iterador_movil)

    print("######## condicion 6 lista \n")  
    condicion_7 = []
    for  iterador_movil in condicion_6:
        # ultimo numero primo
        if isprime(iterador_movil[-1]):
            condicion_7.append(iterador_movil)

    print("######## condicion 7 lista \n")  
    condicion_7.sort()
    resultado = list(k for k,_ in itertools.groupby(condicion_7))

    print(f'### resultado ### \n {resultado}')
    return resultado 

# detector de codigos en la lista
def generator_comb(vector_f):
    codigos = [[0,4,2,4],[0,4,1,4],[0,4,2,6],[0,4,1,6],[0,4,1,2]]
    """
    itera sobre la lista codigos para conseguir cual lista se encuentra entre los valores de la lista de números
    sino consigue un codigo de area, se retorna un string notificando que no existel codigo. 
    
    return: codigo aceptado.
    else string 
    """
    if all(isinstance(x, int) for x in vector_f) and (len(vector_f) == 11):
        print(vector_f)
        codigo = [i for i in codigos if set(i).issubset(set(vector_f))]
        print(codigo[0])        
        [vector_f.remove(i) for i in codigo[0]]
        print(vector_f)
       
        
        resultado = preprocessing(vector_f,codigo[0])
                                  
    else: print("inserte una lista con valores enteros")      
    return    
    
            