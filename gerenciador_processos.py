import os
import signal

def listar_processos():
    print("Listando processos ativos:")
    os.system("ps -e")

def terminar_processo(pid):
    try:
        os.kill(pid, signal.SIGKILL)
        print(f"Processo com PID {pid} terminado com sucesso.")
    except OSError as e:
        print(f"Erro ao terminar o processo: {e}")

def main():
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Listar processos")
        print("2. Terminar um processo")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            listar_processos()
        elif escolha == '2':
            try:
                pid = int(input("Digite o PID do processo a ser terminado: "))
                terminar_processo(pid)
            except ValueError:
                print("Por favor, digite um número válido para o PID.")
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
