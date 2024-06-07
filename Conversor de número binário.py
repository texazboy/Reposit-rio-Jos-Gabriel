from bitstring import BitArray

def main():
    # Lista de inteiros
    inteiros = [32, 57, 101, 77]

    # Converter cada inteiro para binário
    binarios = [BitArray(uint=numero, length=8) for numero in inteiros]

    # Exibir os números binários
    for numero, binario in zip(inteiros, binarios):
        print(f"Inteiro: {numero} - Binário: {binario.bin}")

if __name__ == "__main__":
    main()