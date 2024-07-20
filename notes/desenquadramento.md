### Controle de risco de desenquadramento e simulador

#### 1. check de enquadramento
A base será a comparação de 2 tabelas: política de investimento e alocação atual
A política de investimentos descrita em formato de tabela com as colunas sendo as classes de ativos e percentual máximo de alocação de cada um
A carteira precisa ser lançada em formato de tabela, com os valores das posições atual e definição da classe de ativo. 
App calculará a alocação e fará um check com a tabela de política de investimentos.
Se determinado ativo estiver fora da faixa da alocação permitida, app mostrará uma flag

#### 2. simulador de operações
Desenvolver um simulador de operações, em que o app coleta a carteira atual e abre campos para inserir valores.
Os valores são adicionados aos anteriores e o app calcula a nova distribuição da alocação, apresentando flags se a nova alocação resultar em desenquadramento.
