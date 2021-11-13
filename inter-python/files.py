def read():
    numbers = []
    # el artibuto enconding permite leer caraccteres especiales.
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))

    print(numbers)


def write():
    names = ["Elias", "Chibbu", "Chobbs", "Elenano"]
    # w -> reemplazo de escritura.
    # a -> agregar información al archivo.
    with open("./files/names.txt", "a", encoding="utf-8") as f:
        for i in names:
            # metodo write para escribir en el archivo de texto
            f.write(i)
            f.write("\n")


def run():
    read()
    write()


if __name__ == "__main__":
    run()
