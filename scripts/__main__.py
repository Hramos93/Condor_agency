import crear_numero_movil as start

def insert_num():
    n = 11    
    a = list(map(int, 
        input("\n Inserte 11 enteros entre 0-9 separados por un espacio  : ").strip().split()))[:n]

    return a
    

if __name__ == '__main__':
    numero = insert_num()
    print(start.generator_comb(numero))

