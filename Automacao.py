# passo a passo do projeto

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# 1. entrar no sistema da empresa
pyautogui.PAUSE = 1

    # abrir o navegador (Opera)

pyautogui.press('win')
pyautogui.write('Navegador Opera GX')
    # entrar no link 
pyautogui.press('enter')

        # https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

# 2. fazer login
    # pegar a posicao do 'EMAIL'
pyautogui.click(x=841, y=448)
        # escrever um email
pyautogui.write('contadulucas@gmail.com')
pyautogui.press('tab')# passando pro próximo campo
pyautogui.write('a senha é')
pyautogui.press('enter')
# pyautogui.click(x=1000, y=318)

# 3. importar a base de dados de produtos para cadastrar
import pandas as pd

base_de_dados = pd.read_csv('Aula 1/produtos.csv')
# tabela = pd.read_csv("produtos.csv")
print(base_de_dados)

# # 4. cadastrar um produto ###

# 5. repetir isso até acabar a base de dados

for linha in base_de_dados.index:
    pyautogui.click(x=1000, y=318)
    # Código do Produto
    preencher = base_de_dados.loc[linha,'codigo']
    pyautogui.write(preencher)
    pyautogui.press('tab')

    # preencher com 'marca'
    preencher = base_de_dados.loc[linha,'marca']
    pyautogui.write(preencher)
    pyautogui.press('tab')

    # Tipo do Produto
    preencher = base_de_dados.loc[linha,'tipo']
    pyautogui.write(preencher)
    pyautogui.press('tab')

    # Categoria do Produto
    preencher = str(base_de_dados.loc[linha, 'categoria'])
    pyautogui.write(preencher)
    pyautogui.press('tab')
        
    # Preço Unitário do Produto
    preencher = str(base_de_dados.loc[linha, 'preco_unitario'])
    pyautogui.write(preencher)
    pyautogui.press('tab')

    # Custo do Produto
    preencher = str(base_de_dados.loc[linha, 'custo'])
    pyautogui.write(preencher)
    pyautogui.press('tab')

    # OBS
    preencher = base_de_dados.loc[linha, 'obs']
    if not pd.isna(preencher):
        pyautogui.write(preencher)
    else:
        pyautogui.press('tab')

    # ENTER
    pyautogui.press('enter')
    pyautogui.scroll(5000)


    
