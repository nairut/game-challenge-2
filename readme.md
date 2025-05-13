# Desafio: Construir um Motor de Jogo de Aventura Textual Simplificado

## Visão Geral do Projeto

Desenvolva um motor de jogo em Python que permita criar e jogar aventuras simples baseadas em texto. O jogador navegará por diferentes locais, interagirá com objetos e personagens. O foco principal será a aplicação de conceitos intermediários de Programação Orientada a Objetos (POO), como **Herança**, **Composição**, **Encapsulamento** e **Polimorfismo** para modelar o mundo do jogo de forma flexível e extensível.

## Objetivos de Aprendizagem

* **Aprofundar em Programação Orientada a Objetos:**
  * Aplicar **Herança** para criar hierarquias de classes (ex: diferentes tipos de itens ou personagens).
  * Utilizar **Composição** para construir objetos complexos a partir de outros (ex: uma sala contendo itens e personagens).
  * Implementar **Polimorfismo** para permitir que diferentes objetos respondam à mesma mensagem (ex: `examinar()`) de maneiras específicas.``<item>```:
  * Reforçar o **Encapsulamento** protegendo o estado interno dos objetos.
* **Gerenciar Lógica Básica do Jogo:** Controlar a localização do jogador, inventário e interações dentro de uma única sessão de jogo.
* **Praticar Estrutura e Modularização:** Organizar o código em classes e módulos coesos.
* **Manipular Dados Estruturados:** Carregar a definição inicial do mundo a partir de um arquivo JSON.
* **Seguir o Git Flow:** Continuar a prática de entregas incrementais com Pull Requests.

## Conceitos Chave de POO a Aplicar

* **Herança:**
  * Crie uma classe base `ObjetoJogo` (ou `GameObject`) da qual outras entidades do jogo herdarão (ex: `Lugar`, `Item`, `Personagem`).
  * Crie subclasses para `Item` (ex: `Chave`, `Consumivel`) que possam ter comportamentos específicos (ex: um método `usar()`).
  * Crie subclasses para `Personagem` (ex: `Jogador`, `NPC`) com atributos ou métodos distintos (ex: `falar()`).
* **Composição:**
  * A classe `Lugar` deve *conter* coleções de `Itens` e `Personagens` presentes nela.
  * A classe `Jogador` (que herda de `Personagem`) deve *conter* um inventário (uma coleção de `Itens`).
  * A classe principal `Jogo` (ou `GameEngine`) *compõe* o estado atual, incluindo o `Lugar` atual do `Jogador` e o próprio objeto `Jogador`.
* **Polimorfismo:**
  * Implemente um método comum (ex: `descrever()` ou `examinar()`) nas classes base/abstratas que subclasses podem sobrescrever. O motor do jogo poderá chamar `objeto.examinar()` sem saber o tipo exato do objeto, e obter a descrição correta.
  * A interação com diferentes tipos de `Itens` (ex: `usar(item)`) pode ser tratada polimorficamente.
* **Encapsulamento:**
  * Garanta que os atributos internos das classes (ex: descrição de um lugar, status de um item) sejam acessados e modificados através de métodos, quando apropriado.

## Estrutura Sugerida do Projeto (Classes Principais)

1. **`ObjetoJogo` (Classe Base):**

   * Atributos comuns: `nome`, `descricao`.
   * Métodos comuns: `descrever()`.
2. **`Lugar` (Herda de `ObjetoJogo`):**

   * Responsabilidades: Descrever o local, armazenar itens e personagens presentes, gerenciar conexões para outros lugares *pelo nome*.
   * Atributos: `nome`, `descricao`, `itens` (lista/dict de `Item`), `personagens` (lista/dict de `Personagem`), `conexoes` (dict mapeando **nome do lugar de destino** para o objeto `Lugar` correspondente).
   * Métodos: `adicionar_item()`, `remover_item()`, `adicionar_personagem()`, `remover_personagem()`, `get_conexao(nome_lugar)`, `descrever_detalhes()` (mostra lugar, itens, personagens, lugares acessíveis por nome).
3. **`Item` (Herda de `ObjetoJogo`):**

   * Responsabilidades: Representar um objeto que pode ser examinado, pego, largado, etc.
   * Atributos: `nome`, `descricao`, `pegavel` (bool).
   * Métodos: `examinar()`.
   * **Subclasses (Exemplos):**
     * `Chave`: Pode ter um atributo que identifica o que ela abre. Método `usar()`.
     * `Consumivel`: Pode ter um efeito ao ser usado. Método `usar()`.
4. **`Personagem` (Herda de `ObjetoJogo`):**

   * Responsabilidades: Representar uma entidade viva no jogo.
   * Atributos: `nome`, `descricao`.
   * Métodos: `falar()` (pode retornar um diálogo padrão).
   * **Subclasses:**
     * **`Jogador` (Herda de `Personagem`):**
       * Atributos: `inventario` (lista/dict de `Item`).
       * Métodos: `pegar_item(item)`, `largar_item(item)`, `mostrar_inventario()`, `ir_para(nome_lugar)`.
     * **`NPC` (Non-Player Character - Herda de `Personagem`):**
       * Atributos: `dialogo` (string ou lista de strings).
       * Métodos: `falar()` (retorna o diálogo específico).
5. **`Jogo` (Motor Principal):**

   * Responsabilidades: Orquestrar o fluxo do jogo, processar comandos do jogador, gerenciar o estado **em memória** (lugar atual, jogador), carregar a definição inicial do mundo.
   * Atributos: `jogador`, `lugar_atual`, `mundo` (coleção de todos os lugares/objetos carregados).
   * Métodos: `iniciar()`, `processar_comando(comando_str)`, `carregar_mundo(arquivo_json)`. **(Nota: Salvamento/Carregamento de estado do jogo não é exigido)**.

## Funcionalidades Mínimas Essenciais

1. **Definição do Mundo:** Carregar a estrutura inicial do mundo (lugares, suas descrições, conexões *por nome*, itens iniciais, NPCs) a partir de um arquivo JSON (`mundo.json`). O estado do jogo existe apenas em memória enquanto o programa roda.
2. **Movimentação Simplificada:** Permitir que o jogador se mova entre os lugares usando comandos como `ir <NomeDoLugar>` (ex: `ir Cozinha`, `ir Corredor`). O `Lugar` atual deve listar os nomes dos lugares diretamente acessíveis.
3. **Observação:** Permitir que o jogador examine o lugar atual (`olhar`), itens específicos (`examinar <item>`) e personagens (`examinar <personagem>`).
4. **Interação com Itens:** Permitir pegar (`pegar <item>`) e largar (`largar <item>`) itens que sejam marcados como `pegavel`.
5. **Inventário:** Permitir ao jogador ver seu inventário (`inventario` ou `i`).
6. **Interação Básica com NPCs:** Permitir falar com NPCs (`falar com <npc>`).
7. **Processamento de Comandos:** Implementar um parser simples que interprete os comandos do jogador (verbo + alvo(s), ex: `pegar chave`, `ir Cozinha`).
8. **Saída Limpa:** Comando para sair do jogo (`sair`).

## Exemplo de Mundo Pequeno para Implementação/Teste (Navegação por Nome)

Crie um mundo simples com pelo menos 3 lugares conectados:

* **"Sala de Estar"**: Contém uma `chave velha`. Conexão: Leva para o "Corredor". Descrição: "Você está numa sala de estar empoeirada. Você pode ir para: Corredor."
* **"Corredor"**: Contém um `NPC` chamado `Guardião`. Conexões: Leva para "Sala de Estar", leva para "Cozinha". Descrição: "Um corredor estreito. Um guardião silencioso está aqui. Você pode ir para: Sala de Estar, Cozinha." O Guardião pode dizer: "Bem-vindo ao corredor."
* **"Cozinha"**: Contém uma `maçã` (Item Consumível). Conexão: Leva para o "Corredor". Descrição: "Uma cozinha bagunçada. Uma maçã vermelha brilha sobre a mesa. Você pode ir para: Corredor."

## Persistência de Dados (Simplificada)

* **Definição do Mundo:** Use um arquivo JSON (`mundo.json`) para definir os lugares, suas descrições, conexões (mapeando nomes de lugares para onde levam), itens iniciais e NPCs. O método `Jogo.carregar_mundo()` deve ler este arquivo **uma vez no início** e instanciar os objetos correspondentes em memória.
* **Estado do Jogo:** **Não é necessário implementar salvamento e carregamento do estado do jogo.** O progresso do jogador (inventário, localização atual) será perdido quando o programa for fechado.

## Modularização

Organize seu código em módulos (arquivos `.py`):

* `objetos_jogo.py` (para `ObjetoJogo`, `Item`, `Personagem` e suas subclasses)
* `lugar.py` (para a classe `Lugar`)
* `jogador.py` (para a classe `Jogador`)
* `jogo.py` (para a classe `Jogo`/Engine)
* `main.py` (ponto de entrada, instancia `Jogo` e inicia o loop principal)
* `utils.py` (opcional, para funções auxiliares como parsing de comando)

## Fluxo de Jogo Básico (Loop Principal)

1. Carregar definição inicial do mundo do `mundo.json`.
2. Criar o objeto `Jogador`.
3. Definir o `lugar_atual` inicial do jogador.
4. **Loop:**
   a.  Exibir descrição do lugar atual (incluindo itens visíveis, NPCs e para onde se pode ir).
   b.  Aguardar input do jogador (ex: `> `).
   c.  Ler o comando do jogador.
   d.  Se comando for `sair`, encerrar o loop.
   e.  Processar o comando (identificar verbo e alvos, chamar métodos apropriados nos objetos `Jogo`, `Jogador` ou `Lugar`).
   f.  Atualizar o estado do jogo em memória (posição do jogador, inventário, etc.).
   g.  Exibir feedback para o jogador (ex: "Você pegou a chave.", "Você foi para a Cozinha.").
   h.  Repetir o loop.

## Controle de Versão e Git Flow

Divida o desenvolvimento em partes lógicas e use **pelo menos 5 Pull Requests** para integrar as funcionalidades ao branch principal (`main` ou `master`).

**Exemplo de Divisão (Sugestão Adaptada):**

1. **PR 1:** Estrutura básica do projeto, classes `ObjetoJogo`, `Lugar` (sem itens/personagens/conexões ainda), `Jogo` inicial (sem loop). Definição básica do `mundo.json`.
2. **PR 2:** Implementação da classe `Item` e subclasses simples. Funcionalidade de `examinar item` e `olhar` (mostrando itens no lugar). Carregamento de itens do `mundo.json`.
3. **PR 3:** Implementação das classes `Personagem`, `Jogador`, `NPC`. Funcionalidade de `examinar personagem`, `falar com npc`. Carregamento de personagens do `mundo.json`.
4. **PR 4:** Implementação de `pegar`, `largar`, `inventario`. Implementação da movimentação simplificada (`ir <NomeDoLugar>`) e carregamento/uso das `conexoes` entre `Lugar`es.
5. **PR 5:** Implementação do loop principal do jogo em `Jogo`, parser de comandos básico e refinamentos gerais.

## Desafios Bônus (Opcional - Mantidos)

* **Puzzles Simples:** Implementar portas ou passagens bloqueadas que requerem `Chave`s específicas (`usar chave`).
* **Sistema de Combate Básico:** Adicionar atributos de ataque/defesa a `Personagem` e `Item` (como `Arma`), e implementar um comando `atacar`.
* **Efeitos de Itens:** Fazer itens consumíveis (`Consumivel`) terem efeitos reais no jogador.

## Considerações Finais

Este projeto foca em aprofundar seus conhecimentos em POO, modelando um sistema interativo. A simplificação na navegação e no estado permite concentrar-se nas relações entre classes ("é um" vs. "tem um") e como usar Herança e Composição eficazmente. Divirta-se construindo seu próprio mundo de aventura!
