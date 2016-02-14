#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Radio Presidio Prototype
# Generated: Mon Feb  8 10:45:07 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import dtv
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import osmosdr
import sip
import sys
import time


class Radio_Presidio_Prototype(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Radio Presidio Prototype")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Radio Presidio Prototype")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Radio_Presidio_Prototype")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.txfirtuning = txfirtuning = -100000
        self.rxfirtuning = rxfirtuning = -100000
        self.finetxfirtune = finetxfirtune = 0
        self.finerxfirtune = finerxfirtune = 0
        self.txoffset = txoffset = (finetxfirtune+txfirtuning)
        self.txfreq = txfreq = 449100000
        self.tritoneswitch = tritoneswitch = 0
        self.rxoffset = rxoffset = (finerxfirtune+rxfirtuning)
        self.rxfreq = rxfreq = 444100000
        self.pltoneswitch = pltoneswitch = 1
        self.audio_rate = audio_rate = 96000
        self.writeafscratch = writeafscratch = 0
        self.wbfmtxrate = wbfmtxrate = 192000
        self.wbfmrxrate = wbfmrxrate = audio_rate * 4
        self.wavvolume = wavvolume = 0
        self.wav_rate = wav_rate = 48000
        self.variable_0 = variable_0 = 0
        self.txvga2gain = txvga2gain = 0
        self.txvga1gain = txvga1gain = -35
        self.txsink = txsink = 0
        self.txmodulation = txmodulation = 0
        self.txfirfilterwidth = txfirfilterwidth = 100000
        self.txfirfilterskirt = txfirfilterskirt = 70000
        self.txfirfile = txfirfile = False
        self.txfirdisplay = txfirdisplay = txfreq  + (txoffset)
        self.txfilterswitch = txfilterswitch = 0
        self.txfiltergain = txfiltergain = 1
        self.txdatamodulation = txdatamodulation = 0
        self.txdata = txdata = 0
        self.txbandwidth = txbandwidth = 0
        self.txaudioskirt = txaudioskirt = 100
        self.txaudiolow = txaudiolow = 100
        self.txaudiohigh = txaudiohigh = 10000
        self.txagcswitch = txagcswitch = 0
        self.tx = tx = False
        self.tonetwo = tonetwo = 1046.5
        self.tonethree = tonethree = 1318.5
        self.toneone = toneone = 783.99
        self.symbol_rate = symbol_rate = 4500000.0 / 286 * 684
        self.sym_rate = sym_rate = 2400
        self.squelch = squelch = -75
        self.sps_0 = sps_0 = 8
        self.sps = sps = 8
        self.samp_rate_0 = samp_rate_0 = 96000
        self.samp_rate = samp_rate = 5376000
        self.rxvolume = rxvolume = 5
        self.rxvga2gain = rxvga2gain = 0
        self.rxvga1gain = rxvga1gain = 5
        self.rxtx = rxtx = 0
        self.rxsource = rxsource = 0
        self.rxoutputgain = rxoutputgain = 50
        self.rxmodulation = rxmodulation = 0
        self.rxiqswitch = rxiqswitch = False
        self.rxfirwidth = rxfirwidth = 10000
        self.rxfirswitch = rxfirswitch = False
        self.rxfirfilterskirt = rxfirfilterskirt = 10000
        self.rxfirfile = rxfirfile = False
        self.rxfilterswitch = rxfilterswitch = 1
        self.rxdatamodulation = rxdatamodulation = 0
        self.rxdata = rxdata = 0
        self.rxbandwidth = rxbandwidth = 0
        self.rxaudioskirt = rxaudioskirt = 100
        self.rxaudiolow = rxaudiolow = 100
        self.rxaudiohigh = rxaudiohigh = 10000
        self.rxagcswitch = rxagcswitch = 0
        self.rx = rx = 0
        self.readafscratch = readafscratch = 0
        self.protect = protect = 1
        self.pltone_0 = pltone_0 = 0 if not pltoneswitch else .2
        self.pltone = pltone = 100
        self.pilot_freq = pilot_freq = 309441
        self.nbfmtxrate = nbfmtxrate = 192000 *2
        self.nbfmrxrate = nbfmrxrate = audio_rate * 2
        self.muteaudioout = muteaudioout = 0
        self.mute = mute = 0
        self.micvolume = micvolume = 1
        self.lnagain = lnagain = 0
        self.label = label = rxfreq  + (rxoffset)
        self.freq_shift = freq_shift = -30e3
        self.fm_deviation = fm_deviation = 4.5e3
        self.firrate = firrate = audio_rate * 4
        self.firfiletxamplitude = firfiletxamplitude = 100
        self.cwkey = cwkey = 0
        self.audiofftmagnification = audiofftmagnification = 15
        self.amplitude = amplitude = 1
        self.ampl = ampl = 0 if not tritoneswitch else 1
        self.afscratchvolume = afscratchvolume = 1
        self.PI = PI = 3.1415926

        ##################################################
        # Blocks
        ##################################################
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, "RX")
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, "TX")
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, "Audio")
        self.tab_widget_3 = Qt.QWidget()
        self.tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_3)
        self.tab_grid_layout_3 = Qt.QGridLayout()
        self.tab_layout_3.addLayout(self.tab_grid_layout_3)
        self.tab.addTab(self.tab_widget_3, "Data")
        self.tab_widget_4 = Qt.QWidget()
        self.tab_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_4)
        self.tab_grid_layout_4 = Qt.QGridLayout()
        self.tab_layout_4.addLayout(self.tab_grid_layout_4)
        self.tab.addTab(self.tab_widget_4, "Modulation")
        self.tab_widget_5 = Qt.QWidget()
        self.tab_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_5)
        self.tab_grid_layout_5 = Qt.QGridLayout()
        self.tab_layout_5.addLayout(self.tab_grid_layout_5)
        self.tab.addTab(self.tab_widget_5, "Instrumentation")
        self.top_layout.addWidget(self.tab)
        self._label_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._label_formatter = None
        else:
          self._label_formatter = lambda x: x
        
        self._label_tool_bar.addWidget(Qt.QLabel("RX FIR Actual Frequency"+": "))
        self._label_label = Qt.QLabel(str(self._label_formatter(self.label)))
        self._label_tool_bar.addWidget(self._label_label)
        self.tab_grid_layout_0.addWidget(self._label_tool_bar, 0,3,1,2)
          
        _writeafscratch_check_box = Qt.QCheckBox("Write AF to File")
        self._writeafscratch_choices = {True: 1, False: 0}
        self._writeafscratch_choices_inv = dict((v,k) for k,v in self._writeafscratch_choices.iteritems())
        self._writeafscratch_callback = lambda i: Qt.QMetaObject.invokeMethod(_writeafscratch_check_box, "setChecked", Qt.Q_ARG("bool", self._writeafscratch_choices_inv[i]))
        self._writeafscratch_callback(self.writeafscratch)
        _writeafscratch_check_box.stateChanged.connect(lambda i: self.set_writeafscratch(self._writeafscratch_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_writeafscratch_check_box, 6,3,1,1)
        self._wavvolume_range = Range(0, 10, .1, 0, 10)
        self._wavvolume_win = RangeWidget(self._wavvolume_range, self.set_wavvolume, "WAV Input Volume", "slider", float)
        self.tab_grid_layout_2.addWidget(self._wavvolume_win, 0,3,1,1)
        self._txvga2gain_range = Range(0, 25, 1, 0, 10)
        self._txvga2gain_win = RangeWidget(self._txvga2gain_range, self.set_txvga2gain, "BladeRF TX VGA2 Gain (dB)", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._txvga2gain_win, 1,2,1,1)
        self._txvga1gain_range = Range(-35, -4, 1, -35, 10)
        self._txvga1gain_win = RangeWidget(self._txvga1gain_range, self.set_txvga1gain, "BladeRF TX VGA1 Gain (dB)", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._txvga1gain_win, 1,1,1,1)
        self._txsink_options = (0, 1, 2, )
        self._txsink_labels = ("BladeRF USB Radio Card", "IQ Sampled Data File", "Null Sink", )
        self._txsink_tool_bar = Qt.QToolBar(self)
        self._txsink_tool_bar.addWidget(Qt.QLabel("TX Sink"+": "))
        self._txsink_combo_box = Qt.QComboBox()
        self._txsink_tool_bar.addWidget(self._txsink_combo_box)
        for label in self._txsink_labels: self._txsink_combo_box.addItem(label)
        self._txsink_callback = lambda i: Qt.QMetaObject.invokeMethod(self._txsink_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._txsink_options.index(i)))
        self._txsink_callback(self.txsink)
        self._txsink_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_txsink(self._txsink_options[i]))
        self.tab_grid_layout_1.addWidget(self._txsink_tool_bar, 4,3,1,1)
        self._txmodulation_options = (0, 1, 2, 3, 4, )
        self._txmodulation_labels = ("Narrow Band FM", "Wide Band FM", "Amplitude Modulation", "Upper Side Band", "Lower Side Band", )
        self._txmodulation_tool_bar = Qt.QToolBar(self)
        self._txmodulation_tool_bar.addWidget(Qt.QLabel("TX Modulation"+": "))
        self._txmodulation_combo_box = Qt.QComboBox()
        self._txmodulation_tool_bar.addWidget(self._txmodulation_combo_box)
        for label in self._txmodulation_labels: self._txmodulation_combo_box.addItem(label)
        self._txmodulation_callback = lambda i: Qt.QMetaObject.invokeMethod(self._txmodulation_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._txmodulation_options.index(i)))
        self._txmodulation_callback(self.txmodulation)
        self._txmodulation_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_txmodulation(self._txmodulation_options[i]))
        self.tab_grid_layout_4.addWidget(self._txmodulation_tool_bar, 0,2,1,1)
        self._txfreq_tool_bar = Qt.QToolBar(self)
        self._txfreq_tool_bar.addWidget(Qt.QLabel("Blade RF TX Frequency"+": "))
        self._txfreq_line_edit = Qt.QLineEdit(str(self.txfreq))
        self._txfreq_tool_bar.addWidget(self._txfreq_line_edit)
        self._txfreq_line_edit.returnPressed.connect(
        	lambda: self.set_txfreq(int(str(self._txfreq_line_edit.text().toAscii()))))
        self.tab_grid_layout_1.addWidget(self._txfreq_tool_bar, 0,1,1,1)
        self._txfirfilterwidth_range = Range(0, 200000, 1000, 100000, 10)
        self._txfirfilterwidth_win = RangeWidget(self._txfirfilterwidth_range, self.set_txfirfilterwidth, "TX FIR Filter Width", "counter_slider", float)
        self.tab_grid_layout_4.addWidget(self._txfirfilterwidth_win, 3,1,1,1)
        self._txfirfilterskirt_range = Range(1000, 100000, 10, 70000, 10)
        self._txfirfilterskirt_win = RangeWidget(self._txfirfilterskirt_range, self.set_txfirfilterskirt, "TX FIR Filter Skirt", "counter_slider", float)
        self.tab_grid_layout_4.addWidget(self._txfirfilterskirt_win, 3,2,1,1)
        _txfirfile_check_box = Qt.QCheckBox("TX FIR File")
        self._txfirfile_choices = {True: True, False: False}
        self._txfirfile_choices_inv = dict((v,k) for k,v in self._txfirfile_choices.iteritems())
        self._txfirfile_callback = lambda i: Qt.QMetaObject.invokeMethod(_txfirfile_check_box, "setChecked", Qt.Q_ARG("bool", self._txfirfile_choices_inv[i]))
        self._txfirfile_callback(self.txfirfile)
        _txfirfile_check_box.stateChanged.connect(lambda i: self.set_txfirfile(self._txfirfile_choices[bool(i)]))
        self.tab_grid_layout_1.addWidget(_txfirfile_check_box, 2,2,1,1)
        _txfilterswitch_check_box = Qt.QCheckBox("Filter TX Audio")
        self._txfilterswitch_choices = {True: 1, False: 0}
        self._txfilterswitch_choices_inv = dict((v,k) for k,v in self._txfilterswitch_choices.iteritems())
        self._txfilterswitch_callback = lambda i: Qt.QMetaObject.invokeMethod(_txfilterswitch_check_box, "setChecked", Qt.Q_ARG("bool", self._txfilterswitch_choices_inv[i]))
        self._txfilterswitch_callback(self.txfilterswitch)
        _txfilterswitch_check_box.stateChanged.connect(lambda i: self.set_txfilterswitch(self._txfilterswitch_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_txfilterswitch_check_box, 4,0,1,1)
        self._txdatamodulation_options = (0, )
        self._txdatamodulation_labels = ("ATSC Television", )
        self._txdatamodulation_tool_bar = Qt.QToolBar(self)
        self._txdatamodulation_tool_bar.addWidget(Qt.QLabel("TX Data Modulation"+": "))
        self._txdatamodulation_combo_box = Qt.QComboBox()
        self._txdatamodulation_tool_bar.addWidget(self._txdatamodulation_combo_box)
        for label in self._txdatamodulation_labels: self._txdatamodulation_combo_box.addItem(label)
        self._txdatamodulation_callback = lambda i: Qt.QMetaObject.invokeMethod(self._txdatamodulation_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._txdatamodulation_options.index(i)))
        self._txdatamodulation_callback(self.txdatamodulation)
        self._txdatamodulation_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_txdatamodulation(self._txdatamodulation_options[i]))
        self.tab_grid_layout_3.addWidget(self._txdatamodulation_tool_bar, 1,2,1,1)
        _txdata_check_box = Qt.QCheckBox("Enable TX Data Modulation")
        self._txdata_choices = {True: 1, False: 0}
        self._txdata_choices_inv = dict((v,k) for k,v in self._txdata_choices.iteritems())
        self._txdata_callback = lambda i: Qt.QMetaObject.invokeMethod(_txdata_check_box, "setChecked", Qt.Q_ARG("bool", self._txdata_choices_inv[i]))
        self._txdata_callback(self.txdata)
        _txdata_check_box.stateChanged.connect(lambda i: self.set_txdata(self._txdata_choices[bool(i)]))
        self.tab_grid_layout_3.addWidget(_txdata_check_box, 1,0,1,1)
        self._txbandwidth_tool_bar = Qt.QToolBar(self)
        self._txbandwidth_tool_bar.addWidget(Qt.QLabel("BladeRF TX Bandwidth"+": "))
        self._txbandwidth_line_edit = Qt.QLineEdit(str(self.txbandwidth))
        self._txbandwidth_tool_bar.addWidget(self._txbandwidth_line_edit)
        self._txbandwidth_line_edit.returnPressed.connect(
        	lambda: self.set_txbandwidth(eng_notation.str_to_num(str(self._txbandwidth_line_edit.text().toAscii()))))
        self.tab_grid_layout_1.addWidget(self._txbandwidth_tool_bar, 4,2,1,1)
        self._txaudioskirt_tool_bar = Qt.QToolBar(self)
        self._txaudioskirt_tool_bar.addWidget(Qt.QLabel("TX Audio Filter Skirt (Hz)"+": "))
        self._txaudioskirt_line_edit = Qt.QLineEdit(str(self.txaudioskirt))
        self._txaudioskirt_tool_bar.addWidget(self._txaudioskirt_line_edit)
        self._txaudioskirt_line_edit.returnPressed.connect(
        	lambda: self.set_txaudioskirt(eng_notation.str_to_num(str(self._txaudioskirt_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._txaudioskirt_tool_bar, 4,3,1,1)
        self._txaudiolow_tool_bar = Qt.QToolBar(self)
        self._txaudiolow_tool_bar.addWidget(Qt.QLabel("TX Audio High Pass (Hz)"+": "))
        self._txaudiolow_line_edit = Qt.QLineEdit(str(self.txaudiolow))
        self._txaudiolow_tool_bar.addWidget(self._txaudiolow_line_edit)
        self._txaudiolow_line_edit.returnPressed.connect(
        	lambda: self.set_txaudiolow(eng_notation.str_to_num(str(self._txaudiolow_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._txaudiolow_tool_bar, 4,1,1,1)
        self._txaudiohigh_tool_bar = Qt.QToolBar(self)
        self._txaudiohigh_tool_bar.addWidget(Qt.QLabel("TX Audio Low Pass (Hz)"+": "))
        self._txaudiohigh_line_edit = Qt.QLineEdit(str(self.txaudiohigh))
        self._txaudiohigh_tool_bar.addWidget(self._txaudiohigh_line_edit)
        self._txaudiohigh_line_edit.returnPressed.connect(
        	lambda: self.set_txaudiohigh(eng_notation.str_to_num(str(self._txaudiohigh_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._txaudiohigh_tool_bar, 4,2,1,1)
        _txagcswitch_check_box = Qt.QCheckBox("Enable TX Audio AGC")
        self._txagcswitch_choices = {True: 1, False: 0}
        self._txagcswitch_choices_inv = dict((v,k) for k,v in self._txagcswitch_choices.iteritems())
        self._txagcswitch_callback = lambda i: Qt.QMetaObject.invokeMethod(_txagcswitch_check_box, "setChecked", Qt.Q_ARG("bool", self._txagcswitch_choices_inv[i]))
        self._txagcswitch_callback(self.txagcswitch)
        _txagcswitch_check_box.stateChanged.connect(lambda i: self.set_txagcswitch(self._txagcswitch_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_txagcswitch_check_box, 6,0,1,1)
        _tx_check_box = Qt.QCheckBox("TX")
        self._tx_choices = {True: True, False: False}
        self._tx_choices_inv = dict((v,k) for k,v in self._tx_choices.iteritems())
        self._tx_callback = lambda i: Qt.QMetaObject.invokeMethod(_tx_check_box, "setChecked", Qt.Q_ARG("bool", self._tx_choices_inv[i]))
        self._tx_callback(self.tx)
        _tx_check_box.stateChanged.connect(lambda i: self.set_tx(self._tx_choices[bool(i)]))
        self.tab_grid_layout_1.addWidget(_tx_check_box, 0,0,1,1)
        self._tonetwo_tool_bar = Qt.QToolBar(self)
        self._tonetwo_tool_bar.addWidget(Qt.QLabel("Tone Two Frequency: (Hz)"+": "))
        self._tonetwo_line_edit = Qt.QLineEdit(str(self.tonetwo))
        self._tonetwo_tool_bar.addWidget(self._tonetwo_line_edit)
        self._tonetwo_line_edit.returnPressed.connect(
        	lambda: self.set_tonetwo(eng_notation.str_to_num(str(self._tonetwo_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._tonetwo_tool_bar, 2,2,1,1)
        self._tonethree_tool_bar = Qt.QToolBar(self)
        self._tonethree_tool_bar.addWidget(Qt.QLabel("Tone Three Frequency: (Hz)"+": "))
        self._tonethree_line_edit = Qt.QLineEdit(str(self.tonethree))
        self._tonethree_tool_bar.addWidget(self._tonethree_line_edit)
        self._tonethree_line_edit.returnPressed.connect(
        	lambda: self.set_tonethree(eng_notation.str_to_num(str(self._tonethree_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._tonethree_tool_bar, 2,3,1,1)
        self._toneone_tool_bar = Qt.QToolBar(self)
        self._toneone_tool_bar.addWidget(Qt.QLabel("Tone One Frequency: (Hz)"+": "))
        self._toneone_line_edit = Qt.QLineEdit(str(self.toneone))
        self._toneone_tool_bar.addWidget(self._toneone_line_edit)
        self._toneone_line_edit.returnPressed.connect(
        	lambda: self.set_toneone(eng_notation.str_to_num(str(self._toneone_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._toneone_tool_bar, 2,1,1,1)
        self.tab2 = Qt.QTabWidget()
        self.tab2_widget_0 = Qt.QWidget()
        self.tab2_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab2_widget_0)
        self.tab2_grid_layout_0 = Qt.QGridLayout()
        self.tab2_layout_0.addLayout(self.tab2_grid_layout_0)
        self.tab2.addTab(self.tab2_widget_0, "Waterfall")
        self.tab2_widget_1 = Qt.QWidget()
        self.tab2_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab2_widget_1)
        self.tab2_grid_layout_1 = Qt.QGridLayout()
        self.tab2_layout_1.addLayout(self.tab2_grid_layout_1)
        self.tab2.addTab(self.tab2_widget_1, "Audio FFT")
        self.tab2_widget_2 = Qt.QWidget()
        self.tab2_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab2_widget_2)
        self.tab2_grid_layout_2 = Qt.QGridLayout()
        self.tab2_layout_2.addLayout(self.tab2_grid_layout_2)
        self.tab2.addTab(self.tab2_widget_2, "IQ FFT")
        self.tab2_widget_3 = Qt.QWidget()
        self.tab2_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab2_widget_3)
        self.tab2_grid_layout_3 = Qt.QGridLayout()
        self.tab2_layout_3.addLayout(self.tab2_grid_layout_3)
        self.tab2.addTab(self.tab2_widget_3, "FIR FFT")
        self.tab2_widget_4 = Qt.QWidget()
        self.tab2_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab2_widget_4)
        self.tab2_grid_layout_4 = Qt.QGridLayout()
        self.tab2_layout_4.addLayout(self.tab2_grid_layout_4)
        self.tab2.addTab(self.tab2_widget_4, "FIR Waterfall")
        self.tab2_widget_5 = Qt.QWidget()
        self.tab2_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab2_widget_5)
        self.tab2_grid_layout_5 = Qt.QGridLayout()
        self.tab2_layout_5.addLayout(self.tab2_grid_layout_5)
        self.tab2.addTab(self.tab2_widget_5, "Decimation FFT")
        self.top_layout.addWidget(self.tab2)
        self._squelch_range = Range(-150, 0, 1, -75, 10)
        self._squelch_win = RangeWidget(self._squelch_range, self.set_squelch, "RX Power Squelch (dBFS)", "counter_slider", float)
        self.tab_grid_layout_2.addWidget(self._squelch_win, 5,2,1,2)
        self._samp_rate_tool_bar = Qt.QToolBar(self)
        self._samp_rate_tool_bar.addWidget(Qt.QLabel("Flowgraph Sample Rate"+": "))
        self._samp_rate_line_edit = Qt.QLineEdit(str(self.samp_rate))
        self._samp_rate_tool_bar.addWidget(self._samp_rate_line_edit)
        self._samp_rate_line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate(eng_notation.str_to_num(str(self._samp_rate_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._samp_rate_tool_bar, 4,1,1,1)
        self._rxvolume_range = Range(0, 100, .1, 5, 10)
        self._rxvolume_win = RangeWidget(self._rxvolume_range, self.set_rxvolume, "RX Audio Output Volume", "slider", float)
        self.tab_grid_layout_2.addWidget(self._rxvolume_win, 0,1,1,1)
        self._rxvga2gain_range = Range(0, 60, 1, 0, 10)
        self._rxvga2gain_win = RangeWidget(self._rxvga2gain_range, self.set_rxvga2gain, "BladeRF RXVGA2 Gain (dB)", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._rxvga2gain_win, 1,3,1,1)
        self._rxvga1gain_range = Range(5, 30, 1, 5, 10)
        self._rxvga1gain_win = RangeWidget(self._rxvga1gain_range, self.set_rxvga1gain, "BladeRF RX VGA1 Gain (dB)", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._rxvga1gain_win, 1,2,1,1)
        self._rxsource_options = (0, 1, 2, )
        self._rxsource_labels = ("BladeRF USB Radio Card", "IQ Sampled Data File", "Null Source", )
        self._rxsource_tool_bar = Qt.QToolBar(self)
        self._rxsource_tool_bar.addWidget(Qt.QLabel("RX Source"+": "))
        self._rxsource_combo_box = Qt.QComboBox()
        self._rxsource_tool_bar.addWidget(self._rxsource_combo_box)
        for label in self._rxsource_labels: self._rxsource_combo_box.addItem(label)
        self._rxsource_callback = lambda i: Qt.QMetaObject.invokeMethod(self._rxsource_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._rxsource_options.index(i)))
        self._rxsource_callback(self.rxsource)
        self._rxsource_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_rxsource(self._rxsource_options[i]))
        self.tab_grid_layout_0.addWidget(self._rxsource_tool_bar, 4,3,1,1)
        self._rxoutputgain_tool_bar = Qt.QToolBar(self)
        self._rxoutputgain_tool_bar.addWidget(Qt.QLabel("RX Output Gain"+": "))
        self._rxoutputgain_line_edit = Qt.QLineEdit(str(self.rxoutputgain))
        self._rxoutputgain_tool_bar.addWidget(self._rxoutputgain_line_edit)
        self._rxoutputgain_line_edit.returnPressed.connect(
        	lambda: self.set_rxoutputgain(eng_notation.str_to_num(str(self._rxoutputgain_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._rxoutputgain_tool_bar, 5,1,1,1)
        self._rxmodulation_options = (0, 1, 2, 3, 4, )
        self._rxmodulation_labels = ("Narrow Band FM", "Wide Band FM", "Amplitude Modulation", "Upper Side Band", "Lower Side Band", )
        self._rxmodulation_tool_bar = Qt.QToolBar(self)
        self._rxmodulation_tool_bar.addWidget(Qt.QLabel("RX Modulation"+": "))
        self._rxmodulation_combo_box = Qt.QComboBox()
        self._rxmodulation_tool_bar.addWidget(self._rxmodulation_combo_box)
        for label in self._rxmodulation_labels: self._rxmodulation_combo_box.addItem(label)
        self._rxmodulation_callback = lambda i: Qt.QMetaObject.invokeMethod(self._rxmodulation_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._rxmodulation_options.index(i)))
        self._rxmodulation_callback(self.rxmodulation)
        self._rxmodulation_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_rxmodulation(self._rxmodulation_options[i]))
        self.tab_grid_layout_4.addWidget(self._rxmodulation_tool_bar, 0,1,1,1)
        _rxiqswitch_check_box = Qt.QCheckBox("Save RX IQ Data to File")
        self._rxiqswitch_choices = {True: True, False: False}
        self._rxiqswitch_choices_inv = dict((v,k) for k,v in self._rxiqswitch_choices.iteritems())
        self._rxiqswitch_callback = lambda i: Qt.QMetaObject.invokeMethod(_rxiqswitch_check_box, "setChecked", Qt.Q_ARG("bool", self._rxiqswitch_choices_inv[i]))
        self._rxiqswitch_callback(self.rxiqswitch)
        _rxiqswitch_check_box.stateChanged.connect(lambda i: self.set_rxiqswitch(self._rxiqswitch_choices[bool(i)]))
        self.tab_grid_layout_0.addWidget(_rxiqswitch_check_box, 4,4,1,1)
        self._rxfreq_tool_bar = Qt.QToolBar(self)
        self._rxfreq_tool_bar.addWidget(Qt.QLabel("BladeRF RX  Frequency"+": "))
        self._rxfreq_line_edit = Qt.QLineEdit(str(self.rxfreq))
        self._rxfreq_tool_bar.addWidget(self._rxfreq_line_edit)
        self._rxfreq_line_edit.returnPressed.connect(
        	lambda: self.set_rxfreq(eng_notation.str_to_num(str(self._rxfreq_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._rxfreq_tool_bar, 0,1,1,1)
        self._rxfirwidth_range = Range(0, 200000, 1000, 10000, 10)
        self._rxfirwidth_win = RangeWidget(self._rxfirwidth_range, self.set_rxfirwidth, "RX FIR Filter Width", "counter_slider", float)
        self.tab_grid_layout_4.addWidget(self._rxfirwidth_win, 1,1,1,1)
        _rxfirswitch_check_box = Qt.QCheckBox("Write FIR File")
        self._rxfirswitch_choices = {True: True, False: False}
        self._rxfirswitch_choices_inv = dict((v,k) for k,v in self._rxfirswitch_choices.iteritems())
        self._rxfirswitch_callback = lambda i: Qt.QMetaObject.invokeMethod(_rxfirswitch_check_box, "setChecked", Qt.Q_ARG("bool", self._rxfirswitch_choices_inv[i]))
        self._rxfirswitch_callback(self.rxfirswitch)
        _rxfirswitch_check_box.stateChanged.connect(lambda i: self.set_rxfirswitch(self._rxfirswitch_choices[bool(i)]))
        self.tab_grid_layout_0.addWidget(_rxfirswitch_check_box, 3,0,1,1)
        self._rxfirfilterskirt_range = Range(1, 100000, 10, 10000, 10)
        self._rxfirfilterskirt_win = RangeWidget(self._rxfirfilterskirt_range, self.set_rxfirfilterskirt, "RX FIR Filter Skirt", "counter_slider", float)
        self.tab_grid_layout_4.addWidget(self._rxfirfilterskirt_win, 1,2,1,1)
        _rxfirfile_check_box = Qt.QCheckBox("Read FIR File")
        self._rxfirfile_choices = {True: True, False: False}
        self._rxfirfile_choices_inv = dict((v,k) for k,v in self._rxfirfile_choices.iteritems())
        self._rxfirfile_callback = lambda i: Qt.QMetaObject.invokeMethod(_rxfirfile_check_box, "setChecked", Qt.Q_ARG("bool", self._rxfirfile_choices_inv[i]))
        self._rxfirfile_callback(self.rxfirfile)
        _rxfirfile_check_box.stateChanged.connect(lambda i: self.set_rxfirfile(self._rxfirfile_choices[bool(i)]))
        self.tab_grid_layout_0.addWidget(_rxfirfile_check_box, 4,0,1,1)
        _rxfilterswitch_check_box = Qt.QCheckBox("Filter RX Audio")
        self._rxfilterswitch_choices = {True: 1, False: 0}
        self._rxfilterswitch_choices_inv = dict((v,k) for k,v in self._rxfilterswitch_choices.iteritems())
        self._rxfilterswitch_callback = lambda i: Qt.QMetaObject.invokeMethod(_rxfilterswitch_check_box, "setChecked", Qt.Q_ARG("bool", self._rxfilterswitch_choices_inv[i]))
        self._rxfilterswitch_callback(self.rxfilterswitch)
        _rxfilterswitch_check_box.stateChanged.connect(lambda i: self.set_rxfilterswitch(self._rxfilterswitch_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_rxfilterswitch_check_box, 3,0,1,1)
        self._rxbandwidth_tool_bar = Qt.QToolBar(self)
        self._rxbandwidth_tool_bar.addWidget(Qt.QLabel("BladeRF RX Bandwidth"+": "))
        self._rxbandwidth_line_edit = Qt.QLineEdit(str(self.rxbandwidth))
        self._rxbandwidth_tool_bar.addWidget(self._rxbandwidth_line_edit)
        self._rxbandwidth_line_edit.returnPressed.connect(
        	lambda: self.set_rxbandwidth(eng_notation.str_to_num(str(self._rxbandwidth_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._rxbandwidth_tool_bar, 4,2,1,1)
        self._rxaudioskirt_tool_bar = Qt.QToolBar(self)
        self._rxaudioskirt_tool_bar.addWidget(Qt.QLabel("RX Audio Filter Skirt (Hz)"+": "))
        self._rxaudioskirt_line_edit = Qt.QLineEdit(str(self.rxaudioskirt))
        self._rxaudioskirt_tool_bar.addWidget(self._rxaudioskirt_line_edit)
        self._rxaudioskirt_line_edit.returnPressed.connect(
        	lambda: self.set_rxaudioskirt(eng_notation.str_to_num(str(self._rxaudioskirt_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._rxaudioskirt_tool_bar, 3,3,1,1)
        self._rxaudiolow_tool_bar = Qt.QToolBar(self)
        self._rxaudiolow_tool_bar.addWidget(Qt.QLabel("RX Audio High Pass (Hz)"+": "))
        self._rxaudiolow_line_edit = Qt.QLineEdit(str(self.rxaudiolow))
        self._rxaudiolow_tool_bar.addWidget(self._rxaudiolow_line_edit)
        self._rxaudiolow_line_edit.returnPressed.connect(
        	lambda: self.set_rxaudiolow(eng_notation.str_to_num(str(self._rxaudiolow_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._rxaudiolow_tool_bar, 3,1,1,1)
        self._rxaudiohigh_tool_bar = Qt.QToolBar(self)
        self._rxaudiohigh_tool_bar.addWidget(Qt.QLabel("RX Audio Low Pass (Hz)"+": "))
        self._rxaudiohigh_line_edit = Qt.QLineEdit(str(self.rxaudiohigh))
        self._rxaudiohigh_tool_bar.addWidget(self._rxaudiohigh_line_edit)
        self._rxaudiohigh_line_edit.returnPressed.connect(
        	lambda: self.set_rxaudiohigh(eng_notation.str_to_num(str(self._rxaudiohigh_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._rxaudiohigh_tool_bar, 3,2,1,1)
        _rxagcswitch_check_box = Qt.QCheckBox("Enable RX Audio AGC")
        self._rxagcswitch_choices = {True: 1, False: 0}
        self._rxagcswitch_choices_inv = dict((v,k) for k,v in self._rxagcswitch_choices.iteritems())
        self._rxagcswitch_callback = lambda i: Qt.QMetaObject.invokeMethod(_rxagcswitch_check_box, "setChecked", Qt.Q_ARG("bool", self._rxagcswitch_choices_inv[i]))
        self._rxagcswitch_callback(self.rxagcswitch)
        _rxagcswitch_check_box.stateChanged.connect(lambda i: self.set_rxagcswitch(self._rxagcswitch_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_rxagcswitch_check_box, 5,0,1,1)
        _rx_check_box = Qt.QCheckBox("RX")
        self._rx_choices = {True: 1, False: 0}
        self._rx_choices_inv = dict((v,k) for k,v in self._rx_choices.iteritems())
        self._rx_callback = lambda i: Qt.QMetaObject.invokeMethod(_rx_check_box, "setChecked", Qt.Q_ARG("bool", self._rx_choices_inv[i]))
        self._rx_callback(self.rx)
        _rx_check_box.stateChanged.connect(lambda i: self.set_rx(self._rx_choices[bool(i)]))
        self.tab_grid_layout_0.addWidget(_rx_check_box, 0,0,1,1)
        _readafscratch_check_box = Qt.QCheckBox("Read AF from File")
        self._readafscratch_choices = {True: 1, False: 0}
        self._readafscratch_choices_inv = dict((v,k) for k,v in self._readafscratch_choices.iteritems())
        self._readafscratch_callback = lambda i: Qt.QMetaObject.invokeMethod(_readafscratch_check_box, "setChecked", Qt.Q_ARG("bool", self._readafscratch_choices_inv[i]))
        self._readafscratch_callback(self.readafscratch)
        _readafscratch_check_box.stateChanged.connect(lambda i: self.set_readafscratch(self._readafscratch_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_readafscratch_check_box, 7,3,1,1)
        _protect_check_box = Qt.QCheckBox("Zero RX gains if TX")
        self._protect_choices = {True: 1, False: 0}
        self._protect_choices_inv = dict((v,k) for k,v in self._protect_choices.iteritems())
        self._protect_callback = lambda i: Qt.QMetaObject.invokeMethod(_protect_check_box, "setChecked", Qt.Q_ARG("bool", self._protect_choices_inv[i]))
        self._protect_callback(self.protect)
        _protect_check_box.stateChanged.connect(lambda i: self.set_protect(self._protect_choices[bool(i)]))
        self.tab_grid_layout_0.addWidget(_protect_check_box, 3,1,1,1)
        self._pltone_0_tool_bar = Qt.QToolBar(self)
        self._pltone_0_tool_bar.addWidget(Qt.QLabel("PL Tone Signal Amplitude"+": "))
        self._pltone_0_line_edit = Qt.QLineEdit(str(self.pltone_0))
        self._pltone_0_tool_bar.addWidget(self._pltone_0_line_edit)
        self._pltone_0_line_edit.returnPressed.connect(
        	lambda: self.set_pltone_0(eng_notation.str_to_num(str(self._pltone_0_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._pltone_0_tool_bar, 1,1,1,1)
        self._pltone_range = Range(0, 500, 1, 100, 10)
        self._pltone_win = RangeWidget(self._pltone_range, self.set_pltone, "PL Tone Frequency", "counter_slider", float)
        self.tab_grid_layout_2.addWidget(self._pltone_win, 1,2,1,1)
        _mute_check_box = Qt.QCheckBox("Mute RX Audio during TX")
        self._mute_choices = {True: 1, False: 0}
        self._mute_choices_inv = dict((v,k) for k,v in self._mute_choices.iteritems())
        self._mute_callback = lambda i: Qt.QMetaObject.invokeMethod(_mute_check_box, "setChecked", Qt.Q_ARG("bool", self._mute_choices_inv[i]))
        self._mute_callback(self.mute)
        _mute_check_box.stateChanged.connect(lambda i: self.set_mute(self._mute_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_mute_check_box, 0,0,1,1)
        self._micvolume_range = Range(0, 100, .1, 1, 10)
        self._micvolume_win = RangeWidget(self._micvolume_range, self.set_micvolume, "Microphone Input Volume", "slider", float)
        self.tab_grid_layout_2.addWidget(self._micvolume_win, 0,2,1,1)
        self._lnagain_range = Range(0, 6, 3, 0, 10)
        self._lnagain_win = RangeWidget(self._lnagain_range, self.set_lnagain, "BladeRF RX LNA Gain (dB)", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._lnagain_win, 1,1,1,1)
        self._firfiletxamplitude_range = Range(1, 1000, 10, 100, 10)
        self._firfiletxamplitude_win = RangeWidget(self._firfiletxamplitude_range, self.set_firfiletxamplitude, "TX FIR File Multiplier", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._firfiletxamplitude_win, 2,1,1,1)
        _cwkey_push_button = Qt.QPushButton("CW Key")
        self._cwkey_choices = {'Pressed': 1, 'Released': 0}
        _cwkey_push_button.pressed.connect(lambda: self.set_cwkey(self._cwkey_choices['Pressed']))
        _cwkey_push_button.released.connect(lambda: self.set_cwkey(self._cwkey_choices['Released']))
        self.tab_grid_layout_1.addWidget(_cwkey_push_button, 4,1,1,1)
        self._audiofftmagnification_range = Range(1, 100, .1, 15, 10)
        self._audiofftmagnification_win = RangeWidget(self._audiofftmagnification_range, self.set_audiofftmagnification, "Audio FFT Magnification Factor", "slider", float)
        self.tab_grid_layout_5.addWidget(self._audiofftmagnification_win, 0,1,1,1)
        self._amplitude_range = Range(0, 1, .01, 1, 10)
        self._amplitude_win = RangeWidget(self._amplitude_range, self.set_amplitude, "Heterodyne Amplitude Output", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._amplitude_win, 1,3,1,1)
        self._ampl_tool_bar = Qt.QToolBar(self)
        self._ampl_tool_bar.addWidget(Qt.QLabel("Tri-Tone Amplitude"+": "))
        self._ampl_line_edit = Qt.QLineEdit(str(self.ampl))
        self._ampl_tool_bar.addWidget(self._ampl_line_edit)
        self._ampl_line_edit.returnPressed.connect(
        	lambda: self.set_ampl(eng_notation.str_to_num(str(self._ampl_line_edit.text().toAscii()))))
        self.tab_grid_layout_2.addWidget(self._ampl_tool_bar, 1,3,1,1)
        self._afscratchvolume_range = Range(0, 10, .1, 1, 10)
        self._afscratchvolume_win = RangeWidget(self._afscratchvolume_range, self.set_afscratchvolume, "Audio Scratch Volume", "slider", float)
        self.tab_grid_layout_2.addWidget(self._afscratchvolume_win, 7,1,1,1)
        self.txsinkselector = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=3,
        	input_index=0,
        	output_index=txsink,
        )
        self._txfirtuning_tool_bar = Qt.QToolBar(self)
        self._txfirtuning_tool_bar.addWidget(Qt.QLabel("TX FIR Signal Offset"+": "))
        self._txfirtuning_line_edit = Qt.QLineEdit(str(self.txfirtuning))
        self._txfirtuning_tool_bar.addWidget(self._txfirtuning_line_edit)
        self._txfirtuning_line_edit.returnPressed.connect(
        	lambda: self.set_txfirtuning(eng_notation.str_to_num(str(self._txfirtuning_line_edit.text().toAscii()))))
        self.tab_grid_layout_1.addWidget(self._txfirtuning_tool_bar, 0,2,1,1)
        self._txfirdisplay_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._txfirdisplay_formatter = None
        else:
          self._txfirdisplay_formatter = lambda x: x
        
        self._txfirdisplay_tool_bar.addWidget(Qt.QLabel("TX FIR Actual Frequency"+": "))
        self._txfirdisplay_label = Qt.QLabel(str(self._txfirdisplay_formatter(self.txfirdisplay)))
        self._txfirdisplay_tool_bar.addWidget(self._txfirdisplay_label)
        self.tab_grid_layout_1.addWidget(self._txfirdisplay_tool_bar, 0,3,1,1)
          
        self.txfilterselector = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=txfilterswitch,
        	output_index=0,
        )
        self.txdatamodulationselector = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=1,
        	input_index=txdatamodulation,
        	output_index=0,
        )
        self.tx_audio_band_pass_filter = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	1, audio_rate, txaudiolow, txaudiohigh, txaudioskirt, firdes.WIN_HAMMING, 6.76))
        _tritoneswitch_check_box = Qt.QCheckBox("Generate Tri-Tone")
        self._tritoneswitch_choices = {True: 1, False: 0}
        self._tritoneswitch_choices_inv = dict((v,k) for k,v in self._tritoneswitch_choices.iteritems())
        self._tritoneswitch_callback = lambda i: Qt.QMetaObject.invokeMethod(_tritoneswitch_check_box, "setChecked", Qt.Q_ARG("bool", self._tritoneswitch_choices_inv[i]))
        self._tritoneswitch_callback(self.tritoneswitch)
        _tritoneswitch_check_box.stateChanged.connect(lambda i: self.set_tritoneswitch(self._tritoneswitch_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_tritoneswitch_check_box, 2,0,1,1)
        _rxtx_check_box = Qt.QCheckBox("Enable TX RXed Audio")
        self._rxtx_choices = {True: 1, False: 0}
        self._rxtx_choices_inv = dict((v,k) for k,v in self._rxtx_choices.iteritems())
        self._rxtx_callback = lambda i: Qt.QMetaObject.invokeMethod(_rxtx_check_box, "setChecked", Qt.Q_ARG("bool", self._rxtx_choices_inv[i]))
        self._rxtx_callback(self.rxtx)
        _rxtx_check_box.stateChanged.connect(lambda i: self.set_rxtx(self._rxtx_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_rxtx_check_box, 6,1,1,1)
        self.rxsourceselector = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=3,
        	num_outputs=2,
        	input_index=rxsource,
        	output_index=rx,
        )
        (self.rxsourceselector).set_processor_affinity([4])
        self._rxfirtuning_tool_bar = Qt.QToolBar(self)
        self._rxfirtuning_tool_bar.addWidget(Qt.QLabel("RX FIR Frequency Offset"+": "))
        self._rxfirtuning_line_edit = Qt.QLineEdit(str(self.rxfirtuning))
        self._rxfirtuning_tool_bar.addWidget(self._rxfirtuning_line_edit)
        self._rxfirtuning_line_edit.returnPressed.connect(
        	lambda: self.set_rxfirtuning(eng_notation.str_to_num(str(self._rxfirtuning_line_edit.text().toAscii()))))
        self.tab_grid_layout_0.addWidget(self._rxfirtuning_tool_bar, 0,2,1,1)
        self._rxdatamodulation_options = (0, )
        self._rxdatamodulation_labels = ("ATSC Television", )
        self._rxdatamodulation_tool_bar = Qt.QToolBar(self)
        self._rxdatamodulation_tool_bar.addWidget(Qt.QLabel("RX Data Modulation"+": "))
        self._rxdatamodulation_combo_box = Qt.QComboBox()
        self._rxdatamodulation_tool_bar.addWidget(self._rxdatamodulation_combo_box)
        for label in self._rxdatamodulation_labels: self._rxdatamodulation_combo_box.addItem(label)
        self._rxdatamodulation_callback = lambda i: Qt.QMetaObject.invokeMethod(self._rxdatamodulation_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._rxdatamodulation_options.index(i)))
        self._rxdatamodulation_callback(self.rxdatamodulation)
        self._rxdatamodulation_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_rxdatamodulation(self._rxdatamodulation_options[i]))
        self.tab_grid_layout_3.addWidget(self._rxdatamodulation_tool_bar, 0,2,1,1)
        _rxdata_check_box = Qt.QCheckBox("Enable RX Data Modulation")
        self._rxdata_choices = {True: 1, False: 0}
        self._rxdata_choices_inv = dict((v,k) for k,v in self._rxdata_choices.iteritems())
        self._rxdata_callback = lambda i: Qt.QMetaObject.invokeMethod(_rxdata_check_box, "setChecked", Qt.Q_ARG("bool", self._rxdata_choices_inv[i]))
        self._rxdata_callback(self.rxdata)
        _rxdata_check_box.stateChanged.connect(lambda i: self.set_rxdata(self._rxdata_choices[bool(i)]))
        self.tab_grid_layout_3.addWidget(_rxdata_check_box, 0,0,1,1)
        self.rxaudiofilterselector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=rxfilterswitch,
        	output_index=0,
        )
        self.rx_selector = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=5,
        	input_index=0,
        	output_index=rxmodulation,
        )
        (self.rx_selector).set_processor_affinity([2])
        self.rx_audio_band_pass_filter = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	1, audio_rate, rxaudiolow, rxaudiohigh, rxaudioskirt, firdes.WIN_HAMMING, 6.76))
        self.rational_resampler_xxx_3_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        (self.rational_resampler_xxx_3_0).set_processor_affinity([4])
        self.rational_resampler_xxx_3 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        (self.rational_resampler_xxx_3).set_processor_affinity([4])
        self.rational_resampler_xxx_2_0_0_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate / audio_rate,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_2_0_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate / audio_rate,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=samp_rate / audio_rate ,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=audiofftmagnification,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_2_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate / nbfmtxrate,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        (self.rational_resampler_xxx_0_2_0).set_processor_affinity([4])
        self.rational_resampler_xxx_0_1_0_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate / firrate,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate / firrate *2,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=2,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_waterfall_sink_x_2 = qtgui.waterfall_sink_c(
        	1024 * 6, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_2.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_2.enable_grid(False)
        
        if not True:
          self.qtgui_waterfall_sink_x_2.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_2.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_2.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_2.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_2.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_2_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_2.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_2_win, 0,2,1,1)
        self.qtgui_waterfall_sink_x_1_0 = qtgui.waterfall_sink_f(
        	1024 * 3, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate / audiofftmagnification, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_1_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_1_0.enable_grid(False)
        
        if not True:
          self.qtgui_waterfall_sink_x_1_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_waterfall_sink_x_1_0.set_plot_pos_half(not False)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_1_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_1_0.set_intensity_range(-90, 0)
        
        self._qtgui_waterfall_sink_x_1_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.tab2_layout_5.addWidget(self._qtgui_waterfall_sink_x_1_0_win)
        self.qtgui_waterfall_sink_x_1 = qtgui.waterfall_sink_f(
        	1024 * 3, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate / audiofftmagnification * 10, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_1.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_1.enable_grid(False)
        
        if not True:
          self.qtgui_waterfall_sink_x_1.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_waterfall_sink_x_1.set_plot_pos_half(not False)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_1.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_1.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab2_layout_1.addWidget(self._qtgui_waterfall_sink_x_1_win)
        self.qtgui_waterfall_sink_x_0_0 = qtgui.waterfall_sink_c(
        	10000 * 2, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	rxfirwidth, #bw
        	"FIR Waterfall", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0_0.set_update_time(0.01)
        self.qtgui_waterfall_sink_x_0_0.enable_grid(True)
        
        if not True:
          self.qtgui_waterfall_sink_x_0_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0_0.set_intensity_range(-140, -20)
        
        self._qtgui_waterfall_sink_x_0_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.tab2_layout_4.addWidget(self._qtgui_waterfall_sink_x_0_0_win)
        (self.qtgui_waterfall_sink_x_0_0).set_processor_affinity([7])
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
        	10240 * 2, #size
        	firdes.WIN_KAISER, #wintype
        	0, #fc
        	samp_rate, #bw
        	"RX Waterfall", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.01)
        self.qtgui_waterfall_sink_x_0.enable_grid(True)
        
        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-110, -20)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.tab2_layout_0.addWidget(self._qtgui_waterfall_sink_x_0_win)
        (self.qtgui_waterfall_sink_x_0).set_processor_affinity([3])
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
        	4096 * 2, #size
        	audio_rate, #samp_rate
        	"RX Audio Output Scope", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_win, 0,0,1,1)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	4096 * 2, #size
        	audio_rate, #samp_rate
        	"TX Audio Input Scope", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win, 0,1,1,1)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	4096 * 2, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	rxfirwidth, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.01)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-140, 0)
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(True)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.tab2_layout_3.addWidget(self._qtgui_freq_sink_x_1_0_win)
        (self.qtgui_freq_sink_x_1_0).set_processor_affinity([5])
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024 * 2, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.01)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 0)
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(True)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.tab2_layout_2.addWidget(self._qtgui_freq_sink_x_1_win)
        _pltoneswitch_check_box = Qt.QCheckBox("Generate PL Tone")
        self._pltoneswitch_choices = {True: 1, False: 0}
        self._pltoneswitch_choices_inv = dict((v,k) for k,v in self._pltoneswitch_choices.iteritems())
        self._pltoneswitch_callback = lambda i: Qt.QMetaObject.invokeMethod(_pltoneswitch_check_box, "setChecked", Qt.Q_ARG("bool", self._pltoneswitch_choices_inv[i]))
        self._pltoneswitch_callback(self.pltoneswitch)
        _pltoneswitch_check_box.stateChanged.connect(lambda i: self.set_pltoneswitch(self._pltoneswitch_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_pltoneswitch_check_box, 1,0,1,1)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "bladerf=0,xb200,verbosity=verbose,buffers=128" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(txfreq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(txvga2gain if tx else 0, 0)
        self.osmosdr_sink_0.set_if_gain(0, 0)
        self.osmosdr_sink_0.set_bb_gain(txvga1gain if tx else -35, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(txbandwidth, 0)
          
        (self.osmosdr_sink_0).set_processor_affinity([3])
        _muteaudioout_check_box = Qt.QCheckBox("Audio Mute")
        self._muteaudioout_choices = {True: 1, False: 0}
        self._muteaudioout_choices_inv = dict((v,k) for k,v in self._muteaudioout_choices.iteritems())
        self._muteaudioout_callback = lambda i: Qt.QMetaObject.invokeMethod(_muteaudioout_check_box, "setChecked", Qt.Q_ARG("bool", self._muteaudioout_choices_inv[i]))
        self._muteaudioout_callback(self.muteaudioout)
        _muteaudioout_check_box.stateChanged.connect(lambda i: self.set_muteaudioout(self._muteaudioout_choices[bool(i)]))
        self.tab_grid_layout_2.addWidget(_muteaudioout_check_box, 6,2,1,1)
        self.interp_fir_filter_xxx_0_1 = filter.interp_fir_filter_ccc(1, (firdes.low_pass_2(1, samp_rate, txfirfilterwidth,txfirfilterskirt, 40,  firdes.WIN_RECTANGULAR, 6.76)))
        self.interp_fir_filter_xxx_0_1.declare_sample_delay(0)
        (self.interp_fir_filter_xxx_0_1).set_processor_affinity([6])
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(samp_rate / firrate, (filter.firdes.low_pass(1,samp_rate,rxfirwidth,rxfirfilterskirt,filter.firdes.WIN_FLATTOP)), rxoffset, samp_rate)
        (self.freq_xlating_fir_filter_xxx_0).set_processor_affinity([7])
        (self.freq_xlating_fir_filter_xxx_0).set_min_output_buffer(2000)
        (self.freq_xlating_fir_filter_xxx_0).set_max_output_buffer(10000)
        self._finetxfirtune_range = Range(-1000, 1000, 1, 0, 10)
        self._finetxfirtune_win = RangeWidget(self._finetxfirtune_range, self.set_finetxfirtune, "TX FIR Fine Tuning", "counter_slider", float)
        self.tab_grid_layout_1.addWidget(self._finetxfirtune_win, 3,2,1,3)
        self._finerxfirtune_range = Range(-1000, 1000, 1, 0, 10)
        self._finerxfirtune_win = RangeWidget(self._finerxfirtune_range, self.set_finerxfirtune, "RX FIR Fine Tuning", "counter_slider", float)
        self.tab_grid_layout_0.addWidget(self._finerxfirtune_win, 3,2,1,3)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, (firdes.root_raised_cosine(0.1, symbol_rate, symbol_rate/2, 0.1152, 100)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.dtv_atsc_trellis_encoder_0 = dtv.atsc_trellis_encoder()
        self.dtv_atsc_rs_encoder_0 = dtv.atsc_rs_encoder()
        self.dtv_atsc_randomizer_0 = dtv.atsc_randomizer()
        self.dtv_atsc_pad_0 = dtv.atsc_pad()
        self.dtv_atsc_interleaver_0 = dtv.atsc_interleaver()
        self.dtv_atsc_field_sync_mux_0 = dtv.atsc_field_sync_mux()
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(([symbol + 1.25 for symbol in [-7,-5,-3,-1,1,3,5,7]]), 1)
        self.blocks_wavfile_source_0_0 = blocks.wavfile_source("/home/goatman/radiodata/doorbell2.wav", True)
        self.blocks_vector_to_stream_1 = blocks.vector_to_stream(gr.sizeof_char*1, 1024)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_char*1, samp_rate if (txdata and tx) else 0,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_null_source_1 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_1_3 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_1_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_xx_0_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1_0_0_0_3_0 = blocks.multiply_const_vcc((rxoutputgain, ))
        self.blocks_multiply_const_vxx_1_0_0_0_3 = blocks.multiply_const_vcc((rxoutputgain, ))
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_vcc((rxoutputgain, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc((firfiletxamplitude, ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vff((micvolume, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((0 if (tx and mute) else rxvolume, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((wavvolume, ))
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_char, 832, 1024, 4)
        self.blocks_integrate_xx_0 = blocks.integrate_ff(audiofftmagnification * 10, 1)
        self.blocks_float_to_complex_0_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_1_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/goatman/radiodata/rxfirfile.iq" if rxfirfile else "/dev/zero", True)
        self.blocks_file_source_1 = blocks.file_source(gr.sizeof_float*1, "/home/goatman/radiodata/afscratch.raw" if readafscratch else "/dev/zero", True)
        self.blocks_file_source_0_1 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/goatman/radiodata/rxfirfile.iq", True)
        (self.blocks_file_source_0_1).set_processor_affinity([2])
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_char*1, "/home/goatman/radiodata/advatsc.ts", False)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/goatman/radiodata/rxiqfile.iq", True)
        (self.blocks_file_source_0).set_processor_affinity([2])
        self.blocks_file_sink_1_0_1 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/goatman/radiodata/rxfirfile.iq" if rxfirswitch else "/dev/null", False)
        self.blocks_file_sink_1_0_1.set_unbuffered(False)
        self.blocks_file_sink_1_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/goatman/radiodata/txiqfile.iq", False)
        self.blocks_file_sink_1_0_0.set_unbuffered(False)
        self.blocks_file_sink_1_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/goatman/radiodata/rxiqfile.iq" if rxiqswitch else "/dev/null", False)
        self.blocks_file_sink_1_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, "/home/goatman/radiodata/afscratch.raw" if writeafscratch else "/dev/null", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blks2_selector_3 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=txdata,
        	output_index=0,
        )
        self.blks2_selector_2 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=rxfirfile,
        	output_index=0,
        )
        self.blks2_selector_1_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=1,
        	num_outputs=2,
        	input_index=0,
        	output_index=tx,
        )
        self.blks2_selector_1 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=txfirfile,
        	output_index=0,
        )
        self.blks2_selector_0_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=5,
        	num_outputs=1,
        	input_index=rxmodulation,
        	output_index=0,
        )
        (self.blks2_selector_0_0_0).set_processor_affinity([7])
        self.blks2_selector_0_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=1,
        	num_outputs=5,
        	input_index=0,
        	output_index=txmodulation,
        )
        (self.blks2_selector_0_0).set_processor_affinity([2])
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=5,
        	num_outputs=1,
        	input_index=txmodulation,
        	output_index=0,
        )
        self.band_pass_filter_0_2 = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, audio_rate, -10000, -50, 50, firdes.WIN_RECTANGULAR, 6.76))
        self.band_pass_filter_0_1 = filter.interp_fir_filter_ccc(1, firdes.complex_band_pass(
        	txfiltergain, audio_rate, -10000, 10000, 500, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0 = filter.interp_fir_filter_ccc(1, firdes.complex_band_pass(
        	txfiltergain, audio_rate, -5000, -200, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.interp_fir_filter_ccc(1, firdes.complex_band_pass(
        	txfiltergain, audio_rate, 200, 5000, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter = filter.fir_filter_ccc(1, firdes.complex_band_pass(
        	1, 96000, 50, 10000, 50, firdes.WIN_RECTANGULAR, 6.76))
        (self.band_pass_filter).set_processor_affinity([4])
        self.audioinputadd = blocks.add_vff(1)
        self.audio_source_0 = audio.source(audio_rate, "pulse", False)
        (self.audio_source_0).set_processor_affinity([3])
        self.audio_sink_0 = audio.sink(96000, "pulse", True)
        (self.audio_sink_0).set_block_alias("3")
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=192000,
        	tau=75e-6,
        	max_dev=75e3 ,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=wbfmrxrate ,
        	audio_decimation=wbfmrxrate / audio_rate,
        )
        self.analog_sig_source_x_1 = analog.sig_source_f(audio_rate, analog.GR_COS_WAVE, toneone, ampl, 0)
        self.analog_sig_source_x_0_4 = analog.sig_source_f(audio_rate, analog.GR_SIN_WAVE, 1000, cwkey, 0)
        self.analog_sig_source_x_0_3 = analog.sig_source_c(symbol_rate, analog.GR_COS_WAVE, -3000000+pilot_freq, 0.9, 0)
        self.analog_sig_source_x_0_2_0 = analog.sig_source_f(audio_rate, analog.GR_COS_WAVE, tonethree, ampl, 0)
        self.analog_sig_source_x_0_2 = analog.sig_source_f(audio_rate, analog.GR_COS_WAVE, tonetwo, ampl, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(audio_rate, analog.GR_SIN_WAVE, pltone, pltone_0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, txoffset, amplitude if tx else 0, 0)
        self.analog_pwr_squelch_xx_0_0_1_0_0 = analog.pwr_squelch_cc(squelch, 0.02, 0, False)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=nbfmtxrate,
        	tau=150e-6,
        	max_dev=10000,
        )
        (self.analog_nbfm_tx_0).set_processor_affinity([4])
        self.analog_nbfm_rx_0 = analog.nbfm_rx(
        	audio_rate=audio_rate,
        	quad_rate=nbfmrxrate * 2,
        	tau=75e-6,
        	max_dev=5000,
        )
        (self.analog_nbfm_rx_0).set_processor_affinity([7])
        self.analog_const_source_x_0_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=384000,
        	audio_decim=4,
        	audio_pass=10000,
        	audio_stop=11000,
        )
        self.analog_agc2_xx_0_0 = analog.agc2_ff(0.001, 10, .8, 1)
        self.analog_agc2_xx_0_0.set_max_gain(1 if not rxagcswitch else 65536)
        self.analog_agc2_xx_0 = analog.agc2_ff(.1, .1, 1.0 , 1.0)
        self.analog_agc2_xx_0.set_max_gain(1 if not txagcswitch else 65536)
        self.afscratchvolumeblock = blocks.multiply_const_vff((afscratchvolume, ))
        self.Osmocom_RX = osmosdr.source( args="numchan=" + str(1) + " " + "bladerf=0,xb200,verbosity=verbose,buffers=128" )
        self.Osmocom_RX.set_sample_rate(samp_rate)
        self.Osmocom_RX.set_center_freq(rxfreq, 0)
        self.Osmocom_RX.set_freq_corr(0, 0)
        self.Osmocom_RX.set_dc_offset_mode(0, 0)
        self.Osmocom_RX.set_iq_balance_mode(0, 0)
        self.Osmocom_RX.set_gain_mode(False, 0)
        self.Osmocom_RX.set_gain(0 if (tx and protect) else lnagain, 0)
        self.Osmocom_RX.set_if_gain(5 if (tx and protect) else rxvga1gain, 0)
        self.Osmocom_RX.set_bb_gain(0 if (tx and protect) else rxvga2gain, 0)
        self.Osmocom_RX.set_antenna("", 0)
        self.Osmocom_RX.set_bandwidth(rxbandwidth, 0)
          
        (self.Osmocom_RX).set_processor_affinity([7])

        ##################################################
        # Connections
        ##################################################
        self.connect((self.Osmocom_RX, 0), (self.rxsourceselector, 0))    
        self.connect((self.afscratchvolumeblock, 0), (self.blocks_add_xx_1, 1))    
        self.connect((self.analog_agc2_xx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.analog_agc2_xx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.analog_am_demod_cf_0, 0), (self.blks2_selector_0_0_0, 2))    
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.analog_const_source_x_0_0, 0), (self.blocks_float_to_complex_0_0, 1))    
        self.connect((self.analog_const_source_x_0_0_0, 0), (self.blocks_float_to_complex_0_0_0, 1))    
        self.connect((self.analog_nbfm_rx_0, 0), (self.blks2_selector_0_0_0, 0))    
        self.connect((self.analog_nbfm_tx_0, 0), (self.rational_resampler_xxx_0_2_0, 0))    
        self.connect((self.analog_pwr_squelch_xx_0_0_1_0_0, 0), (self.rx_selector, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_add_xx_0, 4))    
        self.connect((self.analog_sig_source_x_0_2_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0_3, 0), (self.blocks_multiply_xx_0_2, 0))    
        self.connect((self.analog_sig_source_x_0_4, 0), (self.blocks_add_xx_0, 5))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0, 3))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.blks2_selector_0_0_0, 1))    
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_0_1_0, 0))    
        self.connect((self.audio_source_0, 0), (self.blocks_add_xx_1, 0))    
        self.connect((self.audioinputadd, 0), (self.tx_audio_band_pass_filter, 0))    
        self.connect((self.audioinputadd, 0), (self.txfilterselector, 0))    
        self.connect((self.band_pass_filter, 0), (self.blocks_multiply_const_vxx_1_0_0_0_3, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.rational_resampler_xxx_2_0_0, 0))    
        self.connect((self.band_pass_filter_0_0, 0), (self.rational_resampler_xxx_2_0_0_0, 0))    
        self.connect((self.band_pass_filter_0_1, 0), (self.rational_resampler_xxx_2, 0))    
        self.connect((self.band_pass_filter_0_2, 0), (self.blocks_multiply_const_vxx_1_0, 0))    
        self.connect((self.blks2_selector_0, 0), (self.blks2_selector_1, 0))    
        self.connect((self.blks2_selector_0_0, 0), (self.analog_nbfm_tx_0, 0))    
        self.connect((self.blks2_selector_0_0, 1), (self.analog_wfm_tx_0, 0))    
        self.connect((self.blks2_selector_0_0, 2), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blks2_selector_0_0, 3), (self.blocks_float_to_complex_0_0, 0))    
        self.connect((self.blks2_selector_0_0, 4), (self.blocks_float_to_complex_0_0_0, 0))    
        self.connect((self.blks2_selector_0_0_0, 0), (self.analog_agc2_xx_0_0, 0))    
        self.connect((self.blks2_selector_1, 0), (self.interp_fir_filter_xxx_0_1, 0))    
        self.connect((self.blks2_selector_1_0, 1), (self.blks2_selector_0_0, 0))    
        self.connect((self.blks2_selector_1_0, 0), (self.blocks_null_sink_1_0, 0))    
        self.connect((self.blks2_selector_1_0, 1), (self.qtgui_time_sink_x_0_0_0, 0))    
        self.connect((self.blks2_selector_2, 0), (self.analog_pwr_squelch_xx_0_0_1_0_0, 0))    
        self.connect((self.blks2_selector_2, 0), (self.qtgui_freq_sink_x_1_0, 0))    
        self.connect((self.blks2_selector_2, 0), (self.qtgui_waterfall_sink_x_0_0, 0))    
        self.connect((self.blks2_selector_3, 0), (self.qtgui_waterfall_sink_x_2, 0))    
        self.connect((self.blks2_selector_3, 0), (self.txsinkselector, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blks2_selector_1_0, 0))    
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.blks2_selector_0_0_0, 3))    
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.blks2_selector_0_0_0, 4))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_throttle_1, 0))    
        self.connect((self.blocks_file_source_0_1, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.blocks_file_source_1, 0), (self.afscratchvolumeblock, 0))    
        self.connect((self.blocks_file_source_1_0, 0), (self.blks2_selector_2, 1))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.band_pass_filter_0_1, 0))    
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.blocks_float_to_complex_0_0_0, 0), (self.band_pass_filter_0_0, 0))    
        self.connect((self.blocks_integrate_xx_0, 0), (self.qtgui_waterfall_sink_x_1_0, 0))    
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audioinputadd, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_integrate_xx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.rational_resampler_xxx_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.rx_audio_band_pass_filter, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.rxaudiofilterselector_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.audioinputadd, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.rational_resampler_xxx_0_1_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_complex_to_real_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_0_0_0_3, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1_0_0_0_3_0, 0), (self.analog_am_demod_cf_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blks2_selector_3, 0))    
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.fft_filter_xxx_0, 0))    
        self.connect((self.blocks_null_source_1, 0), (self.blocks_throttle_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.rxsourceselector, 1))    
        self.connect((self.blocks_throttle_0_0, 0), (self.rxsourceselector, 2))    
        self.connect((self.blocks_throttle_1, 0), (self.dtv_atsc_pad_0, 0))    
        self.connect((self.blocks_vector_to_stream_1, 0), (self.blocks_keep_m_in_n_0, 0))    
        self.connect((self.blocks_wavfile_source_0_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_multiply_xx_0_2, 1))    
        self.connect((self.dtv_atsc_field_sync_mux_0, 0), (self.blocks_vector_to_stream_1, 0))    
        self.connect((self.dtv_atsc_interleaver_0, 0), (self.dtv_atsc_trellis_encoder_0, 0))    
        self.connect((self.dtv_atsc_pad_0, 0), (self.dtv_atsc_randomizer_0, 0))    
        self.connect((self.dtv_atsc_randomizer_0, 0), (self.dtv_atsc_rs_encoder_0, 0))    
        self.connect((self.dtv_atsc_rs_encoder_0, 0), (self.dtv_atsc_interleaver_0, 0))    
        self.connect((self.dtv_atsc_trellis_encoder_0, 0), (self.dtv_atsc_field_sync_mux_0, 0))    
        self.connect((self.fft_filter_xxx_0, 0), (self.txdatamodulationselector, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blks2_selector_2, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_file_sink_1_0_1, 0))    
        self.connect((self.interp_fir_filter_xxx_0_1, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0_1_0, 0), (self.blks2_selector_0, 1))    
        self.connect((self.rational_resampler_xxx_0_1_0_0, 0), (self.blks2_selector_1, 1))    
        self.connect((self.rational_resampler_xxx_0_2_0, 0), (self.blks2_selector_0, 0))    
        self.connect((self.rational_resampler_xxx_1, 0), (self.qtgui_waterfall_sink_x_1, 0))    
        self.connect((self.rational_resampler_xxx_2, 0), (self.blks2_selector_0, 2))    
        self.connect((self.rational_resampler_xxx_2_0_0, 0), (self.blks2_selector_0, 3))    
        self.connect((self.rational_resampler_xxx_2_0_0_0, 0), (self.blks2_selector_0, 4))    
        self.connect((self.rational_resampler_xxx_3, 0), (self.band_pass_filter, 0))    
        self.connect((self.rational_resampler_xxx_3_0, 0), (self.band_pass_filter_0_2, 0))    
        self.connect((self.rx_audio_band_pass_filter, 0), (self.rxaudiofilterselector_0, 1))    
        self.connect((self.rx_selector, 0), (self.analog_nbfm_rx_0, 0))    
        self.connect((self.rx_selector, 1), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.rx_selector, 2), (self.blocks_multiply_const_vxx_1_0_0_0_3_0, 0))    
        self.connect((self.rx_selector, 3), (self.rational_resampler_xxx_3, 0))    
        self.connect((self.rx_selector, 4), (self.rational_resampler_xxx_3_0, 0))    
        self.connect((self.rxaudiofilterselector_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.rxaudiofilterselector_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.rxaudiofilterselector_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))    
        self.connect((self.rxsourceselector, 1), (self.blocks_file_sink_1_0, 0))    
        self.connect((self.rxsourceselector, 0), (self.blocks_null_sink_1, 0))    
        self.connect((self.rxsourceselector, 1), (self.freq_xlating_fir_filter_xxx_0, 0))    
        self.connect((self.rxsourceselector, 1), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.rxsourceselector, 1), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.tx_audio_band_pass_filter, 0), (self.txfilterselector, 1))    
        self.connect((self.txdatamodulationselector, 0), (self.blks2_selector_3, 1))    
        self.connect((self.txfilterselector, 0), (self.analog_agc2_xx_0, 0))    
        self.connect((self.txsinkselector, 1), (self.blocks_file_sink_1_0_0, 0))    
        self.connect((self.txsinkselector, 2), (self.blocks_null_sink_1_3, 0))    
        self.connect((self.txsinkselector, 0), (self.osmosdr_sink_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Radio_Presidio_Prototype")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_txfirtuning(self):
        return self.txfirtuning

    def set_txfirtuning(self, txfirtuning):
        self.txfirtuning = txfirtuning
        Qt.QMetaObject.invokeMethod(self._txfirtuning_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.txfirtuning)))
        self.set_txoffset((self.finetxfirtune+self.txfirtuning))

    def get_rxfirtuning(self):
        return self.rxfirtuning

    def set_rxfirtuning(self, rxfirtuning):
        self.rxfirtuning = rxfirtuning
        Qt.QMetaObject.invokeMethod(self._rxfirtuning_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rxfirtuning)))
        self.set_rxoffset((self.finerxfirtune+self.rxfirtuning))

    def get_finetxfirtune(self):
        return self.finetxfirtune

    def set_finetxfirtune(self, finetxfirtune):
        self.finetxfirtune = finetxfirtune
        self.set_txoffset((self.finetxfirtune+self.txfirtuning))

    def get_finerxfirtune(self):
        return self.finerxfirtune

    def set_finerxfirtune(self, finerxfirtune):
        self.finerxfirtune = finerxfirtune
        self.set_rxoffset((self.finerxfirtune+self.rxfirtuning))

    def get_txoffset(self):
        return self.txoffset

    def set_txoffset(self, txoffset):
        self.txoffset = txoffset
        self.set_txfirdisplay(self._txfirdisplay_formatter(self.txfreq  + (self.txoffset)))
        self.analog_sig_source_x_0.set_frequency(self.txoffset)

    def get_txfreq(self):
        return self.txfreq

    def set_txfreq(self, txfreq):
        self.txfreq = txfreq
        self.set_txfirdisplay(self._txfirdisplay_formatter(self.txfreq  + (self.txoffset)))
        Qt.QMetaObject.invokeMethod(self._txfreq_line_edit, "setText", Qt.Q_ARG("QString", str(self.txfreq)))
        self.osmosdr_sink_0.set_center_freq(self.txfreq, 0)

    def get_tritoneswitch(self):
        return self.tritoneswitch

    def set_tritoneswitch(self, tritoneswitch):
        self.tritoneswitch = tritoneswitch
        self.set_ampl(0 if not self.tritoneswitch else 1)
        self._tritoneswitch_callback(self.tritoneswitch)

    def get_rxoffset(self):
        return self.rxoffset

    def set_rxoffset(self, rxoffset):
        self.rxoffset = rxoffset
        self.set_label(self._label_formatter(self.rxfreq  + (self.rxoffset)))
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.rxoffset)

    def get_rxfreq(self):
        return self.rxfreq

    def set_rxfreq(self, rxfreq):
        self.rxfreq = rxfreq
        self.set_label(self._label_formatter(self.rxfreq  + (self.rxoffset)))
        Qt.QMetaObject.invokeMethod(self._rxfreq_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rxfreq)))
        self.Osmocom_RX.set_center_freq(self.rxfreq, 0)

    def get_pltoneswitch(self):
        return self.pltoneswitch

    def set_pltoneswitch(self, pltoneswitch):
        self.pltoneswitch = pltoneswitch
        self.set_pltone_0(0 if not self.pltoneswitch else .2)
        self._pltoneswitch_callback(self.pltoneswitch)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.set_firrate(self.audio_rate * 4)
        self.set_nbfmrxrate(self.audio_rate * 2)
        self.set_wbfmrxrate(self.audio_rate * 4)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.audio_rate)
        self.analog_sig_source_x_0_2.set_sampling_freq(self.audio_rate)
        self.analog_sig_source_x_0_2_0.set_sampling_freq(self.audio_rate)
        self.analog_sig_source_x_0_4.set_sampling_freq(self.audio_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.audio_rate)
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(self.txfiltergain, self.audio_rate, 200, 5000, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(self.txfiltergain, self.audio_rate, -5000, -200, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.complex_band_pass(self.txfiltergain, self.audio_rate, -10000, 10000, 500, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_2.set_taps(firdes.complex_band_pass(1, self.audio_rate, -10000, -50, 50, firdes.WIN_RECTANGULAR, 6.76))
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.audio_rate)
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.audio_rate)
        self.qtgui_waterfall_sink_x_1.set_frequency_range(0, self.audio_rate / self.audiofftmagnification * 10)
        self.qtgui_waterfall_sink_x_1_0.set_frequency_range(0, self.audio_rate / self.audiofftmagnification)
        self.rx_audio_band_pass_filter.set_taps(firdes.band_pass(1, self.audio_rate, self.rxaudiolow, self.rxaudiohigh, self.rxaudioskirt, firdes.WIN_HAMMING, 6.76))
        self.tx_audio_band_pass_filter.set_taps(firdes.band_pass(1, self.audio_rate, self.txaudiolow, self.txaudiohigh, self.txaudioskirt, firdes.WIN_HAMMING, 6.76))

    def get_writeafscratch(self):
        return self.writeafscratch

    def set_writeafscratch(self, writeafscratch):
        self.writeafscratch = writeafscratch
        self._writeafscratch_callback(self.writeafscratch)
        self.blocks_file_sink_0.open("/home/goatman/radiodata/afscratch.raw" if self.writeafscratch else "/dev/null")

    def get_wbfmtxrate(self):
        return self.wbfmtxrate

    def set_wbfmtxrate(self, wbfmtxrate):
        self.wbfmtxrate = wbfmtxrate

    def get_wbfmrxrate(self):
        return self.wbfmrxrate

    def set_wbfmrxrate(self, wbfmrxrate):
        self.wbfmrxrate = wbfmrxrate

    def get_wavvolume(self):
        return self.wavvolume

    def set_wavvolume(self, wavvolume):
        self.wavvolume = wavvolume
        self.blocks_multiply_const_vxx_0.set_k((self.wavvolume, ))

    def get_wav_rate(self):
        return self.wav_rate

    def set_wav_rate(self, wav_rate):
        self.wav_rate = wav_rate

    def get_variable_0(self):
        return self.variable_0

    def set_variable_0(self, variable_0):
        self.variable_0 = variable_0

    def get_txvga2gain(self):
        return self.txvga2gain

    def set_txvga2gain(self, txvga2gain):
        self.txvga2gain = txvga2gain
        self.osmosdr_sink_0.set_gain(self.txvga2gain if self.tx else 0, 0)

    def get_txvga1gain(self):
        return self.txvga1gain

    def set_txvga1gain(self, txvga1gain):
        self.txvga1gain = txvga1gain
        self.osmosdr_sink_0.set_bb_gain(self.txvga1gain if self.tx else -35, 0)

    def get_txsink(self):
        return self.txsink

    def set_txsink(self, txsink):
        self.txsink = txsink
        self._txsink_callback(self.txsink)
        self.txsinkselector.set_output_index(int(self.txsink))

    def get_txmodulation(self):
        return self.txmodulation

    def set_txmodulation(self, txmodulation):
        self.txmodulation = txmodulation
        self._txmodulation_callback(self.txmodulation)
        self.blks2_selector_0.set_input_index(int(self.txmodulation))
        self.blks2_selector_0_0.set_output_index(int(self.txmodulation))

    def get_txfirfilterwidth(self):
        return self.txfirfilterwidth

    def set_txfirfilterwidth(self, txfirfilterwidth):
        self.txfirfilterwidth = txfirfilterwidth
        self.interp_fir_filter_xxx_0_1.set_taps((firdes.low_pass_2(1, self.samp_rate, self.txfirfilterwidth,self.txfirfilterskirt, 40,  firdes.WIN_RECTANGULAR, 6.76)))

    def get_txfirfilterskirt(self):
        return self.txfirfilterskirt

    def set_txfirfilterskirt(self, txfirfilterskirt):
        self.txfirfilterskirt = txfirfilterskirt
        self.interp_fir_filter_xxx_0_1.set_taps((firdes.low_pass_2(1, self.samp_rate, self.txfirfilterwidth,self.txfirfilterskirt, 40,  firdes.WIN_RECTANGULAR, 6.76)))

    def get_txfirfile(self):
        return self.txfirfile

    def set_txfirfile(self, txfirfile):
        self.txfirfile = txfirfile
        self._txfirfile_callback(self.txfirfile)
        self.blks2_selector_1.set_input_index(int(self.txfirfile))

    def get_txfirdisplay(self):
        return self.txfirdisplay

    def set_txfirdisplay(self, txfirdisplay):
        self.txfirdisplay = txfirdisplay
        Qt.QMetaObject.invokeMethod(self._txfirdisplay_label, "setText", Qt.Q_ARG("QString", str(self.txfirdisplay)))

    def get_txfilterswitch(self):
        return self.txfilterswitch

    def set_txfilterswitch(self, txfilterswitch):
        self.txfilterswitch = txfilterswitch
        self._txfilterswitch_callback(self.txfilterswitch)
        self.txfilterselector.set_input_index(int(self.txfilterswitch))

    def get_txfiltergain(self):
        return self.txfiltergain

    def set_txfiltergain(self, txfiltergain):
        self.txfiltergain = txfiltergain
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(self.txfiltergain, self.audio_rate, 200, 5000, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(self.txfiltergain, self.audio_rate, -5000, -200, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.complex_band_pass(self.txfiltergain, self.audio_rate, -10000, 10000, 500, firdes.WIN_HAMMING, 6.76))

    def get_txdatamodulation(self):
        return self.txdatamodulation

    def set_txdatamodulation(self, txdatamodulation):
        self.txdatamodulation = txdatamodulation
        self._txdatamodulation_callback(self.txdatamodulation)
        self.txdatamodulationselector.set_input_index(int(self.txdatamodulation))

    def get_txdata(self):
        return self.txdata

    def set_txdata(self, txdata):
        self.txdata = txdata
        self._txdata_callback(self.txdata)
        self.blks2_selector_3.set_input_index(int(self.txdata))
        self.blocks_throttle_1.set_sample_rate(self.samp_rate if (self.txdata and self.tx) else 0)

    def get_txbandwidth(self):
        return self.txbandwidth

    def set_txbandwidth(self, txbandwidth):
        self.txbandwidth = txbandwidth
        Qt.QMetaObject.invokeMethod(self._txbandwidth_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.txbandwidth)))
        self.osmosdr_sink_0.set_bandwidth(self.txbandwidth, 0)

    def get_txaudioskirt(self):
        return self.txaudioskirt

    def set_txaudioskirt(self, txaudioskirt):
        self.txaudioskirt = txaudioskirt
        Qt.QMetaObject.invokeMethod(self._txaudioskirt_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.txaudioskirt)))
        self.tx_audio_band_pass_filter.set_taps(firdes.band_pass(1, self.audio_rate, self.txaudiolow, self.txaudiohigh, self.txaudioskirt, firdes.WIN_HAMMING, 6.76))

    def get_txaudiolow(self):
        return self.txaudiolow

    def set_txaudiolow(self, txaudiolow):
        self.txaudiolow = txaudiolow
        Qt.QMetaObject.invokeMethod(self._txaudiolow_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.txaudiolow)))
        self.tx_audio_band_pass_filter.set_taps(firdes.band_pass(1, self.audio_rate, self.txaudiolow, self.txaudiohigh, self.txaudioskirt, firdes.WIN_HAMMING, 6.76))

    def get_txaudiohigh(self):
        return self.txaudiohigh

    def set_txaudiohigh(self, txaudiohigh):
        self.txaudiohigh = txaudiohigh
        Qt.QMetaObject.invokeMethod(self._txaudiohigh_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.txaudiohigh)))
        self.tx_audio_band_pass_filter.set_taps(firdes.band_pass(1, self.audio_rate, self.txaudiolow, self.txaudiohigh, self.txaudioskirt, firdes.WIN_HAMMING, 6.76))

    def get_txagcswitch(self):
        return self.txagcswitch

    def set_txagcswitch(self, txagcswitch):
        self.txagcswitch = txagcswitch
        self._txagcswitch_callback(self.txagcswitch)
        self.analog_agc2_xx_0.set_max_gain(1 if not self.txagcswitch else 65536)

    def get_tx(self):
        return self.tx

    def set_tx(self, tx):
        self.tx = tx
        self._tx_callback(self.tx)
        self.Osmocom_RX.set_gain(0 if (self.tx and self.protect) else self.lnagain, 0)
        self.Osmocom_RX.set_if_gain(5 if (self.tx and self.protect) else self.rxvga1gain, 0)
        self.Osmocom_RX.set_bb_gain(0 if (self.tx and self.protect) else self.rxvga2gain, 0)
        self.analog_sig_source_x_0.set_amplitude(self.amplitude if self.tx else 0)
        self.blks2_selector_1_0.set_output_index(int(self.tx))
        self.blocks_multiply_const_vxx_0_0.set_k((0 if (self.tx and self.mute) else self.rxvolume, ))
        self.blocks_throttle_1.set_sample_rate(self.samp_rate if (self.txdata and self.tx) else 0)
        self.osmosdr_sink_0.set_gain(self.txvga2gain if self.tx else 0, 0)
        self.osmosdr_sink_0.set_bb_gain(self.txvga1gain if self.tx else -35, 0)

    def get_tonetwo(self):
        return self.tonetwo

    def set_tonetwo(self, tonetwo):
        self.tonetwo = tonetwo
        Qt.QMetaObject.invokeMethod(self._tonetwo_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.tonetwo)))
        self.analog_sig_source_x_0_2.set_frequency(self.tonetwo)

    def get_tonethree(self):
        return self.tonethree

    def set_tonethree(self, tonethree):
        self.tonethree = tonethree
        Qt.QMetaObject.invokeMethod(self._tonethree_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.tonethree)))
        self.analog_sig_source_x_0_2_0.set_frequency(self.tonethree)

    def get_toneone(self):
        return self.toneone

    def set_toneone(self, toneone):
        self.toneone = toneone
        Qt.QMetaObject.invokeMethod(self._toneone_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.toneone)))
        self.analog_sig_source_x_1.set_frequency(self.toneone)

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.analog_sig_source_x_0_3.set_sampling_freq(self.symbol_rate)
        self.fft_filter_xxx_0.set_taps((firdes.root_raised_cosine(0.1, self.symbol_rate, self.symbol_rate/2, 0.1152, 100)))

    def get_sym_rate(self):
        return self.sym_rate

    def set_sym_rate(self, sym_rate):
        self.sym_rate = sym_rate

    def get_squelch(self):
        return self.squelch

    def set_squelch(self, squelch):
        self.squelch = squelch
        self.analog_pwr_squelch_xx_0_0_1_0_0.set_threshold(self.squelch)

    def get_sps_0(self):
        return self.sps_0

    def set_sps_0(self, sps_0):
        self.sps_0 = sps_0

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        Qt.QMetaObject.invokeMethod(self._samp_rate_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate)))
        self.Osmocom_RX.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate if (self.txdata and self.tx) else 0)
        self.freq_xlating_fir_filter_xxx_0.set_taps((filter.firdes.low_pass(1,self.samp_rate,self.rxfirwidth,self.rxfirfilterskirt,filter.firdes.WIN_FLATTOP)))
        self.interp_fir_filter_xxx_0_1.set_taps((firdes.low_pass_2(1, self.samp_rate, self.txfirfilterwidth,self.txfirfilterskirt, 40,  firdes.WIN_RECTANGULAR, 6.76)))
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_waterfall_sink_x_2.set_frequency_range(0, self.samp_rate)

    def get_rxvolume(self):
        return self.rxvolume

    def set_rxvolume(self, rxvolume):
        self.rxvolume = rxvolume
        self.blocks_multiply_const_vxx_0_0.set_k((0 if (self.tx and self.mute) else self.rxvolume, ))

    def get_rxvga2gain(self):
        return self.rxvga2gain

    def set_rxvga2gain(self, rxvga2gain):
        self.rxvga2gain = rxvga2gain
        self.Osmocom_RX.set_bb_gain(0 if (self.tx and self.protect) else self.rxvga2gain, 0)

    def get_rxvga1gain(self):
        return self.rxvga1gain

    def set_rxvga1gain(self, rxvga1gain):
        self.rxvga1gain = rxvga1gain
        self.Osmocom_RX.set_if_gain(5 if (self.tx and self.protect) else self.rxvga1gain, 0)

    def get_rxtx(self):
        return self.rxtx

    def set_rxtx(self, rxtx):
        self.rxtx = rxtx
        self._rxtx_callback(self.rxtx)

    def get_rxsource(self):
        return self.rxsource

    def set_rxsource(self, rxsource):
        self.rxsource = rxsource
        self._rxsource_callback(self.rxsource)
        self.rxsourceselector.set_input_index(int(self.rxsource))

    def get_rxoutputgain(self):
        return self.rxoutputgain

    def set_rxoutputgain(self, rxoutputgain):
        self.rxoutputgain = rxoutputgain
        Qt.QMetaObject.invokeMethod(self._rxoutputgain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rxoutputgain)))
        self.blocks_multiply_const_vxx_1_0.set_k((self.rxoutputgain, ))
        self.blocks_multiply_const_vxx_1_0_0_0_3.set_k((self.rxoutputgain, ))
        self.blocks_multiply_const_vxx_1_0_0_0_3_0.set_k((self.rxoutputgain, ))

    def get_rxmodulation(self):
        return self.rxmodulation

    def set_rxmodulation(self, rxmodulation):
        self.rxmodulation = rxmodulation
        self._rxmodulation_callback(self.rxmodulation)
        self.blks2_selector_0_0_0.set_input_index(int(self.rxmodulation))
        self.rx_selector.set_output_index(int(self.rxmodulation))

    def get_rxiqswitch(self):
        return self.rxiqswitch

    def set_rxiqswitch(self, rxiqswitch):
        self.rxiqswitch = rxiqswitch
        self._rxiqswitch_callback(self.rxiqswitch)
        self.blocks_file_sink_1_0.open("/home/goatman/radiodata/rxiqfile.iq" if self.rxiqswitch else "/dev/null")

    def get_rxfirwidth(self):
        return self.rxfirwidth

    def set_rxfirwidth(self, rxfirwidth):
        self.rxfirwidth = rxfirwidth
        self.freq_xlating_fir_filter_xxx_0.set_taps((filter.firdes.low_pass(1,self.samp_rate,self.rxfirwidth,self.rxfirfilterskirt,filter.firdes.WIN_FLATTOP)))
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.rxfirwidth)
        self.qtgui_waterfall_sink_x_0_0.set_frequency_range(0, self.rxfirwidth)

    def get_rxfirswitch(self):
        return self.rxfirswitch

    def set_rxfirswitch(self, rxfirswitch):
        self.rxfirswitch = rxfirswitch
        self._rxfirswitch_callback(self.rxfirswitch)
        self.blocks_file_sink_1_0_1.open("/home/goatman/radiodata/rxfirfile.iq" if self.rxfirswitch else "/dev/null")

    def get_rxfirfilterskirt(self):
        return self.rxfirfilterskirt

    def set_rxfirfilterskirt(self, rxfirfilterskirt):
        self.rxfirfilterskirt = rxfirfilterskirt
        self.freq_xlating_fir_filter_xxx_0.set_taps((filter.firdes.low_pass(1,self.samp_rate,self.rxfirwidth,self.rxfirfilterskirt,filter.firdes.WIN_FLATTOP)))

    def get_rxfirfile(self):
        return self.rxfirfile

    def set_rxfirfile(self, rxfirfile):
        self.rxfirfile = rxfirfile
        self._rxfirfile_callback(self.rxfirfile)
        self.blks2_selector_2.set_input_index(int(self.rxfirfile))
        self.blocks_file_source_1_0.open("/home/goatman/radiodata/rxfirfile.iq" if self.rxfirfile else "/dev/zero", True)

    def get_rxfilterswitch(self):
        return self.rxfilterswitch

    def set_rxfilterswitch(self, rxfilterswitch):
        self.rxfilterswitch = rxfilterswitch
        self._rxfilterswitch_callback(self.rxfilterswitch)
        self.rxaudiofilterselector_0.set_input_index(int(self.rxfilterswitch))

    def get_rxdatamodulation(self):
        return self.rxdatamodulation

    def set_rxdatamodulation(self, rxdatamodulation):
        self.rxdatamodulation = rxdatamodulation
        self._rxdatamodulation_callback(self.rxdatamodulation)

    def get_rxdata(self):
        return self.rxdata

    def set_rxdata(self, rxdata):
        self.rxdata = rxdata
        self._rxdata_callback(self.rxdata)

    def get_rxbandwidth(self):
        return self.rxbandwidth

    def set_rxbandwidth(self, rxbandwidth):
        self.rxbandwidth = rxbandwidth
        Qt.QMetaObject.invokeMethod(self._rxbandwidth_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rxbandwidth)))
        self.Osmocom_RX.set_bandwidth(self.rxbandwidth, 0)

    def get_rxaudioskirt(self):
        return self.rxaudioskirt

    def set_rxaudioskirt(self, rxaudioskirt):
        self.rxaudioskirt = rxaudioskirt
        Qt.QMetaObject.invokeMethod(self._rxaudioskirt_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rxaudioskirt)))
        self.rx_audio_band_pass_filter.set_taps(firdes.band_pass(1, self.audio_rate, self.rxaudiolow, self.rxaudiohigh, self.rxaudioskirt, firdes.WIN_HAMMING, 6.76))

    def get_rxaudiolow(self):
        return self.rxaudiolow

    def set_rxaudiolow(self, rxaudiolow):
        self.rxaudiolow = rxaudiolow
        Qt.QMetaObject.invokeMethod(self._rxaudiolow_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rxaudiolow)))
        self.rx_audio_band_pass_filter.set_taps(firdes.band_pass(1, self.audio_rate, self.rxaudiolow, self.rxaudiohigh, self.rxaudioskirt, firdes.WIN_HAMMING, 6.76))

    def get_rxaudiohigh(self):
        return self.rxaudiohigh

    def set_rxaudiohigh(self, rxaudiohigh):
        self.rxaudiohigh = rxaudiohigh
        Qt.QMetaObject.invokeMethod(self._rxaudiohigh_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.rxaudiohigh)))
        self.rx_audio_band_pass_filter.set_taps(firdes.band_pass(1, self.audio_rate, self.rxaudiolow, self.rxaudiohigh, self.rxaudioskirt, firdes.WIN_HAMMING, 6.76))

    def get_rxagcswitch(self):
        return self.rxagcswitch

    def set_rxagcswitch(self, rxagcswitch):
        self.rxagcswitch = rxagcswitch
        self._rxagcswitch_callback(self.rxagcswitch)
        self.analog_agc2_xx_0_0.set_max_gain(1 if not self.rxagcswitch else 65536)

    def get_rx(self):
        return self.rx

    def set_rx(self, rx):
        self.rx = rx
        self._rx_callback(self.rx)
        self.rxsourceselector.set_output_index(int(self.rx))

    def get_readafscratch(self):
        return self.readafscratch

    def set_readafscratch(self, readafscratch):
        self.readafscratch = readafscratch
        self._readafscratch_callback(self.readafscratch)
        self.blocks_file_source_1.open("/home/goatman/radiodata/afscratch.raw" if self.readafscratch else "/dev/zero", True)

    def get_protect(self):
        return self.protect

    def set_protect(self, protect):
        self.protect = protect
        self._protect_callback(self.protect)
        self.Osmocom_RX.set_gain(0 if (self.tx and self.protect) else self.lnagain, 0)
        self.Osmocom_RX.set_if_gain(5 if (self.tx and self.protect) else self.rxvga1gain, 0)
        self.Osmocom_RX.set_bb_gain(0 if (self.tx and self.protect) else self.rxvga2gain, 0)

    def get_pltone_0(self):
        return self.pltone_0

    def set_pltone_0(self, pltone_0):
        self.pltone_0 = pltone_0
        Qt.QMetaObject.invokeMethod(self._pltone_0_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.pltone_0)))
        self.analog_sig_source_x_0_0.set_amplitude(self.pltone_0)

    def get_pltone(self):
        return self.pltone

    def set_pltone(self, pltone):
        self.pltone = pltone
        self.analog_sig_source_x_0_0.set_frequency(self.pltone)

    def get_pilot_freq(self):
        return self.pilot_freq

    def set_pilot_freq(self, pilot_freq):
        self.pilot_freq = pilot_freq
        self.analog_sig_source_x_0_3.set_frequency(-3000000+self.pilot_freq)

    def get_nbfmtxrate(self):
        return self.nbfmtxrate

    def set_nbfmtxrate(self, nbfmtxrate):
        self.nbfmtxrate = nbfmtxrate

    def get_nbfmrxrate(self):
        return self.nbfmrxrate

    def set_nbfmrxrate(self, nbfmrxrate):
        self.nbfmrxrate = nbfmrxrate

    def get_muteaudioout(self):
        return self.muteaudioout

    def set_muteaudioout(self, muteaudioout):
        self.muteaudioout = muteaudioout
        self._muteaudioout_callback(self.muteaudioout)

    def get_mute(self):
        return self.mute

    def set_mute(self, mute):
        self.mute = mute
        self._mute_callback(self.mute)
        self.blocks_multiply_const_vxx_0_0.set_k((0 if (self.tx and self.mute) else self.rxvolume, ))

    def get_micvolume(self):
        return self.micvolume

    def set_micvolume(self, micvolume):
        self.micvolume = micvolume
        self.blocks_multiply_const_vxx_0_1.set_k((self.micvolume, ))

    def get_lnagain(self):
        return self.lnagain

    def set_lnagain(self, lnagain):
        self.lnagain = lnagain
        self.Osmocom_RX.set_gain(0 if (self.tx and self.protect) else self.lnagain, 0)

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label
        Qt.QMetaObject.invokeMethod(self._label_label, "setText", Qt.Q_ARG("QString", str(self.label)))

    def get_freq_shift(self):
        return self.freq_shift

    def set_freq_shift(self, freq_shift):
        self.freq_shift = freq_shift

    def get_fm_deviation(self):
        return self.fm_deviation

    def set_fm_deviation(self, fm_deviation):
        self.fm_deviation = fm_deviation

    def get_firrate(self):
        return self.firrate

    def set_firrate(self, firrate):
        self.firrate = firrate

    def get_firfiletxamplitude(self):
        return self.firfiletxamplitude

    def set_firfiletxamplitude(self, firfiletxamplitude):
        self.firfiletxamplitude = firfiletxamplitude
        self.blocks_multiply_const_vxx_1.set_k((self.firfiletxamplitude, ))

    def get_cwkey(self):
        return self.cwkey

    def set_cwkey(self, cwkey):
        self.cwkey = cwkey
        self.analog_sig_source_x_0_4.set_amplitude(self.cwkey)

    def get_audiofftmagnification(self):
        return self.audiofftmagnification

    def set_audiofftmagnification(self, audiofftmagnification):
        self.audiofftmagnification = audiofftmagnification
        self.qtgui_waterfall_sink_x_1.set_frequency_range(0, self.audio_rate / self.audiofftmagnification * 10)
        self.qtgui_waterfall_sink_x_1_0.set_frequency_range(0, self.audio_rate / self.audiofftmagnification)

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self.analog_sig_source_x_0.set_amplitude(self.amplitude if self.tx else 0)

    def get_ampl(self):
        return self.ampl

    def set_ampl(self, ampl):
        self.ampl = ampl
        Qt.QMetaObject.invokeMethod(self._ampl_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.ampl)))
        self.analog_sig_source_x_0_2.set_amplitude(self.ampl)
        self.analog_sig_source_x_0_2_0.set_amplitude(self.ampl)
        self.analog_sig_source_x_1.set_amplitude(self.ampl)

    def get_afscratchvolume(self):
        return self.afscratchvolume

    def set_afscratchvolume(self, afscratchvolume):
        self.afscratchvolume = afscratchvolume
        self.afscratchvolumeblock.set_k((self.afscratchvolume, ))

    def get_PI(self):
        return self.PI

    def set_PI(self, PI):
        self.PI = PI


def main(top_block_cls=Radio_Presidio_Prototype, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable real-time scheduling."

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
