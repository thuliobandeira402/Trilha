class Tarefa():
    def __init__(self, titulo, prioridade, status='Pendente'):
        self.titulo = titulo
        self.prioridade = prioridade
        self.status = status

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if not value or not value.strip():
            raise ValueError("O título da tarefa não pode ser vazio.")
        self._titulo = value

    @property
    def prioridade(self):
        return self._prioridade

    @prioridade.setter
    def prioridade(self, value):
        if value not in ['Baixa', 'Média', 'Alta']:
            raise ValueError("A prioridade deve ser 'Baixa', 'Média' ou 'Alta'.")
        self._prioridade = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ['Pendente', 'Em andamento', 'Concluída']:
            raise ValueError("O status deve ser 'Pendente', 'Em andamento' ou 'Concluída'.")
        self._status = value

class GestorDeTarefas():
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f"Tarefa '{tarefa.titulo}' adicionada com sucesso.")

    def listar_tarefas(self):
        print("\n--- Lista de Tarefas ---")
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return
        for tarefa in self.tarefas:
            print(f"Título: {tarefa.titulo}, Prioridade: {tarefa.prioridade}, Status: {tarefa.status}")
        print("------------------------\n")

    def atualizar_status(self, titulo, novo_status):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                tarefa.status = novo_status
                print(f"Status da tarefa '{titulo}' atualizado para '{novo_status}'")
                return
        print(f"Tarefa com título '{titulo}' não encontrada.")

    def concluir_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                tarefa.status = 'Concluída'
                print(f"Tarefa '{titulo}' concluída.")
                return
        print(f"Tarefa com título '{titulo}' não encontrada.")

# Rotina de execução para testar as funcionalidades do gestor de tarefas abaixo:

if __name__ == "__main__":
    gestor = GestorDeTarefas()

    print(">>> 1. Criando e adicionando tarefas válidas:")
    t1 = Tarefa("Estudar Python POO", "Alta", "Em andamento")
    t2 = Tarefa("Fazer compras da semana", "Média")
    t3 = Tarefa("Limpar a mesa de trabalho", "Baixa")
    t4 = Tarefa("Ir pra academia", "Alta", 'Pendente')

    gestor.adicionar_tarefa(t1)
    gestor.adicionar_tarefa(t2)
    gestor.adicionar_tarefa(t3)
    gestor.adicionar_tarefa(t4)

    print("\n>>> 2. Listagem inicial:")
    gestor.listar_tarefas()

    print(">>> 3. Atualizando status e concluindo tarefas:")
    gestor.atualizar_status("Fazer compras da semana", "Em andamento")
    gestor.concluir_tarefa("Estudar Python POO")

    print("\n>>> 4. Listagem após atualizações:")
    gestor.listar_tarefas()

    print(">>> 5. Testando o tratamento de erros:")
    #Tentativa com título vazio
    try:
        Tarefa("   ", "Baixa")
    except ValueError as erro:
        print(f"[Validação Capturada] {erro}")

    #tentativa com prioridade inválida
    try:
        Tarefa("Ler documentação", "Urgente")
    except ValueError as erro:
        print(f"[Validação Capturada] {erro}")

    # Tentativa com status inválido ao atualizar
    try:
        t2.status = "Cancelada"
    except ValueError as erro:
        print(f"[Validação Capturada] {erro}")

