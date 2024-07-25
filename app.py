import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QComboBox, QLabel, QTextBrowser, QSizePolicy, QStatusBar, QTextEdit, QHBoxLayout, QVBoxLayout)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap, QCursor
import markdown
from my_widgets import ImageDropLabel
from pyollama import run_multimodel_models, convert_nanoseconds_to_seconds, list_models_names

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 800, 600
        self.setMinimumSize(self.window_width, self.window_height)
        self.setWindowTitle(f'Ollama - LLava v1.0.0')
        self.setWindowIcon(QIcon('./icons/icon.png'))
        self.setObjectName('mainwindow')
        self.setStyleSheet('''
            font-size: 16px;
        ''')

        self.layout = {}
        self.layout['main'] = QVBoxLayout()
        self.setLayout(self.layout['main'])

        self.layout['main_sub'] = QHBoxLayout()
        self.layout['main'].addLayout(self.layout['main_sub'])

        self.init_ui()

    def init_ui(self):
        self.layout['column1_main'] = QVBoxLayout()
        self.layout['main_sub'].addLayout(self.layout['column1_main'])

        self.layout['column2_main'] = QVBoxLayout()
        self.layout['main_sub'].addLayout(self.layout['column2_main'])
        
        self.combo_box = QComboBox()
        self.combo_box.setFixedWidth(250)
        self.combo_box.addItems(models_list)
        self.layout['column1_main'].addWidget(self.combo_box)

        self.image_label = ImageDropLabel()
        self.layout['column1_main'].addWidget(self.image_label)

        self.layout['column1_main'].addStretch()

        self.layout['prompt'] = QVBoxLayout()
        self.layout['column2_main'].addLayout(self.layout['prompt'])

        self.prompt_input = QTextEdit()
        self.prompt_input.setFixedHeight(400)
        self.prompt_input.setPlaceholderText('Enter your prompt here ...')
        self.layout['prompt'].addWidget(self.prompt_input)
        self.layout['prompt'].setAlignment(self.prompt_input, Qt.AlignmentFlag.AlignTop)

        self.response_output = QTextBrowser()
        self.response_output.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layout['prompt'].addWidget(self.response_output)

        self.layout['buttons'] = QHBoxLayout()
        self.layout['prompt'].addLayout(self.layout['buttons'])

        self.btn_generate = QPushButton('&Send', clicked=self.run_model)
        self.btn_generate.setFixedWidth(150)
        self.btn_generate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.layout['buttons'].addStretch(100)
        self.layout['buttons'].addWidget(self.btn_generate)
        self.layout['buttons'].addSpacing(10)

        self.btn_clear = QPushButton('&Reset', clicked=self.reset)
        self.btn_clear.setFixedWidth(75)
        self.btn_clear.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.layout['buttons'].addWidget(self.btn_clear)

        self.status_bar = QStatusBar()
        self.layout['main'].addWidget(self.status_bar)

        if ollama_offline:
            self.status_bar.showMessage('Ollama Offline')
        else:
            self.status_bar.showMessage('Ollama Online')

    def run_model(self):
        if self.image_label.image_data is None:
            self.status_bar.showMessage('No image to process. Please upload an image')
            return
        
        prompt = self.prompt_input.toPlainText()
        if not prompt.strip():
            self.status_bar.showMessage('Prompt is empty')
            return
        
        model = self.combo_box.currentText()
        response = run_multimodel_models(
            model=model,
            prompt=prompt,
            images=[self.image_label.image_data]
        )

        html = markdown.markdown(response['response'].strip(), extensions=['nl2br'])

        self.response_output.clear()
        self.response_output.append(html + '\n\n')

        self.status_bar.showMessage(f'Total duration : {convert_nanoseconds_to_seconds(response["total_duration"]):.2f} second. Tokens (prompt): {response.get("promp_evalcount", 0)}. Token (respon): {response["eval_count"]}.')

    def reset(self):
        self.image_label.setPixmap(QPixmap())
        self.image_label.setText("\n\n Drop Image Here \n - or - \n Click to Upload \n\n")
        self.prompt_input.clear()
        self.response_output.clear()
        self.status_bar.clearMessage()

if __name__ == '__main__':
    multi_models = ['llava']
    try:
        models_list = []
        available_models = list_models_names()
        for model in multi_models:
            for model_2 in available_models:
                if model in model_2:
                    models_list.append(model_2)
                    llama_available = True
        else:
            llama_available = False

        ollama_offline = False
    except httpx.ConnectError:
        models = []
        ollama_offline = True

    app = QApplication(sys.argv)

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window ...')