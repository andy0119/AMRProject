#new
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QProgressBar, QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QPainter, QPen, QFont
from PyQt5.QtCore import Qt

class SpeedDial(QWidget):
    def __init__(self):
        super().__init__()
        self.value = 10
        self.setFixedSize(200, 120)  # 設置固定大小為200x120像素

    def setValue(self, value):
        self.value = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        rect = self.rect()
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)  # 設置背景為白色
        painter.drawRect(rect)

        painter.setPen(QPen(Qt.black, 2))
        font = QFont('Arial', 20)  # 設置字體和大小
        painter.setFont(font)
        painter.drawText(rect, Qt.AlignCenter, f'{self.value} KM/hr')  # 在文本后面添加单位

class TemperatureWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.temperatureLabel = QLabel('溫度 (°C)')
        self.tempProgressBar = QProgressBar()
        self.tempProgressBar.setRange(-20, 150)
        self.tempProgressBar.setValue(26)  # 示例值
        self.tempValueLabel = QLabel('26°C')

        layout.addWidget(self.temperatureLabel)
        layout.addWidget(self.tempProgressBar)
        layout.addWidget(self.tempValueLabel)

        self.setLayout(layout)

class HumidityWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.humidityLabel = QLabel('濕度 (%)')
        self.humidityProgressBar = QProgressBar()
        self.humidityProgressBar.setRange(0, 100)
        self.humidityProgressBar.setValue(50)  # 示例值
        self.humidityValueLabel = QLabel('50%')

        layout.addWidget(self.humidityLabel)
        layout.addWidget(self.humidityProgressBar)
        layout.addWidget(self.humidityValueLabel)

        self.setLayout(layout)

class AMRDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainLayout = QHBoxLayout()

        for i in range(3):  # 可調整AMR部分的數量
            groupBox = QGroupBox(f'AMR {i+1}')
            sectionLayout = QVBoxLayout()

            # 車輛圖標
            carLabel = QLabel(self)
            pixmap = QPixmap('car.png')  # 確保car.png在當前目錄下或提供正確的路徑
            carLabel.setPixmap(pixmap)
            carLabel.setAlignment(Qt.AlignCenter)

            # 緯度和經度
            latLabel = QLabel('緯度 (lat): 25.042')
            lonLabel = QLabel('經度 (lon): 121.535')

            # 方向和速度顯示
            directionLabel = QLabel('方向')
            directionValueLabel = QLabel('90° 北')  # 初始值
            directionValueLabel.setStyleSheet('background-color: white;')
            directionValueLabel.setAlignment(Qt.AlignCenter)
            directionValueLabel.setFixedSize(200, 120)  # 與SpeedDial相同的大小設置
            font = QFont('Arial', 20)  # 設置字體和大小
            directionValueLabel.setFont(font)

            speedLabel = QLabel('速度 (KM/hr)')
            speedDial = SpeedDial()
            speedDial.setValue(10)
            speedValueLabel = QLabel('')
            speedValueLabel.setAlignment(Qt.AlignCenter)
            speedValueLabel.setFont(font)

            # 添加到sectionLayout中
            sectionLayout.addWidget(latLabel)
            sectionLayout.addWidget(lonLabel)

            directionSpeedLayout = QHBoxLayout()
            directionLayout = QVBoxLayout()
            directionLayout.addWidget(directionLabel)
            directionLayout.addWidget(directionValueLabel)
            directionSpeedLayout.addLayout(directionLayout)

            speedLayout = QVBoxLayout()
            speedLayout.addWidget(speedLabel)
            speedLayout.addWidget(speedDial)
            speedLayout.addWidget(speedValueLabel)
            directionSpeedLayout.addLayout(speedLayout)

            sectionLayout.addLayout(directionSpeedLayout)

            # 添加電池信息到佈局中
            batteryLayout = QVBoxLayout()
            batteryLabel = QLabel('電池狀態')
            batteryLayout.addWidget(batteryLabel)

            powerByUGVLabel = QLabel('UGV供電')
            powerByUGVBar = QProgressBar()
            powerByUGVBar.setRange(0, 100)
            powerByUGVBar.setValue(75)  # 示例值
            powerByUGVLayout = QVBoxLayout()
            powerByUGVLayout.addWidget(powerByUGVLabel)
            powerByUGVLayout.addWidget(powerByUGVBar)
            batteryLayout.addLayout(powerByUGVLayout)

            powerForECULabel = QLabel('ECU供電')
            powerForECUBar = QProgressBar()
            powerForECUBar.setRange(0, 100)
            powerForECUBar.setValue(50)  # 示例值
            powerForECULayout = QVBoxLayout()
            powerForECULayout.addWidget(powerForECULabel)
            powerForECULayout.addWidget(powerForECUBar)
            batteryLayout.addLayout(powerForECULayout)

            sectionLayout.addLayout(batteryLayout)

            # 添加電壓和電流信息到佈局中
            voltageLabel = QLabel('電壓 (V)')
            voltageValue = QLabel('49.299')  # 示例值
            voltageECULabel = QLabel('ECU電壓 (V)')
            voltageECUValue = QLabel('24.0')  # 示例值
            currentLabel = QLabel('電流 (A)')
            currentValue = QLabel('0.46')  # 示例值
            currentECULabel = QLabel('ECU電流 (A)')
            currentECUValue = QLabel('0.0')  # 示例值

            voltageLayout = QHBoxLayout()
            voltageLayout.addWidget(voltageLabel)
            voltageLayout.addWidget(voltageValue)
            voltageLayout.addWidget(voltageECULabel)
            voltageLayout.addWidget(voltageECUValue)
            sectionLayout.addLayout(voltageLayout)

            currentLayout = QHBoxLayout()
            currentLayout.addWidget(currentLabel)
            currentLayout.addWidget(currentValue)
            currentLayout.addWidget(currentECULabel)
            currentLayout.addWidget(currentECUValue)
            sectionLayout.addLayout(currentLayout)

            # 添加溫度和濕度信息到佈局中
            temperatureWidget = TemperatureWidget()
            humidityWidget = HumidityWidget()

            sectionLayout.addWidget(temperatureWidget)
            sectionLayout.addWidget(humidityWidget)

            # 添加車輛圖標到佈局中
            sectionLayout.addWidget(carLabel)

            groupBox.setLayout(sectionLayout)
            mainLayout.addWidget(groupBox)

        self.setLayout(mainLayout)
        self.setWindowTitle('AMR 儀表板')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AMRDashboard()
    sys.exit(app.exec_())
