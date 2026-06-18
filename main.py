from models import criar_materia, criar_atividade, listar_atividades_pendentes, marcar_concluida
from calculos import calcular_urgencia

def menu():
    while True:
        print("\n=== Organizador de Estudos ===")
        print("1. Cadastrar matéria")
        print("2. Cadastrar atividade")
        print("3. Ver atividades por prioridade")
        print("4. Marcar atividade como concluída")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da matéria: ")
            confianca = int(input("Sua confiança (0-10): "))
            criar_materia(nome, confianca)

        elif opcao == "2":
            materia_id = int(input("ID da matéria: "))
            titulo = input("Título da atividade: ")
            data_limite = input("Data limite (AAAA-MM-DD): ")
            peso = int(input("Peso (1-10): "))
            confianca = int(input("Sua confiança (0-10): "))
            horario = input("Horário da atividade (HH:MM): ")
            criar_atividade(materia_id, titulo, data_limite, peso, confianca, horario)

        elif opcao == "3":
            atividades = listar_atividades_pendentes()
            atividades_urgencia = [(a, calcular_urgencia(a)) for a in atividades]
            atividades_urgencia.sort(key=lambda x: x[1], reverse=True)
            print("\n=== Atividades por Prioridade ===")
            for a, u in atividades_urgencia:
                print(f"[ID: {a[0]}] {a[2]} | Urgência: {u:.2f} | Prazo: {a[3]}")

        elif opcao == "4":
            atividade_id = int(input("ID da atividade: "))
            marcar_concluida(atividade_id)

        elif opcao == "5":
            print("Até mais!")
            break

menu()