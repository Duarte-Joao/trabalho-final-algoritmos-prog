# Gerenciador de Tarefas (To-Do List) em Python 

Aplicação de terminal desenvolvida em Python com foco em boas práticas de programação, estruturação modular baseada em funções, uso de orientação a objetos (POO) e persistência em memória.

## Funcionalidades do Sistema

O sistema opera inteiramente via linha de comando (CLI) e conta com as seguintes opções:

1. **Cadastrar Tarefa**: Permite adicionar uma nova tarefa informando a descrição e a prioridade (`Alta`, `Média` ou `Baixa`). O sistema gera automaticamente um identificador (`ID`) único e sequencial.
2. **Listar Tarefas**: Exibe todas as tarefas cadastradas divididas em categorias:
   - **Tarefas Ativas**: Organizadas de forma inteligente priorizando o nível de urgência (primeiro as de prioridade *Alta*, depois *Média* e por fim *Baixa*).
   - **Tarefas Concluídas**: Histórico limpo das tarefas já finalizadas.
3. **Concluir Tarefa**: Altera o status de uma tarefa ativa para `"Concluída"`, exibindo previamente as tarefas ativas disponíveis.
4. **Reabrir Tarefa**: Permite resgatar uma tarefa que estava concluída e retorná-la para o status de `"Ativa"`.
5. **Editar Tarefa**: Atualiza a descrição e/ou prioridade de uma tarefa ativa. O sistema permite manter os valores atuais apenas pressionando *Enter* durante a edição.
6. **Remover Tarefa**: Exclui permanentemente uma tarefa da agenda, contando com uma etapa de confirmação (`Sim/Não`) para evitar exclusões acidentais.

---

