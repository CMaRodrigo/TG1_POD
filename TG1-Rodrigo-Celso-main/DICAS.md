# Dicas do professor sobre o sistema da biblioteca:
Essas dicas são para auxiliar você a compreender melhor como funciona um sistema bibliotecário, uma vez que nem todos já usaram ou tem uma ideia concreta de como funciona.

## Dicas sobre usuários
- Existem apenas dois tipos de usuários no sistema: alunos e funcionários.
- Somente usuários cadastrados podem pegar livros emprestados (e devolvê-los).
- Usuários cadastrados  possuem seus dados registrados no arquivo database/usuarios.dat
- Usuários retiram múltiplos livros, mas cada empréstimo deve ser registrado individualmente na base de dados.

__Obs 1: Neste trabalho não há necessidade de implementar métodos para descadastrar usuários.__

__Obs 2: Também não há necessidade de limitar o empréstimo por um exemplar por usuário, então um usuário pode retirar múltiplas vezes um mesmo livro.__

## Dicas sobre livros:
- Apenas os dados básicos de um livro são necessários, como título, autor, e ano.
- Livros que possuem cadastro no acervo também devem possuir os atributos código do livro e quantidade de exemplares do mesmo disponíveis no acervo.
- O código de um livro é único e é atribuído automaticamente quando ele for adicionado ao acervo.

## Dicas sobre o acervo:
- O acervo representa o conjunto de livros da biblioteca.
- No acervo os livros são pesquisados, adicionados, ou retirados do acervo.
- Um ou mais exemplares de um livro são cadastrados e adicionados ao acervo.
- Se o título de um livro a ser cadastrado já faz parte do acervo, você pode apenas incrementar o número de exemplares.
- Se os dados de um livro a ser cadastrado ainda não fazem parte do acervo, então um novo código único de 5 dígitos é automaticamente gerado para esse livro e seus dados são adicionados ao acervo.
- O acervo mantém, no mínimo, um exemplar de cada livro em seu conjunto, portanto, livros nunca serão descadastrados e totalmente removidos do acervo.

## Dicas sobre empréstimo de livros:
- Livros ao serem emprestados recebem uma data na base de dados dos empréstimos. Essa data está no padrão DD-MM-AAAA.
- Livros não podem ser emprestados para usuários que possuem multa.
- Todos empréstimos são devidamente registrados, juntamente com o respectivo usuário, no arquivo emprestimos.dat, que é a base de dados.

__Obs: Fixe o tamanho dos meses em 30 dias para facilitar o cálculo do atraso na devolução dos livros.__

## Dicas sobre devolução de livros:
- Usuários podem pegar livros emprestados por um prazo de n dias.
- Para devoluções de livros que ocorrerem após os n dias do prazo, aplica-se ao usuário uma multa de N PUCoins por dia de atraso.
- Usuários com multa não podem retirar novos livros, mas podem devolver livros.
- Se um usuário com multa tentar devolver outro livro em atraso, a multa desse livro deve ser somada à multa corrente que consta no registro do usuário na base de dados.
- Não podem ser devolvidos livros cujo empréstimo não consta na base de dados.

__Obs 1: Neste trabalho não há necessidade de implementar métodos para remoção de multa.__

__Obs 2: Não há necessidade de calcular o dia final do prazo para devolução de um livro.__

## Dicas sobre a base de dados:
- Os arquivos utilizados como base de dados estão dentro do diretório database.
- Esses arquivos estão no formato .dat e cada linha deles contém um registro. Os dados de um registro são separados por ‘__’ e esse padrão precisa ser mantido.
- O sistema já possui alguns registros de livros, usuários e empréstimos na base de dados. Você deve garantir a coerência e integridade desses dados.

## Dicas sobre o conteúdo dos arquivos de registro no diretório database:
- Arquivo acervo.dat
    - Código do livro__título__autor__ano__numero de exemplares
- Arquivo usuarios.dat
    - tipo__nome__CPF__matrícula__curso ou departamento__multa
- Arquivo emprestimos.dat
    - Código do livro__título do livro__nome do usuário__CPF__data da retirada

## Dicas sobre os arquivos de operações diárias:
- As  operações de cada dia estão no diretório dias. Esses arquivos possuem uma série de operações que representam um dia de funcionamento da biblioteca.
- A primeira operação do arquivo é a today. Essa operação contém a data com o dia que essas operações estão sendo realizadas. Você deve usar essa data como base para registrar o dia do empréstimo de um livro e também para calcular a multa no momento da devolução de livro.
- Além do today, existem quatro outras operações principais:
    - Cadastra usuário (aluno ou funcionário)
    - Cadastra livro
    - Empresta livro
    - Devolve livro
	
## Dicas sobre a aplicação app.py:
- A aplicação app.py vai ler, interpretar e executar os comandos contidos nos arquivos do diretório dias.
- A aplicação vai permitir que múltiplos arquivos sejam passados como argumento no momento da execução. 
    - Ex.:
```
./app.py dias/dia1.txt dias/dias2.txt . . .
```
- A aplicação vai exibir na tela qual foi o comando executado a cada iteração e na sequência o resultado da operação.
    - Ex.: 
```
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Comando => empresta-->00006-->52325874125
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 Empréstimo realizado!
 Livro: Como fazer seu trabalho de python em 5 passos
 Usuario: Fernandes Astroso
```
- A aplicação não pode ser interrompida quando ocorrer um erro durante a execução de uma operação, ou seja, todos os erros devem ser capturados e tratados.
- As mensagens de erro devem ser armazenadas em um arquivo chamado log.err.
- Esse arquivo contém o comando que retornou erro e a respectiva mensagem de erro.
    - Ex.:
```
Comando => devolve-->00078-->52325874125
ErroLivroNaoEncontrado (código: 00078)
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Comando => . . .
Erro . . .
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
```
- Após processar todas as operações de todos os dias, a aplicação deve mostrar na tela o total de empréstimos e devoluções bem sucedidas.
