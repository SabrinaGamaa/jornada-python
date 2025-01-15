import pyautogui
import pandas as pd
from time import sleep
pyautogui.PAUSE = 1

# Carregar o arquivo csv
dado = pd.read_csv('power-up/produtos.csv')


# 1. Abrir o chrome
print('Começando o programa...')
pyautogui.press('win')
pyautogui.write('Chrome')
sleep(2)
pyautogui.press('enter')

# 2. Entrar no site
site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(site)
pyautogui.press('enter')
sleep(4)

# 3. Fazer o login
pyautogui.click(x=594, y=406)

#   Seu email
pyautogui.write('seuemail@gmail.com')
pyautogui.press('tab')
#   Sua senha
pyautogui.write('12345678')
pyautogui.press('tab')
pyautogui.press('enter')
sleep(2)

# Fazamento de senha
pyautogui.press('enter')

# 4. Cadastramento de produto


for linha in dado.itertuples():
    pyautogui.click(x=514, y=296)
    # Cadastrar produto
    # codigo,marca,tipo,categoria,preco_unitario,custo,obs

    # Codigo
    pyautogui.write(linha.codigo)
    pyautogui.press('tab')

    # Marca
    pyautogui.write(linha.marca)
    pyautogui.press('tab')

    # TipoMouse
    pyautogui.write(linha.tipo)
    pyautogui.press('tab')

    # Categoria
    pyautogui.write(str(linha.categoria))
    pyautogui.press('tab')

    # Preço
    pyautogui.write(str(linha.preco_unitario))
    pyautogui.press('tab')

    # Custo
    pyautogui.write(str(linha.custo))
    pyautogui.press('tab')

    if pd.isna(linha.obs) == False:
        pyautogui.write(linha.obs)
    # if pd.notna(linha.obs):  # Use `pd.notna` para verificar se não é NaN
    # pyautogui.write(linha.obs)


    pyautogui.press('tab')
    pyautogui.press('enter')
    
    pyautogui.scroll(10000)
print('Acabou seu Dados')
