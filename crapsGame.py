__author__ = "Mwosa Ogbomo"

from sys import path
from die import *
import sys
import crapsResources_rc
from logging import basicConfig, getLogger, DEBUG, INFO, CRITICAL
from pickle import dump, load
from os import path
from PyQt5.QtCore import pyqtSlot, QSettings, Qt, QTimer, QCoreApplication
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox

startingBankDefault = 100
maximumBetDefault = 100
minimumBetDefault = 10
logFilenameDefault = 'craps.log'
pickleFilenameDefault = ".crapsSavedObjects.pl"

class Craps(QMainWindow):

    die1 = die2 = None


def __init__(self, parent=None):

    super() .__init(parent)

    self.logger = getLogger("crapsGame")
    self.appSettings = QSettings()
    self.quitCounter = 0;

    uic.loadUi("Craps.ui", self)

    self.payouts = [0,0,0,0, 2, 1.5, 1.2, 0, 1.2, 1.5, 2.0, 0, 0]
    self.picleFilename = pickleFilenameDefault

    self.restoreSettings()

    if path.exists(self.pickleFilename):
        self.die1, self.die2, self.firstRoll, self.results, self.PlayerLost, self.firstRollValue, self.buttonText, self.wins, self.losses, self.currentBet, self.currentBank = self.restoreGame()
    else:
        self.restartGame()

    self.rollButton.clicked.connect(self.rollButtonClickedHandler)
    self.bailButton.clicked.connect(self.bailButtonClickedHandler)
    self.preferencesSelectButton.clicked.connect(self.preferencesSelectButtonClickedHandler)
    self.restartButton.clicked.connect(self.restartButtonClickedHandler)

def __str__(self):

    return "Die1: %s\nDie2: %s" % (str(self.die1), str(self.die2))

def updateUI(self):
    if self.createLogFile:
        self.logger.info("Die1: %i, Die2: %i" % (self.die1.getValue(), self.die2.getValue() ) )
    self.bidSpinBox.setRange(self.minimumBet, self.maximumBet)
    self.bidSpinBox.setSingleStep(5)
    self.die1View.setPixmap(QtGui.QPixmap(":/" + str(self.die1.getValue())))
    self.die2View.setPixmap(QtGui.QPixmap(":/" + str(self.die2.getValue())))
    if self.firstRoll:
        self.rollingForLabel.setText("")
    else:
        self.rollingforLabel.setText(str("%i" % self.firstRollValue))
    self.resultsLabel.setText(self.results)
    self.rollButton.setText(self.buttonText)
    self.winsLabel.setText(str("%i" % self.wins))
    self.lossesLable.setText(str("%i" % self.losses))
    self.bankValue.setText(str("%i" % self.currentBank))













