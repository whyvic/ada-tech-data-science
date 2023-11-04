# Ada Tech: Data Science

## Primeira fase: git e versionamento de código
### Git:
- é sistema de versionamento de código que guarda os registros de versão, além da referência/caminho
### GitHub:
* Plataforma que serve para hospedar códigos.
### Comandos Git:
- **mkdir nome-do-arquivo**: serve para voce criar um diretorio(pasta)
- **git init**: serve para voce inicializar um repositório vazio
- **git status**: verifica a situação atual dos arquivos no repositório.
- **git add**: serve para adicionar as mudanças do arquivo para o staged.
- **git diff**: serve para visualizar as linhas que foram alteradas.
- **git diff --staged**: serve para visualizar as linhas alteradas que já recebram o git add
- **git log**: serve para visualizar as alterações já feitas no repositório. São um tipo de histórico.
- **git restore nome_do_arquivo**: serve para remover alterações que ainda não foram commitadas.
- **git restore --staged**: serve para remover alterações que ja foram commitadas.
- **git push origin main**: empurra a ramificação local para o repositório remoto.
- **git pull**: serve para "buscar" as atualizações feitas no repositório remoto e incorporá-las no repositório local
- **git fetch**: não modifica osarquivos locais, ele serve para atualizar o registro do repositório remoto, obtendo informações mais recentes como novos commits e ramificações.
- **git branch nome_da_branch**: serve para criar outra ramificação no repositório.
- **git log --oneline --decorate**: serve para ver em qual branch o ponteiro head esta apontando, ou seja, ele mostra em que branch está.
- **git checkout nome_da_branch** serve para mudar de branch, se voce esta na branck main e quer ir pra branch teste voce deve dar o git checkout teste para se "locomover".
- **git branch**: mostra quais branch existem no repositorio.
- **git merge nome_da_branch**: serve para voce unir as branchs que existem em uma so ramificação. 
### Estados de arquivo

1. **Unmodified**: arquivo ja mapeado, ou seja, ja esta no staged (já receberam um commit). Eles estão no ultimo estado commitado.
2. **Modified**: arquivo modificado, as mudanças ainda estão sendo mapeadas pelo git.
3. **Staged**: após o git add o arquivo esta preparado para receber o commit. Isso significa que as mudanças foram selecionadas para serem incluídas no próximo commit.