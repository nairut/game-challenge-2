# Guia de Nomenclatura de Branches e Boas Práticas

## Por que um Guia?

Manter um padrão consistente na nomenclatura de branches é crucial quando trabalhamos em projetos, especialmente em equipe (mesmo que a equipe seja só você no futuro!). Isso torna o histórico do Git mais legível, facilita a automação e ajuda a entender rapidamente o propósito de cada branch. Este guia adota uma convenção comum, alinhada com práticas como o Git Flow.

Além disso, vamos reforçar a importância de escrever código, comentários e nomes de branches/commits em **Inglês**.

## A Convenção de Nomenclatura: `tipo/descricao-curta`

Vamos adotar o seguinte padrão para nomear todas as novas branches (exceto as principais como `main` ou `develop`):

"tipo/descricao_curta"

**De modo que:**

1.  **`tipo`**: Indica a **natureza** ou o **propósito** do trabalho sendo realizado na branch. Deve ser uma das seguintes categorias (em minúsculas):
    *   **`feat`**: Para o desenvolvimento de uma **nova funcionalidade** (feature) para o usuário final.
        *   *Exemplo:* `feat/add-player-inventory`
    *   **`fix`**: Para a **correção de um bug** em produção ou em uma funcionalidade existente.
        *   *Exemplo:* `fix/prevent-item-duplication-on-drop`
    *   **`chore`**: Para tarefas de **manutenção** que não alteram o código de produção diretamente (ex: atualização de dependências, configuração de build, ajustes de ferramentas).
        *   *Exemplo:* `chore/update-python-dependencies`
    *   **`refactor`**: Para **refatoração de código** que não corrige um bug nem adiciona uma funcionalidade (melhora a estrutura, performance, legibilidade).
        *   *Exemplo:* `refactor/simplify-command-parser-logic`
    *   **`docs`**: Para adicionar ou atualizar a **documentação** do projeto.
        *   *Exemplo:* `docs/explain-world-json-format`
    *   **`test`**: Para adicionar ou refatorar **testes** automatizados.
        *   *Exemplo:* `test/add-tests-for-item-interaction`
    *   **`style`**: Para aplicar **ajustes de formatação** de código (espaços, ponto e vírgula, etc., geralmente via linters).
        *   *Exemplo:* `style/apply-black-formatter`

2.  **`/`**: Um separador literal entre o tipo e a descrição.

3.  **`descricao-curta-em-ingles`**: Uma descrição breve e significativa do que está sendo feito na branch. Siga estas regras:
    *   **Use Inglês:** Pela razão explicada abaixo.
    *   **Tudo em minúsculas:** `add-player-inventory` (bom) vs `Add-Player-Inventory` (ruim).
    *   **Use hífens (`-`)** para separar palavras: `add-player-inventory` (bom) vs `add_player_inventory` ou `add player inventory` (ruim).
    *   **Seja conciso, mas claro:** Outra pessoa (ou você no futuro) deve entender o propósito da branch lendo seu nome.
    *   **Evite caracteres especiais:** Além do hífen.


# Adendo ao Guia: Convenção para Mensagens de Commit

## Por Que Padronizar Mensagens de Commit?

Assim como padronizamos os nomes das branches, ter um formato consistente para as **mensagens de commit** é fundamental. Cada commit representa um pequeno passo salvo no histórico do projeto. Mensagens claras e padronizadas tornam esse histórico muito mais fácil de ler, entender e até mesmo automatizar tarefas (como gerar changelogs).

Vamos adotar a convenção conhecida como **Conventional Commits**. Ela se alinha perfeitamente com nossa nomenclatura de branches.

## O Formato Padrão

A estrutura básica de uma mensagem de commit seguindo o Conventional Commits é:

"<tipo>[escopo opcional]: <descrição>"


**Exemplo:** `feat(player): add inventory display command`

**Vamos detalhar cada parte:**

1.  **`<tipo>`:** Indica a **categoria** da mudança introduzida pelo commit. **Use os mesmos tipos que definimos para as branches**, garantindo consistência:
    *   **`feat`**: Uma nova funcionalidade (feature).
    *   **`fix`**: Uma correção de bug.
    *   **`chore`**: Tarefas de manutenção (build, dependências, etc.).
    *   **`refactor`**: Refatoração de código sem mudança funcional.
    *   **`docs`**: Mudanças na documentação.
    *   **`test`**: Adição ou refatoração de testes.
    *   **`style`**: Ajustes de formatação de código (linting).
    *   *(Opcional)* `perf`: Uma mudança que melhora a performance.

2.  **`[escopo opcional]`:** (Opcional) Uma palavra ou frase curta entre parênteses `()` que especifica a **parte do código** que a mudança afeta. Ajuda a dar contexto rápido.
    *   *Exemplos:* `(parser)`, `(inventory)`, `(docs)`, `(game_engine)`, `(item)`
    *   Se a mudança for muito ampla ou difícil de definir um escopo, pode ser omitido.
    *   *Exemplo com escopo:* `fix(parser): handle commands with extra spaces`
    *   *Exemplo sem escopo:* `refactor: improve readability of main loop`

3.  **`: `:** Um dois-pontos e um espaço separam o cabeçalho da descrição.

4.  **`<descrição>`:** Uma descrição **curta e imperativa** do que o commit faz. Siga estas regras:
    *   **Use Inglês.** (Pelos mesmos motivos do guia de branches).
    *   Comece com **letra minúscula**.
    *   Use o **modo imperativo** (como se estivesse dando uma ordem: "add", "fix", "change", "remove" em vez de "added", "fixed", "changes", "removed"). Pense: "Este commit irá... *[descrição]*".
    *   **Não termine com ponto final**.
    *   Seja conciso (idealmente, menos de 50-72 caracteres).



## Exemplos Práticos

**Bons Exemplos:**

*   `feat: add look command to describe current location`
*   `fix(inventory): prevent adding duplicate items`
*   `docs: explain the command parsing logic`
*   `refactor(item): simplify item usage method`
*   `chore: update project dependencies in requirements.txt`
*   `test: add unit tests for player movement`
*   `style: apply black code formatter`

**Exemplos a Evitar:**

*   `Fixed bug` (Não informativo, sem tipo)
*   `WIP` (Trabalho em progresso - faça commits mais atômicos)
*   `feat: Added the new inventory system.` (Não imperativo, ponto final)
*   `changed stuff` (Vago, sem tipo)
*   `chore: Adding the license file and updating the readme with new instructions` (Muito longo, não imperativo)

## Conectando Commits e Branches

Normalmente, uma branch criada com um certo tipo (ex: `feat/add-new-monster`) conterá principalmente commits desse mesmo tipo (`feat: ...`). Podem ocorrer commits de `fix:` se você corrigir algo relacionado à feature *dentro* da mesma branch, ou `refactor:` se decidir limpar o código antes de finalizar. A chave é a consistência e a clareza do histórico.

## Resumo

*   Use o formato `tipo(escopo): descrição` para suas mensagens de commit.
*   Mantenha os `tipos` consistentes com os nomes das branches.
*   Escreva descrições curtas, em inglês, no imperativo e começando com minúscula.
*   Opcionalmente, use `escopo` para dar mais contexto.

Praticar essas convenções tornará seu histórico do Git muito mais profissional e útil, facilitando a colaboração e a manutenção do projeto a longo prazo.



## A Importância de Usar Inglês no Código e Nomes

Mesmo que estejamos aprendendo em português, adotar o inglês para nomes de variáveis, funções, classes, comentários, mensagens de commit e nomes de branches é uma **prática profissional essencial** por várias razões:

1.  **Internacionalização e Colaboração:** O inglês é a língua franca da programação. Seu código poderá ser lido, entendido e mantido por desenvolvedores de qualquer lugar do mundo. Se você for trabalhar em projetos open-source ou em empresas com equipes globais, isso é indispensável.
2.  **Consistência com Ferramentas e Bibliotecas:** A vasta maioria das linguagens de programação, bibliotecas, frameworks e documentações técnicas está em inglês. Manter seu próprio código em inglês cria um ambiente mais coeso e evita a mistura de idiomas, que pode ser confusa.
3.  **Facilidade de Pesquisa:** É muito mais fácil encontrar soluções para problemas, exemplos de código e discussões em fóruns (como Stack Overflow) pesquisando termos técnicos em inglês.
4.  **Profissionalismo:** Demonstra que você está alinhado com as convenções e práticas da indústria de desenvolvimento de software.

**Exemplo Prático:**

*   **Ruim (Português):** `feat/adicionar-inventario-jogador`
*   **Bom (Inglês):** `feat/add-player-inventory`

## Resumo

*   Nomeie suas branches usando `tipo/descricao-curta-em-ingles`.
*   Escolha o `tipo` correto (`feat`, `fix`, `chore`, `refactor`, `docs`, `test`, `style`).
*   Escreva descrições curtas, claras, em minúsculas e separadas por hífen.
*   **Priorize o Inglês** em todo o código, comentários, commits e nomes de branches.

Adotar essas práticas desde cedo facilitará muito sua jornada como desenvolvedor e sua capacidade de trabalhar em projetos mais complexos e colaborativos.
