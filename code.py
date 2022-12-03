import sys
import cv2
import qrcode
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui

#........This is main UI class
class Mygui(QMainWindow):
    
    def __init__(self):                #  To load the UI
        super(Mygui,self).__init__()
        uic.loadUi("QrCodeGUI.ui",self)
        self.show()
# .........This code connects the buttons to the fuction when triggered
        self.current_file=""
        self.actionOpen.triggered.connect(self.open_image)
        self.actionSave.triggered.connect(self.save_image)
        self.actionQuit.triggered.connect(self.quit)
        self.pushButton.clicked.connect(self.generate_code)
        self.pushButton_2.clicked.connect(self.read_code)



# .......fuction for opening the QR code in the app
    def open_image(self):
        options =QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self,"open File", "","All files (*)",options=options)
        if filename!="":
            self.current_file=filename
            pixmap= QtGui.QPixmap(self.current_file)
            pixmap= pixmap.scaled(600,600)
            self.label.setScaledContents(True)
            self.label.setPixmap(pixmap)



# .......fuction for Saving The QR code in the app
    def save_image(self):
        options= QFileDialog.Options()
        filename,_= QFileDialog.getSaveFileName(self, "Save File","","PNG (*.png)",options=options)
        if filename!="":
            img=self.label.pixmap()
            img.save(filename,"PNG")

    def quit(self):
        sys.quit()



# .......fuction for generating the qr code from the written text.............
    def generate_code(self):
        qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=2) 
        qr.add_data(self.textEdit.toPlainText())
        qr.make(fit=True)

        img=qr.make_image(fill_color="black", back_color="white")#..............MAIN CODE TEXT CHANGING INTO QRCODE
        
        img.save("currentqr.png")
        pixmap=QtGui.QPixmap("currentqr.png")
        pixmap=pixmap.scaled(600,600)
        self.label.setScaledContents(True)
        self.label.setPixmap(pixmap)

        

# .......function for decoding the QR code
    def read_code(self):
        img=cv2.imread(self.current_file)
        detector= cv2.QRCodeDetector()
        data,_,_= detector.detectAndDecode(img)
        self.textEdit.setText(data)





#...............................DRIVER OR MAIN CODE STARTS HERE....................
def main():
    app=QApplication([])
    window=Mygui()  
    app.exec_()      
if __name__=="__main__":
    main()
