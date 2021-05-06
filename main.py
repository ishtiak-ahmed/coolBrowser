import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https:/youtube.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
#         navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        back_btn = QAction('←', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        forward_btn = QAction('→', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        refresh_btn = QAction('↻', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigateHome)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigateHome(self):
        self.browser.setUrl(QUrl('https://github.com/ishtiak-ahmed'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Ishtiak Secured Browser')
window = MainWindow()
app.exec_()
