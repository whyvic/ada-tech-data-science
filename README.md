# ada-tech-data-science

## Primeira fase: git e versionamento de código
Git:
- é sistema de versionamento de código que guarda os registros de versão, além da referência/caminho

Comandos Git:
- mkdir nome-do-arquivo: serve para voce criar um diretorio(pasta)
- git init: serve para voce inicializar um repositório vazio
- git status: verifica a situação atual dos arquivos no repositório.
- git add: serve para adicionar as mudanças do arquivo para o staged.
- git diff: serve para visualizar as linhas que foram alteradas.
- git diff --staged: serve para visualizar as linhas alteradas que já recebram o git add

ESTADOS DE ARQUIVOS

1. Unmodified: arquivo ja mapeado, ou seja, ja esta no staged (já receberam um commit). Eles estão no ultimo estado commitado.
2. Modified: arquivo modificado, as mudanças ainda estão sendo mapeadas pelo git.
3. Staged: após o git add o arquivo esta preparado para receber o commit. Isso significa que as mudanças foram selecionadas para serem incluídas no próximo commit.