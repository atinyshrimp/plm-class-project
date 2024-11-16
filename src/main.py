from PyQt5.QtWidgets import QApplication
from components.main_window import PLMApp
import sys
import ctypes

VERSION = "0.1.0"

if __name__ == "__main__":
    # Ensure the icon appears correctly in the Windows taskbar
    myappid = f"mgo_sa.plm_internal_software.{VERSION}"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QApplication(sys.argv)
    window = PLMApp(VERSION)  # Pass the version to the main window
    window.show()
    sys.exit(app.exec_())
