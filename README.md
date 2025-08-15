Instale as bibliotecas pandas e validate_docbr
O arquivo a ser validado deverá estar na mesma pasta do script verify.py
O script verfica a validade do cpf dentro de um csv baseado no digito verfificador, para o script funcionar é necessario a existência da coluna 'STATUS DE VALIDADE' dentro do csv onde será adicionado os status dos cpfs verificados(Verficado, Inválido ou Não informado).
Dentro do scrip altere o valor da variavel coluna_cpf para o valor correspondente ao nome da coluna onde se encontra os cpfs à serem validados. EX: coluna_cpf = 'CPF'
Dentro do scrip altere o valor da variavel arquivo_entrada para o valor correspondente ao nome do arquivo que sera validado juntamente com a estensão. EX: arquivo_entrada = 'CPF_validar.xlsx' ou arquivo_entrada = 'CPF_validar.csv'
Dentro do scrip altere o valor da variavel arquivo_saida para o valor correspondente ao nome que deseja para o arquivo que o script irá gerar  com os cpfs validados. EX: arquivo_saida = 'PLANILHA_VALIDADA_FINAL.xlsx'
Rode o script com o comando py verify.py no terminal.

Sinta-se livre para modificar a vontade este script
