import flet as ft

def main(page: ft.Page):
    page.title = "Projeto DIE - Pesquisa de compras"

    page.window_width = 400
    page.window_height = 600

    def button_clicked(e):
        t.value = f"Pesquisando...  {tb5.value}"
        page.update()

    t = ft.Text()

    tb5 = ft.TextField(label="Procurar por:", icon=ft.icons.SEARCH_SHARP)
    b = ft.ElevatedButton(text="Pesquisar", on_click=button_clicked)
    page.add(tb5, b, t)

    # page.add(
    #     ft.Container(
            
    #         # width=390,
    #         # height=400,
    #         bgcolor="#D9D7E8", # amarelo          

    #     )
    # )

    page.add(
        ft.DataTable(
            bgcolor="#E3E3E8", # amarelo 
            width=390,
            height=300,
            columns=[
                ft.DataColumn(ft.Text("First name")),
                ft.DataColumn(ft.Text("Last name")),
                ft.DataColumn(ft.Text("Age"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("John")),
                        ft.DataCell(ft.Text("Smith")),
                        ft.DataCell(ft.Text("43")),
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

