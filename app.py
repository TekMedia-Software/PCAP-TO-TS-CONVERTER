
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout,
    QWidget, QLabel, QProgressBar, QMessageBox, QListWidget
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
import sys
from internal.pcap_parser import generate_ts_from_pcap  # Ensure this points to the updated backend

class ConversionWorker(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(bool, str)

    def __init__(self, file_paths):
        super().__init__()
        self.file_paths = file_paths

    def run(self):
        # Call the conversion function and handle success/failure
        success, message = generate_ts_from_pcap(self.file_paths)
        if success:
            self.progress.emit(100)
            self.finished.emit(True, message)
        else:
            self.finished.emit(False, message)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PCAP to TS Converter")
        #self.setGeometry(100, 100, 800, 600)  # Increased size for better visibility
        self.setStyleSheet("background-color: white;")  # Set background to white
        self.init_ui()
        
        # Disable the maximize button and resize functionality
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # Remove maximize button
        self.setFixedSize(800, 600)  # Prevent window resizing (optional)

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Add logo image at the top center with reduced size
        logo_label = QLabel()
        logo_pixmap = QPixmap("./static/Logo.png")  # Replace with the path to your logo image
        scaled_pixmap = logo_pixmap.scaled(200, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Resize the logo
        logo_label.setPixmap(scaled_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(logo_label)

        # Title label with pink text color and larger font size
        title_label = QLabel("PCAP to TS Converter")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 26px; color: #D91656; margin-bottom: 20px; font-weight: bold;")
        self.layout.addWidget(title_label)

        # Button to select PCAP files with blue border and hover effect
        self.select_pcap_button = QPushButton("Select PCAP Files")
        self.select_pcap_button.clicked.connect(self.select_pcap_files)
        self.select_pcap_button.setStyleSheet("""
            QPushButton {
                font-weight:bold;
                padding: 12px; font-size: 16px; color: white; background-color: #78B3CE;
                border: 2px solid #78B3CE; border-radius: 5px; margin: 10px 0;
            }
            QPushButton:hover { background-color: #78B3CE; color: #D91656; }
            QPushButton:pressed { background-color: #66A7C1; color: #D91656; }
        """)
        self.layout.addWidget(self.select_pcap_button)

        # List widget to show selected files
        self.pcap_list = QListWidget()
        self.layout.addWidget(self.pcap_list)

        # Convert button with similar style (blue border and hover effect)
        self.convert_button = QPushButton("Convert to TS")
        self.convert_button.clicked.connect(self.convert_to_ts)
        self.convert_button.setEnabled(False)
        self.convert_button.setStyleSheet("""
            QPushButton {
                font-weight:bold;
                padding: 12px; font-size: 16px; color: white; background-color: #78B3CE;
                border: 2px solid #78B3CE; border-radius: 5px; margin: 10px 0;
            }
            QPushButton:hover { background-color: #78B3CE; color: #D91656; }
            QPushButton:pressed { background-color: #66A7C1; color:#D91656;}
            QPushButton:disabled {color: #D91656;}
        """)
        self.layout.addWidget(self.convert_button)

        # Progress bar with updated colors for chunk and border
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                height: 20px; border: 2px solid #78B3CE; border-radius: 5px; text-align: center;
            }
            QProgressBar::chunk { background-color: #78B3CE; border-radius: 5px; }
        """)
        self.layout.addWidget(self.progress_bar)

        # Container for layout
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def select_pcap_files(self):
        options = QFileDialog.Options()
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Select PCAP Files", "", "PCAP Files (*.pcap);;All Files (*)", options=options)
        if file_paths:
            self.pcap_list.clear()  # Clear previous selections
            self.pcap_list.addItems(file_paths)  # Display selected files
            self.selected_pcap_files = file_paths
            self.convert_button.setEnabled(True)
        
    def convert_to_ts(self):
        # Change the button text and disable it
        self.convert_button.setText("Converting!")
        self.convert_button.setEnabled(False)
        self.progress_bar.setValue(0)
        self.worker = ConversionWorker(self.selected_pcap_files)
        self.worker.progress.connect(self.update_progress_bar)
        self.worker.finished.connect(self.on_conversion_finished)
        self.worker.start()

    def update_progress_bar(self, value):
        self.progress_bar.setValue(value)
        self.progress_bar.setFormat(f"{value}%")

    def on_conversion_finished(self, success, message):
        if success:
            QMessageBox.information(self, "Success", message)
            self.progress_bar.setValue(100)  # Set to 100% to keep it visible
            self.progress_bar.setFormat("100%")  # Update format to show 100%
        else:
            QMessageBox.warning(self, "Error", message)
        
        # Restore the button text and re-enable it
        self.convert_button.setText("Convert to TS")
        self.convert_button.setEnabled(True)
        self.progress_bar.setFormat("0%")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
