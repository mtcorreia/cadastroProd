from PyQt5 import uic, QtWidgets;
import mysql.connector;

banco = mysql.connector.connect (
    host="localhost",
    user="root",
    passwd="",
    database="cadastro"
)

def funcao_principal():
    codigo = cadastro.lineEdit.text()
    desc = cadastro.lineEdit_2.text()
    preco = cadastro.lineEdit_3.text()

    categoria = ""

    print("Codigo:", codigo)
    print("Descricao:", desc)
    print("Preco:", preco)

    if cadastro.radioButton.isChecked() :
        print("\nCategoria 'Informatica' selecionado.")
        categoria =  "Informatica"
    elif cadastro.radioButton_2.isChecked() :
        print("\nCategoria 'Alimento' selecionado.")
        categoria =  "Alimento"
    else:
        print("\nCategoria 'Eletronico' selecionado.")
        categoria =  "Eletronico"

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s, %s, %s, %s)" 
    dados = (str(codigo), str(desc), str(preco), categoria)
    cursor.execute(comando_SQL, dados)
    banco.commit()

app=QtWidgets.QApplication([])
cadastro = uic.loadUi("cadastro.ui")
cadastro.pushButton.clicked.connect(funcao_principal)

cadastro.show()
app.exec()