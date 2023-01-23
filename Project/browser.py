import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout, QWidget)
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Browser(QWidget):

    def __init__(self):
        super().__init__()


        self.view = QWebEngineView(self)
        self.view.load(QUrl("http:cda.docs.lan"))

        self.back_button = QPushButton("<", self)
        self.forward_button = QPushButton(">", self)
        self.refresh_button = QPushButton("Refresh", self)

        self.back_button.clicked.connect(self.view.back)
        self.forward_button.clicked.connect(self.view.forward)
        self.refresh_button.clicked.connect(self.view.reload)

        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        layout = QVBoxLayout(

        )
        layout.addWidget(self.view)

        button_layout = QHBoxLayout ()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.url_bar)

        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.view.setUrl(q)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    browser = Browser()
    browser.show()

    sys.exit(app.exec_())


