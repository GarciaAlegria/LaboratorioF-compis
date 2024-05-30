import pickle

import LR0


def load_grammar(file_path):
    with open(file_path, "rb") as file:
        grammar = pickle.load(file)

    return grammar


def load_tokens(file_path):
    with open(file_path, "r") as file:
        tokens = file.read().split(",")

    return tokens


if __name__ == "__main__":

    grammar = load_grammar("gramatica.pkl")
    lr0 = LR0.LR0(grammar)
    lr0.visualize().write_pdf("Automata_LR(0).pdf")
    print("LR0 guardado en Automata_LR(0).pdf")
    print("**************************************LR(0)**************************************")
    print("*********************************************************************************")
    print("Grammar:" + str(grammar))
    print("terminals:" + str(grammar["T"]))
    print("non-terminals:" + str(grammar["NT"]))
    print("productions:" + str(grammar["P"]))
    print("items:" + str(grammar["items"]))
    print("ignore:" + str(grammar["ignore"]))
    print("*********************************************************************************")
    print("*********************************************************************************" + "\n")

    print("**************************************Tabla**************************************")
    print("*********************************************************************************")
    lr0.slr1()
    print("*********************************************************************************")
    print("*********************************************************************************" + "\n")

    print("****************************Archivo con la cadena a evaluar*****************************")
    print("****************************************************************************************")
    tokens = load_tokens("tokens.txt")

    if tokens is None:
        print("Tokens no encontrados en tokens.txt")
        exit(1)

    print("tokens en el archivo a evaluar:", tokens)
    print("*********************************************************************************")
    print("*********************************************************************************" + "\n")

    print("************************************Resultado Final*************************************")
    print("****************************************************************************************")
    if lr0.parse(tokens, grammar["ignore"]):
        print("La cadena es aceptada por la gramática.")
    else:
        print("La cadena no es aceptada por la gramática.")
