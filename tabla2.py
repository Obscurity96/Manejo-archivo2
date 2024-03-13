def mostrar_tabla(numero):
    archivo = f"tabla{numero}.txt"

    try:
        with open(archivo, "r") as f:
            contenido = f.read()
            print(f"Tabla de multiplicar para {numero}:\n")
            print(contenido)
    except FileNotFoundError:
        print("Error: El archivo no existe.")

def main():
    try:
        numero = int(input("Ingrese un número entre 1 y 10 para mostrar su tabla de multiplicar: "))
        if numero < 1 or numero > 10:
            print("Error: El número debe estar entre 1 y 10.")
        else:
            mostrar_tabla(numero)
    except ValueError:
        print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    main()
