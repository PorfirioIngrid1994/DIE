import flet as ft
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def pesquisar_na_amazon(produto_a_pesquisar):
    browser = webdriver.Chrome()    
    browser.get("https://www.amazon.com.br/ref=nav_logo")
    time.sleep(1)

    # Encontra o elemento pelo ID
    input_pesquisa = browser.find_element(By.ID, "twotabsearchtextbox")
    input_pesquisa.send_keys(produto_a_pesquisar)

    botao_pesquisar = browser.find_element(By.ID, "nav-search-submit-button")
    botao_pesquisar.click()

    # Encontra todos os elementos que contêm o preço dos produtos
    array_preco = browser.find_elements(By.CSS_SELECTOR, '.a-price-whole')

    array_descricao = browser.find_elements(By.CSS_SELECTOR, 'span.a-text-normal')

    # elemento = browser.find_element_by_xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']")

    for descricao in array_descricao:
        print(f'{descricao.text} \n')

    
    # Imprime os preços dos produtos encontrados
    for preco in array_preco:
        print(f'{preco.text} \n')

    

    for descricao, preco in zip(array_descricao, array_preco):
        print(f'{descricao.text} - {preco.text}')

    # Encontra todos os elementos desejados usando um caminho de árvore DOM

    # Itera sobre a lista de elementos e obtém o texto de cada um
    # for elemento in elementos:
    #     texto_do_elemento = elemento.text
    #     print(texto_do_elemento)    
    
    # Fecha o navegador após concluir a pesquisa
    browser.quit()


def main(page: ft.Page):
    page.title = "Projeto DIE - Pesquisa de compras"

    page.window_width = 400
    page.window_height = 600
    def button_clicked(e):
        t.value = f"Pesquisando...  {tb5.value}"
        produto_a_pesquisar = {tb5.value}
        pesquisar_na_amazon(produto_a_pesquisar)
        page.update()

    t = ft.Text()

    tb5 = ft.TextField(label="Procurar por:", icon=ft.icons.SEARCH_SHARP)
    b = ft.ElevatedButton(text="Pesquisar", on_click=button_clicked)
    page.add(tb5, b, t)

    page.add(
        ft.DataTable(
            bgcolor="#E3E3E8", # amarelo 
            width=390,
            height=350,
            columns=[
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("Descrição")),
                ft.DataColumn(ft.Text("Preço"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Geladeira")),
                        ft.DataCell(ft.Text("Bla bla bla")),
                        ft.DataCell(ft.Text("43,50")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Jack")),
                        ft.DataCell(ft.Text("Brown")),
                        ft.DataCell(ft.Text("19")),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Alice")),
                        ft.DataCell(ft.Text("Wong")),
                        ft.DataCell(ft.Text("25")),
                    ],
                ),
            ],
        ),
    )

ft.app(target=main)

