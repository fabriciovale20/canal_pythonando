import flet as ft
from models import Produto
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#### CONEXÃO BANCO DE DADOS ####

# Criando conexão
CONN = 'sqlite:///app_mobile_flet/appflet.db'

# Criando sessão
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Função da Interface (Botão, texto etc)
def main(page: ft.Page):
    # Título do App
    page.title = 'Cadastro App'

    # Lista de Produtos
    lista_produtos = ft.ListView()

    # Função Cadastrar Produto
    def cadastrar(e):
        # Laço de repetição para verificação do sucesso ou erro no cadastro
        try:
            # Coletando os valores inseridos
            novo_produto = Produto(titulo=produto.value, preco=preco.value)

            # Adicionando produto coletado ao banco de dados
            session.add(novo_produto)
            session.commit()

            # Exibindo os produtos cadastrado na tela do app
            lista_produtos.controls.append(ft.Container(
                    ft.Text(produto.value),
                    bgcolor=ft.colors.BLACK12,
                    padding=15,
                    alignment=ft.alignment.center,
                    margin=3,
                    border_radius=10
                ))
            
            # Cadastro com sucesso
            txt_erro.visible = False # Oculta a mensagem de erro
            txt_acerto.visible = True # Exibe a mensagem de sucesso
        except:
            # Erro no cadastro
            txt_erro.visible = True # Exibe a mensagem de erro
            txt_acerto.visible = False # Oculta a mensagem de sucesso

        # Atualizar página do app após cadastro do produto
        page.update()

        # Mensagem de produto cadastrado
        print('Produto cadastrado!')

    # Variáveis de mensagem de erro ou sucesso ao tentar realizar o cadastro de novos produtos
    txt_erro = ft.Container(ft.Text('Erro ao salvar o produto!'), visible=False, bgcolor=ft.colors.RED, padding=10, alignment=ft.alignment.center)
    txt_acerto = ft.Container(ft.Text('Produto salvar com sucesso!'), visible=False, bgcolor=ft.colors.GREEN, padding=10, alignment=ft.alignment.center)


    #### Informações do produto ####
        
    # Título do Produto
    txt_titulo = ft.Text('Título do produto: ')
    produto = ft.TextField(label='Digite o titulo do produto...', text_align=ft.TextAlign.LEFT) # Input para inserir título do produto

    # Preço do Produto
    txt_preco = ft.Text('Preço do produto')
    preco = ft.TextField(value='0', label='Digite o preço do produto', text_align=ft.TextAlign.LEFT) # Input para inserir o preço do produto

    # Botão
    btn_produto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)


    # Adicionando elementos a página para ser exibido
    page.add(
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btn_produto,
        txt_acerto,
        txt_erro
        )
    
    # Laço de repetição para acessar e coletar todos os produtos cadastrados no banco de dados
    for p in session.query(Produto).all():
        lista_produtos.controls.append(
            ft.Container(
                ft.Text(p.titulo),
                bgcolor=ft.colors.BLACK12,
                padding=15,
                alignment=ft.alignment.center,
                margin=3,
                border_radius=10
            )
        )

    # Adicionando a listagem de produtos para ser exibidana  página no app
    page.add(
        lista_produtos,
    )

# Inicializando o aplicativo
ft.app(target=main)
