# PROJEKTI OHJELMOINNIN PERUSTEITA VARTEN

# Tee Viikkoaikataulu-järjestelmä. Tämä voi olla esim. perheen/työpaikan sisäistä aikataulutusta varten.

# Vaatimukset:
#     -hyvin dokumentoitu, käytä docstring-systeemiä (https://realpython.com/documenting-python-code/)
#       - NOTE [Saaga 15/08/22]: Graaffisessa ympäristössä ei tarvetta. Tee interaktiivinen tutoriaali sen sijaan
#     -toimii komentoriviltä/python shellissa, ei graafista käyttöliittymää
#       - NOTE [Saaga 15/08/22] Graaffinen liittymä sallitty
#     -on tehty olio-ohjelmoinnilla. Tarvitset todennäköisesti ainakin:henkilo,tehtava,aikataulu-oliot.
#       - NOTE [Saaga 15/08/22] O_o miten muutenkaan? Jos arvostat omaa aikaasi, niin käytät olioita
#     -tiedot tallennetaan tiedostoon sessioiden välillä, joten voidaan jatkaa siitä mihin jäätiin.
#     -voit tallentaa tiedot joko tekstinä tai picklen avulla olioina
#       - NOTE [Saaga 15/08/22] Tai omalla binääri-formaatilla
#     -viikko on jaettu 112 slottiin, joita on joka päivä 16 (kello 8 - 24)
#       - NOTE [Saaga 15/08/22] Koodarit eivät tiedä TOSseista, joten tästä tulee 24h-kalenteri, missä valittavana koodari-mode
#       - EI tullut koodari-modea
#     

# Toiminnot:
#     -lisää henkilö
#       TODO [Saaga 15/08/22]
#       DONE
#     -lisää tehtävä
#       TODO [Saaga 15/08/22]
#       DONE
#     -lisää tehtävä henkilölle johonkin tiettyyn aikaslottiin
#       TODO [Saaga 15/08/22]
#       DONE
#     -listaa kaikki henkilöt
#       TODO [Saaga 15/08/22]
#       DONEISH
#     -listaa koko viikon henkilöt ja tapahtumat
#       TODO [Saaga 15/08/22]
#       DONE
#     Testiajo 
#       NOTE [Saaga 15/08/22] tee tutoriaali
#       DNF
#       -käyttäen ylläolevia toimintoja lisää henkilöitä ja tehtäviä
#       -(voit tehdä testiohjelman joka tayttää ylläolevat satunnaisesti)
#       -testaa että järjestelmä toimii kunnolla, henkilöillä ei ole päällekkäisiä hommia
#       -kaikki hommat tulevat tehdyksi jne.
#     Bonushommat
#     -lisää rajoitteita henkilölle (esim. ei voi tehdä kuin 6 tuntia juttuja viikonloppuna)
#       TODO [Saaga 15/08/22]
#       Lisätty globaali rajoite, muokattavissa tallennus-kansiosta... ei oikein hyvä, kyllästyin
#     -lisää rajoitteita tehtaville (täytyy tehdä tiettynä aikana)
#       TODO [Saaga 15/08/22]
#       DONEish
#     -etsi tekijät hommille rajoitteista huolimatta
#       TODO [Saaga 15/08/22]
#       DNF
#     -henkilöllä pitää olla esim. kaksi tuntia vapaata hommien välillä tms.
#       TODO [Saaga 15/08/22]
#       DNF




#Ulkoiset Kirjastot: Tähän projektiin tarvitsemme PySide2-kirjaston Qt-siteeksi
from PySide2 import QtCore, QtGui, QtWidgets

#Sisäiset kirjastot:
from pathlib import Path
import os, sys

#Alusta yleisiä vakioita:
ROOTFOLDER = Path(__file__).resolve().parents[0] #polku juureen
DEVENV = False #joko vai ei DEVENV on käytössä. DEVENV-tiedosto yliajaa tämän

#tarkista onko kyseessä kehitys-ympäristö
#jos on, käännä uic-tiedostot Py-tiedostoiksi
#tarvitsemme näitä myöhemmin

if os.path.isfile(f"{ROOTFOLDER}\devenv"):
    import convert_ui_files
    DEVENV = True   

#Resurssit: Jotkut UI-resurssit ovat ulkoisia. Tuomme ne täällä
from main_ui import Ui_MainUI

#Resurssit: Jotkut modulimme ovat ulkoisia. Tuomme ne täällä
from calendar_logic import CalendarWindow


class Window(QtWidgets.QMainWindow, Ui_MainUI):
    def __init__(self):
        print("[GUI] Initializing...")
        self.main_ui_object = super().__init__()
        self.setWindowTitle("Calendar-app")
        #self.setWindowIcon(QIcon('icon.ico'))

        self.setupUi(self)
        self.show()

        #alusta muuttujia:
        self.current_language = ""
        self.common_words = False
        self.translatable_bases = []

        #devenv:
        if not DEVENV:
            self.devenv_notice_label.hide()

        #translator
        self.trans = QtCore.QTranslator(self)
        self.translatable_bases.append(self)
        if not self.common_words:
            self.common_words = {
                "eng-fi": {
                    "New Calendar": "Uusi Kalenteri",
                    "Unsaved Calendar": "Tallentamaton Kalenteri",
                    "week_days": ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]
                }
            }
        #self.trans.load("eng-fi.ts", ".\\")
        language_action_group = QtWidgets.QActionGroup(self)
        language_action_group.addAction(self.actionFinnish)
        language_action_group.addAction(self.actionEnglish)
        self.actionFinnish.triggered.connect(lambda: self.set_language("eng-fi"))
        self.actionEnglish.triggered.connect(lambda: self.set_language(""))
        #self.add_calendar_tab("test")

        self.tabWidget.tabCloseRequested.connect(self.on_tab_close_requested) #methodi joka suorittaa tabien sulkemisen
        self.tabWidget.tabBar().setTabButton(0, QtWidgets.QTabBar.RightSide,None) #poistetaan sulkemispainike MENU-tabista
        
        self.new_calendar_button.clicked.connect(lambda: self.add_calendar_tab(self.translate_common_words("New Calendar", self.current_language)))
        self.open_calendar_button.clicked.connect(lambda: self.open_calendar())
        

        print("[GUI] Initializing complete!")
    def open_calendar(self) -> None:
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Load calendar..."), "", self.tr("Calendar Files (*.cldr)"))
        self.filename = fileName[0]
        name = self.filename.split("/")[-1].split(".")[0]
        if fileName[0] != "":
            self.add_calendar_tab(name, fileName[0])
    def translate(self, language:str) -> None:
        pass
    def translate_common_words(self, word:str, language:str) -> str:
        
        if language != "":
            return self.common_words[language][word]
        return word

    def set_language(self, language: str) -> None:
        if language != "":
            print("[GUI] Switching to", language, "at", self.trans.filePath())
            for base in self.translatable_bases:
                base.trans.load(language, "translations")
                _app = QtWidgets.QApplication.instance()
                _app.installTranslator(base.trans)
                base.current_language = language
                base.retranslateUi(base)
                base.translate("eng-fi")
        else:
            
            print("[GUI] Switching to native language")
            for base in self.translatable_bases:
                base.current_language = ""
                _app = QtWidgets.QApplication.instance()
                _app.removeTranslator(base.trans)
                base.retranslateUi(base)
                base.translate("")
        

    def add_calendar_tab(self, name:str, save_file:str = "") -> None:
        tab = QtWidgets.QWidget()
        tab.setObjectName(f"{name}tabObject")
        tab.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        index = self.tabWidget.addTab(tab, f"{name}")
        window = CalendarWindow(tab, self, save_file)
        self.tabWidget.setCurrentIndex(index)
        self.translatable_bases.append(window)

    def on_tab_close_requested(self, index:int) -> None:
        widget = self.tabWidget.widget(index)
        self.translatable_bases.remove(widget.tab_widget)
        widget.close()

def main() -> None:
    print("[MAIN] Starting GUI...")
    defaultfont = QtGui.QFont('Tahoma', 8)
    QtWidgets.QApplication.setFont(defaultfont)

    App = QtWidgets.QApplication(sys.argv)
    App.setStyle('Fusion')
    App.setFont(defaultfont)
    window = Window()
    window.setFont(defaultfont)
    App.exec_()
    return None

if __name__ == "__main__":
    main()