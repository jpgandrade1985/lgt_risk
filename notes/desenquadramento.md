## Controle de risco de desenquadramento e simulador

### 1. check de enquadramento
A base será a comparação de 2 tabelas: política de investimento e alocação atual
A política de investimentos será descrita em formato de tabela de banco de dados com as colunas sendo: fundo, classe do ativo, subclasses do ativo e alocação permitida.
A carteira atual será descrita em formato de tabela, com as colunas: fundo, nome do ativo, classe do ativo, subclasse do ativo e valor da posição. 
As classes e subclasses devem ser as mesmas existentes nas duas tabelas.
App calculará a alocação da carteira atual e fará um check com a tabela de política de investimentos.
Se determinado ativo estiver fora da faixa da alocação permitida, app mostrará uma flag

### 2. simulador de operações
Desenvolver um simulador de operações, em que o app coleta a carteira atual e abre campos para inserir valores.
Os valores são adicionados aos anteriores e o app calcula a nova distribuição da alocação, apresentando flags caso a nova alocação resulte em desenquadramento.

### 3. Questões futuras: 
####Como automatizar?
**importação da carteira:** 
- Que formato deve ter essa carteira?
- deve ser feito algum trabalho prévio com planilhas para uniformizar os dados?
- o administrador já classifica os ativos de acordo com a política de investimentos?
