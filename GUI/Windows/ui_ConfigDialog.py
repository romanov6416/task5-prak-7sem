
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ConfigDialog(object):
    def setupUi(self, ConfigDialog):
        ConfigDialog.setObjectName(_fromUtf8("ConfigDialog"))
        ConfigDialog.resize(623, 347)
        self.gridLayout = QtGui.QGridLayout(ConfigDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(ConfigDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.modnum = QtGui.QSpinBox(ConfigDialog)
        self.modnum.setMinimum(1)
        self.modnum.setMaximum(100)
        self.modnum.setObjectName(_fromUtf8("modnum"))
        self.verticalLayout_2.addWidget(self.modnum)
        self.verticalLayout_11.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(ConfigDialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(ConfigDialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.hwnum = QtGui.QSpinBox(ConfigDialog)
        self.hwnum.setMinimum(1)
        self.hwnum.setMaximum(100)
        self.hwnum.setObjectName(_fromUtf8("hwnum"))
        self.verticalLayout.addWidget(self.hwnum)
        self.verticalLayout_11.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_6 = QtGui.QLabel(ConfigDialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_5.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(ConfigDialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_5.addWidget(self.label_7)
        self.swnum = QtGui.QSpinBox(ConfigDialog)
        self.swnum.setMinimum(3)
        self.swnum.setMaximum(100)
        self.swnum.setObjectName(_fromUtf8("swnum"))
        self.verticalLayout_5.addWidget(self.swnum)
        self.verticalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(ConfigDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.minrel = QtGui.QDoubleSpinBox(ConfigDialog)
        self.minrel.setDecimals(3)
        self.minrel.setMaximum(1.0)
        self.minrel.setSingleStep(0.001)
        self.minrel.setProperty("value", 0.85)
        self.minrel.setObjectName(_fromUtf8("minrel"))
        self.verticalLayout_3.addWidget(self.minrel)
        self.verticalLayout_11.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_3 = QtGui.QLabel(ConfigDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.maxrel = QtGui.QDoubleSpinBox(ConfigDialog)
        self.maxrel.setDecimals(3)
        self.maxrel.setMaximum(1.0)
        self.maxrel.setSingleStep(0.001)
        self.maxrel.setProperty("value", 1.0)
        self.maxrel.setObjectName(_fromUtf8("maxrel"))
        self.verticalLayout_4.addWidget(self.maxrel)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_11.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_11)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_8 = QtGui.QLabel(ConfigDialog)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_6.addWidget(self.label_8)
        self.mincost = QtGui.QSpinBox(ConfigDialog)
        self.mincost.setMaximum(999)
        self.mincost.setProperty("value", 10)
        self.mincost.setObjectName(_fromUtf8("mincost"))
        self.verticalLayout_6.addWidget(self.mincost)
        self.verticalLayout_14.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_9 = QtGui.QLabel(ConfigDialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_7.addWidget(self.label_9)
        self.maxcost = QtGui.QSpinBox(ConfigDialog)
        self.maxcost.setMaximum(999)
        self.maxcost.setProperty("value", 30)
        self.maxcost.setObjectName(_fromUtf8("maxcost"))
        self.verticalLayout_7.addWidget(self.maxcost)
        self.verticalLayout_14.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_10 = QtGui.QLabel(ConfigDialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_8.addWidget(self.label_10)
        self.mintime = QtGui.QSpinBox(ConfigDialog)
        self.mintime.setMaximum(999)
        self.mintime.setProperty("value", 1)
        self.mintime.setObjectName(_fromUtf8("mintime"))
        self.verticalLayout_8.addWidget(self.mintime)
        self.verticalLayout_14.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_11 = QtGui.QLabel(ConfigDialog)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_9.addWidget(self.label_11)
        self.maxtime = QtGui.QSpinBox(ConfigDialog)
        self.maxtime.setMaximum(999)
        self.maxtime.setProperty("value", 10)
        self.maxtime.setObjectName(_fromUtf8("maxtime"))
        self.verticalLayout_9.addWidget(self.maxtime)
        self.verticalLayout_14.addLayout(self.verticalLayout_9)
        self.label_19 = QtGui.QLabel(ConfigDialog)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_14.addWidget(self.label_19)
        self.verticalLayout_22 = QtGui.QVBoxLayout()
        self.verticalLayout_22.setObjectName(_fromUtf8("verticalLayout_22"))
        self.minvol = QtGui.QSpinBox(ConfigDialog)
        self.minvol.setMaximum(999)
        self.minvol.setProperty("value", 1)
        self.minvol.setObjectName(_fromUtf8("minvol"))
        self.verticalLayout_22.addWidget(self.minvol)
        self.verticalLayout_14.addLayout(self.verticalLayout_22)
        self.label_20 = QtGui.QLabel(ConfigDialog)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_14.addWidget(self.label_20)
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.verticalLayout_14.addLayout(self.verticalLayout_13)
        self.maxvol = QtGui.QSpinBox(ConfigDialog)
        self.maxvol.setMaximum(999)
        self.maxvol.setProperty("value", 10)
        self.maxvol.setObjectName(_fromUtf8("maxvol"))
        self.verticalLayout_14.addWidget(self.maxvol)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_14)
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.label_13 = QtGui.QLabel(ConfigDialog)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_15.addWidget(self.label_13)
        self.qrv = QtGui.QDoubleSpinBox(ConfigDialog)
        self.qrv.setDecimals(3)
        self.qrv.setMaximum(1.0)
        self.qrv.setSingleStep(0.001)
        self.qrv.setProperty("value", 0.99)
        self.qrv.setObjectName(_fromUtf8("qrv"))
        self.verticalLayout_15.addWidget(self.qrv)
        self.verticalLayout_18.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.label_14 = QtGui.QLabel(ConfigDialog)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_16.addWidget(self.label_14)
        self.qd = QtGui.QDoubleSpinBox(ConfigDialog)
        self.qd.setDecimals(3)
        self.qd.setMaximum(1.0)
        self.qd.setSingleStep(0.001)
        self.qd.setProperty("value", 0.99)
        self.qd.setObjectName(_fromUtf8("qd"))
        self.verticalLayout_16.addWidget(self.qd)
        self.verticalLayout_18.addLayout(self.verticalLayout_16)
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.label_15 = QtGui.QLabel(ConfigDialog)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_17.addWidget(self.label_15)
        self.qall = QtGui.QDoubleSpinBox(ConfigDialog)
        self.qall.setDecimals(3)
        self.qall.setMaximum(1.0)
        self.qall.setSingleStep(0.001)
        self.qall.setProperty("value", 0.99)
        self.qall.setObjectName(_fromUtf8("qall"))
        self.verticalLayout_17.addWidget(self.qall)
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.label_16 = QtGui.QLabel(ConfigDialog)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_19.addWidget(self.label_16)
        self.tvote = QtGui.QSpinBox(ConfigDialog)
        self.tvote.setProperty("value", 1)
        self.tvote.setObjectName(_fromUtf8("tvote"))
        self.verticalLayout_19.addWidget(self.tvote)
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.label_17 = QtGui.QLabel(ConfigDialog)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.verticalLayout_20.addWidget(self.label_17)
        self.ttest = QtGui.QSpinBox(ConfigDialog)
        self.ttest.setProperty("value", 2)
        self.ttest.setObjectName(_fromUtf8("ttest"))
        self.verticalLayout_20.addWidget(self.ttest)
        self.verticalLayout_19.addLayout(self.verticalLayout_20)
        self.verticalLayout_17.addLayout(self.verticalLayout_19)
        self.verticalLayout_21 = QtGui.QVBoxLayout()
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.label_18 = QtGui.QLabel(ConfigDialog)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.verticalLayout_21.addWidget(self.label_18)
        self.trecov = QtGui.QSpinBox(ConfigDialog)
        self.trecov.setProperty("value", 3)
        self.trecov.setObjectName(_fromUtf8("trecov"))
        self.verticalLayout_21.addWidget(self.trecov)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem2)
        self.verticalLayout_17.addLayout(self.verticalLayout_21)
        self.verticalLayout_18.addLayout(self.verticalLayout_17)
        self.horizontalLayout.addLayout(self.verticalLayout_18)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_12 = QtGui.QLabel(ConfigDialog)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_10.addWidget(self.label_12)
        self.none = QtGui.QCheckBox(ConfigDialog)
        self.none.setChecked(True)
        self.none.setObjectName(_fromUtf8("none"))
        self.verticalLayout_10.addWidget(self.none)
        self.nvp01 = QtGui.QCheckBox(ConfigDialog)
        self.nvp01.setChecked(True)
        self.nvp01.setObjectName(_fromUtf8("nvp01"))
        self.verticalLayout_10.addWidget(self.nvp01)
        self.nvp11 = QtGui.QCheckBox(ConfigDialog)
        self.nvp11.setChecked(True)
        self.nvp11.setObjectName(_fromUtf8("nvp11"))
        self.verticalLayout_10.addWidget(self.nvp11)
        self.rb11 = QtGui.QCheckBox(ConfigDialog)
        self.rb11.setChecked(True)
        self.rb11.setObjectName(_fromUtf8("rb11"))
        self.verticalLayout_10.addWidget(self.rb11)
        self.label_21 = QtGui.QLabel(ConfigDialog)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_10.addWidget(self.label_21)
        self.linkprob = QtGui.QDoubleSpinBox(ConfigDialog)
        self.linkprob.setDecimals(3)
        self.linkprob.setMaximum(1.0)
        self.linkprob.setSingleStep(0.1)
        self.linkprob.setProperty("value", 0.5)
        self.linkprob.setObjectName(_fromUtf8("linkprob"))
        self.verticalLayout_10.addWidget(self.linkprob)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_12.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.retranslateUi(ConfigDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ConfigDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ConfigDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigDialog)

    def retranslateUi(self, ConfigDialog):
        ConfigDialog.setWindowTitle(_translate("ConfigDialog", "Dialog", None))
        self.label.setText(_translate("ConfigDialog", "Number of modules:", None))
        self.label_4.setText(_translate("ConfigDialog", "Number of HW versions", None))
        self.label_5.setText(_translate("ConfigDialog", "per module:", None))
        self.label_6.setText(_translate("ConfigDialog", "Number of SW versions", None))
        self.label_7.setText(_translate("ConfigDialog", "per module:", None))
        self.label_2.setText(_translate("ConfigDialog", "Minimum version reliability:", None))
        self.label_3.setText(_translate("ConfigDialog", "Maximum version reliability:", None))
        self.label_8.setText(_translate("ConfigDialog", "Minimum version cost:", None))
        self.label_9.setText(_translate("ConfigDialog", "Maximun version cost:", None))
        self.label_10.setText(_translate("ConfigDialog", "Minimum version time:", None))
        self.label_11.setText(_translate("ConfigDialog", "Maximum version time:", None))
        self.label_19.setText(_translate("ConfigDialog", "Minimum volume:", None))
        self.label_20.setText(_translate("ConfigDialog", "Maximum volume:", None))
        self.label_13.setText(_translate("ConfigDialog", "Qrv:", None))
        self.label_14.setText(_translate("ConfigDialog", "Qd:", None))
        self.label_15.setText(_translate("ConfigDialog", "Qall:", None))
        self.label_16.setText(_translate("ConfigDialog", "Voter time:", None))
        self.label_17.setText(_translate("ConfigDialog", "Control test time:", None))
        self.label_18.setText(_translate("ConfigDialog", "Recovery time:", None))
        self.label_12.setText(_translate("ConfigDialog", "Tools:", None))
        self.none.setText(_translate("ConfigDialog", "None", None))
        self.nvp01.setText(_translate("ConfigDialog", "NVP/0/1", None))
        self.nvp11.setText(_translate("ConfigDialog", "NVP/1/1", None))
        self.rb11.setText(_translate("ConfigDialog", "RB/1/1", None))
        self.label_21.setText(_translate("ConfigDialog", "Modules connection prob:", None))
