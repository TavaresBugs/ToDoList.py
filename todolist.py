from tabulate import tabulate
import csv

lista = []
aviso = [["Voce esta usando minha ToDo-List para sair do loop aperte CTRL + D"]]
headers = ["Tarefa", "Status"]

def main():
    print(tabulate(aviso, tablefmt="pretty"))
    try:
        while True:
            todo_list = input("Oque voce tem para fazer hoje ?\n")
            todo_status = ""
            while True:
                todo_status = input("Ja fez ?\n").title()
                if "Yes" in todo_status:
                    todo_status = "Feito"
                    todo = todo_list, todo_status
                    lista.append(todo)
                    break
                elif "No" in todo_status:
                    todo_status = "Em aberto"
                    todo = todo_list, todo_status
                    lista.append(todo)
                    break
                else:
                    print("Input invalido! Responda com Yes or No ?")
                    continue
    except EOFError:
        print("\nProcessando ...\n")
        tarefas(lista)

def tarefas(lista):

    arquivo = "todo_list.csv"
    with open("todo_list.csv", "w", newline="") as file:
        escrever = csv.writer(file)
        escrever.writerow(headers)
        for list in lista:
            escrever.writerow(list)

    final_list = []

    with open("todo_list.csv", "r") as file:
        ler = csv.reader(file)
        for linha in ler:
            final_list.append(linha)
    
    print(tabulate(final_list[1:], headers, tablefmt="pretty" ))


main()
