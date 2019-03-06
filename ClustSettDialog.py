from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *

DEFAULT_PARAMS = {'n_of_clusts': 1, 'cols_to_clust': [], 'criterion': "maxclust", 'method': "average",
                  'metric': "euclidean"}


class ClustSettDialog(QDialog):
    def __init__(self, analysis_options):
        super().__init__()
        self.setup_ui()
        self.retranslate_ui()

        self.params = (False, DEFAULT_PARAMS)

        self.nOfClustersBox.setValue(DEFAULT_PARAMS['n_of_clusts'])

        self.columnsToClustList.addItems(analysis_options["data_columns"])
        self.columnsToClustList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        self.criterionBox.addItems(analysis_options["criterions"])
        self.criterionBox.setCurrentText(DEFAULT_PARAMS["criterion"])
        self.methodBox.addItems(analysis_options["methods"])
        self.methodBox.setCurrentText(DEFAULT_PARAMS["method"])
        self.metricBox.addItems(analysis_options["metrics"])
        self.metricBox.setCurrentText(DEFAULT_PARAMS["metric"])

        self.clusterRunButtons.accepted.connect(lambda: self.save_and_close())
        self.clusterRunButtons.rejected.connect(lambda: self.close())

    def setup_ui(self):
        self.resize(510, 379)
        self.clusterRunButtons = QtWidgets.QDialogButtonBox(self)
        self.clusterRunButtons.setGeometry(QtCore.QRect(320, 330, 161, 32))
        self.clusterRunButtons.setOrientation(QtCore.Qt.Horizontal)
        self.clusterRunButtons.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.clusterRunButtons.setObjectName("clusterRunButtons")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 491, 311))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.mainLay = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.mainLay.setContentsMargins(0, 0, 0, 0)
        self.mainLay.setObjectName("mainLay")
        self.leftLay = QtWidgets.QVBoxLayout()
        self.leftLay.setContentsMargins(10, 10, 10, 10)
        self.leftLay.setSpacing(10)
        self.leftLay.setObjectName("leftLay")
        self.criterionLayout = QtWidgets.QVBoxLayout()
        self.criterionLayout.setSpacing(10)
        self.criterionLayout.setObjectName("criterionLayout")
        self.criterionLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.criterionLabel.setObjectName("criterionLabel")
        self.criterionLayout.addWidget(self.criterionLabel)
        self.criterionBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.criterionBox.setObjectName("criterionBox")
        self.criterionLayout.addWidget(self.criterionBox)
        self.leftLay.addLayout(self.criterionLayout)
        self.methodLayout = QtWidgets.QVBoxLayout()
        self.methodLayout.setSpacing(10)
        self.methodLayout.setObjectName("methodLayout")
        self.methodLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.methodLabel.setObjectName("methodLabel")
        self.methodLayout.addWidget(self.methodLabel)
        self.methodBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.methodBox.setObjectName("methodBox")
        self.methodLayout.addWidget(self.methodBox)
        self.leftLay.addLayout(self.methodLayout)
        self.metricLayout = QtWidgets.QVBoxLayout()
        self.metricLayout.setSpacing(10)
        self.metricLayout.setObjectName("metricLayout")
        self.metricLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.metricLabel.setObjectName("metricLabel")
        self.metricLayout.addWidget(self.metricLabel)
        self.metricBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.metricBox.setObjectName("metricBox")
        self.metricLayout.addWidget(self.metricBox)
        self.leftLay.addLayout(self.metricLayout)
        self.mainLay.addLayout(self.leftLay)
        self.rightLay = QtWidgets.QVBoxLayout()
        self.rightLay.setContentsMargins(10, 10, 10, 10)
        self.rightLay.setSpacing(10)
        self.rightLay.setObjectName("rightLay")
        self.nOfClustersLayout = QtWidgets.QVBoxLayout()
        self.nOfClustersLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.nOfClustersLayout.setContentsMargins(10, 10, 10, 10)
        self.nOfClustersLayout.setSpacing(10)
        self.nOfClustersLayout.setObjectName("nOfClustersLayout")
        self.nOfClustersLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.nOfClustersLabel.setObjectName("nOfClustersLabel")
        self.nOfClustersLayout.addWidget(self.nOfClustersLabel)
        self.nOfClustersBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.nOfClustersBox.setObjectName("nOfClustersBox")
        self.nOfClustersBox.setMinimum(1)
        self.nOfClustersLayout.addWidget(self.nOfClustersBox)
        self.rightLay.addLayout(self.nOfClustersLayout)
        self.columnsToClustLayout = QtWidgets.QVBoxLayout()
        self.columnsToClustLayout.setObjectName("columnsToClustLayout")
        self.columnsToClustLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.columnsToClustLabel.setObjectName("columnsToClustLabel")
        self.columnsToClustLayout.addWidget(self.columnsToClustLabel)
        self.columnsToClustList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.columnsToClustList.sizePolicy().hasHeightForWidth())
        self.columnsToClustList.setSizePolicy(sizePolicy)
        self.columnsToClustList.setObjectName("columnsToClustList")
        self.columnsToClustLayout.addWidget(self.columnsToClustList)
        self.rightLay.addLayout(self.columnsToClustLayout)
        self.mainLay.addLayout(self.rightLay)

        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ClusterSettingsDial", "Настройки кластеризации"))
        self.criterionLabel.setText(_translate("ClusterSettingsDial", "Критерий кластеризации"))
        self.methodLabel.setText(_translate("ClusterSettingsDial", "Метод кластеризации"))
        self.metricLabel.setText(_translate("ClusterSettingsDial", "Метрика кластеризации"))
        self.nOfClustersLabel.setText(_translate("ClusterSettingsDial", "Число кластеров"))
        self.columnsToClustLabel.setText(_translate("ClusterSettingsDial", "Столбцы для кластеризации"))

    def save_and_close(self):
        self.params = (True, self.get_params())
        self.close()

    def get_params(self):
        return {
            'n_of_clusts': self.nOfClustersBox.value(),
            'cols_to_clust': [col.text() for col in self.columnsToClustList.selectedItems()],
            'criterion': self.criterionBox.currentText(),
            'method': self.methodBox.currentText(),
            'metric': self.metricBox.currentText()
        }

    @staticmethod
    def get_clust_settings(options):
        dlg = ClustSettDialog(options)
        dlg.exec_()
        return dlg.params


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationName("ClustSettDial")
    cont, pars = ClustSettDialog.get_clust_settings(['Alpha', 'Beta', 'Gamma'])
    print(cont)
    print(pars)
