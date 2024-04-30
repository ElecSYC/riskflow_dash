import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Información aquí")
        layout.addWidget(self.label)

        self.button = QPushButton("Actualizar")
        self.button.clicked.connect(self.actualizar_informacion)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def actualizar_informacion(self):
        # Aquí puedes ejecutar tus funciones para obtener nueva información
        # y actualizar la etiqueta
        nueva_informacion = "Nueva información"
        self.label.setText(nueva_informacion)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())
