# AutoCadastroProdutos

## Descrição do Projeto

O projeto **AutoCadastroProdutos** tem como objetivo automatizar o processo de cadastro de produtos em um sistema específico da empresa. Utilizando a biblioteca PyAutoGUI em Python, o script realiza o login no sistema, navega até a página de cadastro, importa uma base de dados de produtos e cadastra cada item dessa base.

## Requisitos

- Python 3.x
- Bibliotecas Python: pyautogui, time, pandas

## Instruções de Uso

1. **Configuração Inicial:**
    - Certifique-se de ter Python 3.x instalado.
    - Instale as bibliotecas necessárias executando o comando `pip install pyautogui time pandas`.

2. **Execução do Script:**
    - Execute o script Python `autocadastro.py`.

3. **Observações:**
    - O script usa o navegador Opera GX para a interação com o sistema. Certifique-se de ter o navegador instalado.

4. **Importante:**
    - Certifique-se de entender e concordar com as implicações de automação em sistemas antes de usar este script.

## Detalhes do Código

O código está organizado em passos lógicos, cada um representando uma etapa do processo de automação:

1. **Entrar no Sistema da Empresa:**
    - Abre o navegador Opera GX e acessa o link do sistema.

2. **Fazer Login:**
    - Preenche os campos de e-mail e senha para realizar o login.

3. **Importar Base de Dados de Produtos:**
    - Utiliza a biblioteca pandas para ler uma base de dados de produtos no formato CSV.

4. **Cadastrar Produtos:**
    - Utiliza um loop para percorrer a base de dados, preenchendo os campos necessários e realizando o cadastro de cada produto.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está sob a licença [MIT](LICENSE).
