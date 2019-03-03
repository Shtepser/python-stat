from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *

DEFAULT_PARAMS = {'n_of_clusts': 1, 'cols_to_clust': []}


class ClustSettDialog(QDialog):
    def __init__(self, data_columns):
        super().__init__()
        self.setup_ui(data_columns)
        self.retranslate_ui()

        self.params = (False, DEFAULT_PARAMS)

        self.nOfClustersBox.setValue(DEFAULT_PARAMS['n_of_clusts'])

        self.clusterRunButtons.accepted.connect(lambda: self.save_and_close())
        self.clusterRunButtons.rejected.connect(lambda: self.close())

    def setup_ui(self, data_columns):
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

        self.columnsToClustLayout = QtWidgets.QVBoxLayout()

        self.columnsToClustLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.columnsToClustLabel.setEnabled(True)
        self.columnsToClustLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.columnsToClustLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.columnsToClustLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.columnsToClustLabel.setObjectName("columnsToClustLabel")
        self.columnsToClustLayout.addWidget(self.columnsToClustLabel)

        self.columnsToClustList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        # self.columnsToClustList.setSizePolicy(QSizePolicy.Maximum)
        self.columnsToClustList.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        for i in data_columns:
            item = QtWidgets.QListWidgetItem(i)
            self.columnsToClustList.addItem(item)

        self.columnsToClustLayout.addWidget(self.columnsToClustList)
        self.clusterSettings.addLayout(self.columnsToClustLayout)

        self.settingsLayout.addLayout(self.clusterSettings)

        self.clusterRunButtons = QtWidgets.QDialogButtonBox(self)
        self.clusterRunButtons.setGeometry(QtCore.QRect(210, 140, 186, 32))
        self.clusterRunButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.clusterRunButtons.setCenterButtons(False)
        self.clusterRunButtons.setObjectName("clusterRunButtons")
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ClusterSettingsDial", "Настройки кластеризации"))
        self.nOfClustersLabel.setText(_translate("ClusterSettingsDial", "Число кластеров"))
        self.columnsToClustLabel.setText(_translate("ClusterSettingsDial", "Столбцы для кластеризации"))

    def save_and_close(self):
        self.params = (True, self.get_params())
        self.close()

    def get_params(self):
        return {
            'n_of_clusts': self.nOfClustersBox.value(),
            'cols_to_clust': [col.text() for col in self.columnsToClustList.selectedItems()]
        }

    @staticmethod
    def get_clust_settings(data_columns):
        dlg = ClustSettDialog(data_columns)
        dlg.exec_()
        return dlg.params


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("ClustSettDial")
    cont, pars = ClustSettDialog.get_clust_settings(['Alpha', 'Beta', 'Gamma'])
    print(cont)
    print(pars)
