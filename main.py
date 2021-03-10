from PyQt5 import uic,QtWidgets
import pytube

def baixar():
    url = primeira_tela.lineEdit.text()

    yt = pytube.YouTube(url)

    video = yt.streams.first()

    video.download()

    primeira_tela.lineEdit.setText("")

    primeira_tela.label_2.setText('CONCLUIDO!')

aplicativo = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("tela.ui")

primeira_tela.pushButton.clicked.connect(baixar)

primeira_tela.show()
aplicativo.exec()
