from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from static.ui_interface import Ui_MainWindow
from features.network import wordCollection, tokenize
from features.communicate import takecommand, speak
from features.model import Brain
from features.task import *

import sys
import random
import json
import torch
import os
import cv2
import mediapipe as mp

class Worker(QObject):
    left_dataEmmited = pyqtSignal(str)
    right_dataEmmited = pyqtSignal(int)
    close = pyqtSignal()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open("static/intents.json", "r") as jsonData:
        intents = json.load(jsonData)

    FILE = "static/trainedData.pth"
    data = torch.load(FILE)

    modelState = data['model_state']
    inputSize = data['input_size']
    hiddenSize = data['hidden_size']
    outpurSize = data['output_size']
    allWords = data['all_words']
    tags = data['tags']

    model = Brain(inputSize, hiddenSize, outpurSize).to(device)
    model.load_state_dict(modelState)
    model.eval()

    @pyqtSlot()
    def run(self):
        wishMe()
        while True:
            command = takecommand(self)
            query = str(command)
            
            command = tokenize(command)

            X = wordCollection(command, self.allWords)
            X = X.reshape(1, X.shape[0])
            X = torch.from_numpy(X).to(self.device)

            output = self.model.link(X)
            _, predicted = torch.max(output, dim=1)
            tag = self.tags[predicted.item()]

            prob = torch.softmax(output, dim=1)
            prob = prob[0][predicted.item()]

            if prob.item() > 0.75:
                for intent in self.intents['intents']:
                    if tag == intent['tag']:
                        reply = random.choice(intent['responses'])
                        
                        if tag == "time":
                            self.left_dataEmmited.emit("Calender")
                            self.right_dataEmmited.emit(3)
                            getTime(query)
                        elif tag == "calendar":
                            self.left_dataEmmited.emit("Calendar")
                            self.right_dataEmmited.emit(3)
                            getCalendar(query)
                        elif tag == "wikipedia":
                            self.left_dataEmmited.emit("Search")
                            self.right_dataEmmited.emit(3)
                            patterns = intent['patterns']
                            wikiData(query, patterns)
                        elif tag == "search":
                            self.left_dataEmmited.emit("Search")
                            self.right_dataEmmited.emit(3)
                            patterns = intent['patterns']
                            googleData(query, patterns)
                        elif tag == "google":
                            self.left_dataEmmited.emit("Search")
                            self.right_dataEmmited.emit(3)
                            patterns = intent['patterns']
                            searchGoogle(query, patterns)
                        elif tag == "youtube":
                            self.left_dataEmmited.emit("Search")
                            self.right_dataEmmited.emit(3)
                            patterns = intent['patterns']
                            youtubeData(query, patterns)
                        elif tag == "weather":
                            self.left_dataEmmited.emit("Weather")
                            self.right_dataEmmited.emit(3)
                            getWeather(query)
                        elif tag == "precipitate":
                            self.left_dataEmmited.emit("Weather")
                            self.right_dataEmmited.emit(3)
                            getPrecipitation(query)
                        elif tag == "news":
                            self.left_dataEmmited.emit("News")
                            self.right_dataEmmited.emit(3)
                            getNews(query)
                        elif tag == "multimedia":
                            self.left_dataEmmited.emit("MultiMedia")
                            self.right_dataEmmited.emit(3)
                            playMedia(query)
                        elif tag == "open":
                            self.left_dataEmmited.emit("Applications")
                            self.right_dataEmmited.emit(3)
                            openApp(query)
                        elif tag == "joke":
                            self.right_dataEmmited.emit(3)
                            getJoke()
                        elif tag == "greet":
                            self.right_dataEmmited.emit(3)
                            wishMe(start=False)
                        elif tag == "screenshot":
                            self.left_dataEmmited.emit("System")
                            self.right_dataEmmited.emit(3)
                            getScrnShot()
                        elif tag == "clear_cache":
                            self.left_dataEmmited.emit("System")
                            self.right_dataEmmited.emit(3)
                            clearCache()
                            speak(reply)
                        elif tag == "battery":
                            self.left_dataEmmited.emit("Battery")
                            self.right_dataEmmited.emit(3)
                            getBattery()
                        elif tag == "quick_actions":
                            self.left_dataEmmited.emit("Search")
                            self.right_dataEmmited.emit(3)
                            quickTask(query)
                        elif tag == "restart":
                            self.left_dataEmmited.emit("System")
                            self.right_dataEmmited.emit(3)
                            speak("Restarting...")
                            cv2.destroyAllWindows()
                            os.execv(sys.executable, ['python'] + sys.argv)
                        elif tag == "retrain":
                            self.left_dataEmmited.emit("System")
                            self.right_dataEmmited.emit(3)
                            speak("Retraining...")
                            cv2.destroyAllWindows()
                            os.execv(sys.executable, ["python", "train.py"])
                        elif tag == "error":
                            self.right_dataEmmited.emit(3)
                            self.left_dataEmmited.emit("Report")
                            print("Jessica: ...\n")
                        elif tag == "exit":
                            self.left_dataEmmited.emit("System")
                            self.right_dataEmmited.emit(3)
                            speak(reply)
                            self.close.emit()
                        elif tag == "bye_1":
                            self.right_dataEmmited.emit(3)
                            speak(reply)
                            while True:
                                command = takecommand(self)
                                if "wake up" in command or "wake" in command or "jessica" in command:
                                    self.right_dataEmmited.emit(3)
                                    speak("At your service Master.")
                                    break
                                else:
                                    continue
                        elif tag == "bye_2":
                            import datetime
                            self.right_dataEmmited.emit(3)
                            hour = int(datetime.datetime.now().hour)
                            if hour >= 20 and hour <= 23:
                                speak(reply)
                                self.close.emit()
                            else:
                                speak("Master, You are going to bed too early!")
                        elif tag == "logout":
                            self.left_dataEmmited.emit("System")
                            self.right_dataEmmited.emit(3)
                            logOut(self)
                        elif tag == "shutdown":
                            self.left_dataEmmited.emit("System")
                            self.right_dataEmmited.emit(3)
                            shutDown(self)
                        elif query == "jessica":
                            self.left_dataEmmited.emit("Report")
                            self.right_dataEmmited.emit(3)
                            speak("At your service Master.")
                        else:
                            self.left_dataEmmited.emit("Report")
                            self.right_dataEmmited.emit(3)
                            speak(reply)

class WebCam(QObject):
    test_img = None
    image_emmited = pyqtSignal(QImage)

    minDetectionCon = 0.5
    mpFaceDetection = mp.solutions.face_detection
    mpDraw = mp.solutions.drawing_utils
    faceDetection = mpFaceDetection.FaceDetection(minDetectionCon)

    def findFaces(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        # print(self.results)
        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])
                if draw:
                    img = self.fancyDraw(img,bbox)
        return img, bboxs

    def fancyDraw(self, img, bbox, l=30, t=5, rt= 1):
        try:
            x, y, w, h = bbox
            h1 = int(h/8)
            w1 = int(w/10)
            y = y-int(3.5*h1)
            h = h+int(3*h1)
            x = x-int(1.5*w1)
            w = w+int(3*w1)
            x1, y1 = x + w, y + h
            # print(x, y, w, h)

            if w<800:
                cv2.rectangle(img, (x, y, w, h), (255, 0, 255), rt)
                # Top Left  x,y
                cv2.line(img, (x, y), (x + l, y), (255, 0, 255), t)
                cv2.line(img, (x, y), (x, y+l), (255, 0, 255), t)
                # Top Right  x1,y
                cv2.line(img, (x1, y), (x1 - l, y), (255, 0, 255), t)
                cv2.line(img, (x1, y), (x1, y+l), (255, 0, 255), t)
                # Bottom Left  x,y1
                cv2.line(img, (x, y1), (x + l, y1), (255, 0, 255), t)
                cv2.line(img, (x, y1), (x, y1 - l), (255, 0, 255), t)
                # Bottom Right  x1,y1
                cv2.line(img, (x1, y1), (x1 - l, y1), (255, 0, 255), t)
                cv2.line(img, (x1, y1), (x1, y1 - l), (255, 0, 255), t)
                return img
            else:
                return img
        except Exception as e:
            log(e)

    @pyqtSlot()
    def run(self):
        self.cap = cv2.VideoCapture(0)
        while self.cap.isOpened():
            try:
                success, img = self.cap.read()
                img = cv2.resize(img, (1920, 1040))
                img = cv2.flip(img, 1)
                img, bboxs = self.findFaces(img)
                img = QImage(img, img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888).rgbSwapped()
                self.image_emmited.emit(img)
            except Exception as e:
                log(e)

class Network(QObject):
    data_emmited = pyqtSignal(str, int, str)

    @pyqtSlot()
    def run(self):
        while True:
            import socket
            import pythonping

            ip_address = str(socket.gethostbyname(socket.gethostname()))

            try:
                ping_result = pythonping.ping(target='google.com', timeout=2)
                ping = int(ping_result.rtt_avg_ms)
                if ping < 1000:
                    ping = ping
                    stylesheet = "background: none; color: rgb(255, 255, 255); font: 14pt \"Orbitron\";"
                else:
                    ping = 999
                    stylesheet = "background: none; color: rgb(255, 0, 0); font: 14pt \"Orbitron\";"
                self.data_emmited.emit(ip_address, ping, stylesheet)
            except Exception as e:
                log(e)
                ping = 999
                stylesheet = "background: none; color: rgb(255, 0, 0); font: 14pt \"Orbitron\";"
                self.data_emmited.emit(ip_address, ping, stylesheet)


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Jessica")
        self.showMaximized()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.close_button.clicked.connect(self.quit)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(Qt.white)
        shadow.setXOffset(1)
        shadow.setYOffset(1)
        self.title.setGraphicsEffect(shadow)

        self.start()
        

    def start(self):

        self.prompt_box.hide()

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.animate_progress)
        self.timer1.start(1000)
        
        self.animate_progress()
        self.animate_opmenu(label_no=3)
        self.add_memory()
        self.scroll('Report')

        self.th1 = QThread()
        self.th2 = QThread()
        self.th3 = QThread()

        self.worker = Worker()
        self.cam = WebCam()
        self.network = Network()

        self.worker.moveToThread(self.th1)
        self.cam.moveToThread(self.th2)
        self.network.moveToThread(self.th3)

        self.worker.left_dataEmmited.connect(self.scroll)
        self.worker.right_dataEmmited.connect(self.animate_opmenu)
        self.worker.close.connect(self.quit)
        self.cam.image_emmited.connect(self.set_webCam)
        self.network.data_emmited.connect(self.set_networkInfo)

        self.th1.started.connect(self.worker.run)
        self.th2.started.connect(self.cam.run)
        self.th3.started.connect(self.network.run)

        self.th1.start()
        self.th2.start()
        self.th3.start()

    def quit(self):
        self.th3.quit()
        self.th2.quit()
        self.th1.quit()
        self.cam.cap.release()
        cv2.destroyAllWindows()
        self.close()

    def set_webCam(self, image):
        try:
            self.centralwidget.setPixmap(QPixmap.fromImage(image))
        except Exception as e:
            log(e)

    def animate_opmenu(self, label_no:int):
        self.anim1 = QPropertyAnimation(self.animated_label, b"pos")
        label_ypos = self.animated_label.geometry().y()
        if label_no == 1:
            label_ypos = 215
        elif label_no == 2:
            label_ypos = 352
        elif label_no == 3:
            label_ypos = 489
        elif label_no == 4:
            label_ypos = 626
        elif label_no == 5:
            label_ypos = 763
        self.anim1.setEndValue(QPoint(1610, label_ypos))
        self.anim1.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim1.setDuration(2000)
        self.anim1.start()
        
    def scroll(self, scroll_to: str):
        for x in range(self.command_list.count()):
            item = self.command_list.item(x)
            if scroll_to.lower() in item.text().lower():
                item.setSelected(True)
                self.command_list.scrollToItem(item, QAbstractItemView.PositionAtCenter)
            else:
                pass

    def animate_progress(self):
        import psutil
        cpu_usage = int(psutil.cpu_percent())
        ram_usage = int(psutil.virtual_memory()[2])
        disk_usage = int(psutil.disk_usage("/")[3])

        self.cpu_progressBar.setValue(cpu_usage)
        self.ram_progressBar.setValue(ram_usage)
        self.disk_progressBar.setValue(disk_usage)

    def set_networkInfo(self, ip_address, ping, stylesheet):
        self.ip_label.setText(ip_address)
        self.ping_label.setStyleSheet(stylesheet)
        self.ping_label.setText(str(ping))

    def add_memory(self):
        self.command_list.addItem("M01 : Report")
        self.command_list.addItem("M02 : File")
        self.command_list.addItem("M03 : Message")
        self.command_list.addItem("M04 : Search")
        self.command_list.addItem("M05 : MultiMedia")
        self.command_list.addItem("M06 : Battery")
        self.command_list.addItem("M07 : Weather")
        self.command_list.addItem("M08 : Calendar")
        self.command_list.addItem("M09 : News")
        self.command_list.addItem("M10 : Applications")
        self.command_list.addItem("M11 : System")

        self.command_list.setAutoScroll(True)
        self.command_list.setDisabled(True)
        self.command_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
