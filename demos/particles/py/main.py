# main.py

import sys
import simulation
from PySide6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QTimer
from viewer import Viewer

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Subtle Machine - Gravity Control")
        self.viewer = Viewer(simulation)

        self.label = QLabel("Gravity: 0.0")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.change_gravity)

        layout = QVBoxLayout()
        layout.addWidget(self.viewer.canvas.native)
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_simulation)
        self.timer.start(16)  # ~60 FPS

        simulation.initialize()

    def change_gravity(self, value):
        gravity = value / 10.0  # scale from 0.0 to 10.0
        self.label.setText(f"Gravity: {gravity:.1f}")
        simulation.set_gravity(gravity)

    def update_simulation(self):
        simulation.step(0.016)
        self.viewer.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
