# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StatClusterSettingsDial.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ClusterSettingsDial(QtWidgets.QDialog):
    def setupUi(self):
        self.setObjectName("ClusterSettingsDial")
        self.resize(400, 188)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 381, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.settingsLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.settingsLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsLayout.setObjectName("settingsLayout")
        self.methodSettings = QtWidgets.QVBoxLayout()
        self.methodSettings.setObjectName("methodSettings")
        self.settingsLayout.addLayout(self.methodSettings)
        self.clusterSettings = QtWidgets.QVBoxLayout()
        self.clusterSettings.setObjectName("clusterSettings")
        self.nOfClustersLayout = QtWidgets.QVBoxLayout()
        self.nOfClustersLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.nOfClustersLayout.setContentsMargins(5, 5, 5, 5)
        self.nOfClustersLayout.setSpacing(1)
        self.nOfClustersLayout.setObjectName("nOfClustersLayout")
        self.nOfClustersLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.nOfClustersLabel.setEnabled(True)
        self.nOfClustersLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.nOfClustersLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.nOfClustersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nOfClustersLabel.setObjectName("nOfClustersLabel")
        self.nOfClustersLayout.addWidget(self.nOfClustersLabel)
        self.nOfClustersBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.nOfClustersBox.setMaximumSize(QtCore.QSize(16777215, 26))
        self.nOfClustersBox.setSpecialValueText("")
        self.nOfClustersBox.setMinimum(1)
        self.nOfClustersBox.setObjectName("nOfClustersBox")
        self.nOfClustersLayout.addWidget(self.nOfClustersBox)
        self.clusterSettings.addLayout(self.nOfClustersLayout)
        self.settingsLayout.addLayout(self.clusterSettings)
        self.clusterRunButtons = QtWidgets.QDialogButtonBox(self)
        self.clusterRunButtons.setGeometry(QtCore.QRect(210, 140, 186, 32))
        self.clusterRunButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.clusterRunButtons.setCenterButtons(False)
        self.clusterRunButtons.setObjectName("clusterRunButtons")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ClusterSettingsDial", "GroupBox"))
        self.nOfClustersLabel.setText(_translate("ClusterSettingsDial", "Число кластеров"))

if __name__ == "__main__":
    print("Test")
    Ui_ClusterSettingsDial()

