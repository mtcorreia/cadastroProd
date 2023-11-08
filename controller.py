from PyQt5 import uic, QtWidgets;
import mysql.connector;

# Conexão com o banco de dados local.
banco = mysql.connector.connect (
    host="localhost",
    user="root",
    passwd="",
    database="cadastro"
)

# Função de Cadastro do produto.
def cadastro_tela():
    codigo = formulario.lineEdit.text()
    prod = formulario.lineEdit_2.text()
    preco = formulario.lineEdit_3.text()

    categoria = ""

    print("Codigo:", codigo)
    print("Descricao:", prod)
    print("Preco:", preco)

    if formulario.radioButton.isChecked() :
        print("\nCategoria 'Informatica' selecionado.")
        categoria =  "Informatica"
    elif formulario.radioButton_2.isChecked() :
        print("\nCategoria 'Eletronico' selecionado.")
        categoria =  "Eletronico"
    else:
        print("\nCategoria 'Outros' selecionado.")
        categoria =  "Outros"

    # Inserção de valores no Banco de Dados
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s, %s, %s, %s)" 
    dados = (str(codigo), str(prod), str(preco), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()

# Função de limpeza dos campos de edição do usuário.
def limpar_campos():
    codigo = formulario.lineEdit.text()
    prod = formulario.lineEdit_2.text()
    preco = formulario.lineEdit_3.text()

    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")

# Tela de Listagem de Produtos do Estoque.
def lista_tela():
    listagem.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    select = cursor.fetchall()
    
    listagem.tableWidget.setRowCount(len(select))
    listagem.tableWidget.setColumnCount(5)

    for i in range(0, len(select)):
        for j in range(0, 5):
            listagem.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(select[i][j])))

def deletar_produto():
    linha = listagem.tableWidget.currentRow()
    listagem.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    select = cursor.fetchall()
    valor_id = select[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id=" + str(valor_id))


app=QtWidgets.QApplication([])
formulario = uic.loadUi("cadastro.ui")
listagem = uic.loadUi("lista.ui")

# Acionamento por clique da tela DE CADASTRO.
formulario.pushButton.clicked.connect(cadastro_tela)
formulario.pushButton_2.clicked.connect(lista_tela)
formulario.pushButton_3.clicked.connect(limpar_campos)

# Acionamento por clique da tela DE LISTA.
listagem.pushButton_3.clicked.connect(deletar_produto)

formulario.show()
app.exec()