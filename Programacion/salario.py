salario=int(input("Ingrese el salario del profresor: "))
if salario<1800:
    salario= salario+(salario*0.12)
    print("El nuevo salario es",salario)
