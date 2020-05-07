#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: RPi4 FM S RDS
# Generated: Thu May  7 13:07:24 2020
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

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import rds
import time
import wx


class RPi4_FM_S_RDS(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="RPi4 FM S RDS")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.sampleOut = sampleOut = 30000
        self.quadrature = quadrature = samp_rate/10
        self.frekvenca = frekvenca = 106900000

        ##################################################
        # Blocks
        ##################################################
        self.nbook = self.nbook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nbook.AddPage(grc_wxgui.Panel(self.nbook), "Vhodni Spekter")
        self.nbook.AddPage(grc_wxgui.Panel(self.nbook), "MPX spekter")
        self.nbook.AddPage(grc_wxgui.Panel(self.nbook), "MPX slap")
        self.nbook.AddPage(grc_wxgui.Panel(self.nbook), "L+R")
        self.nbook.AddPage(grc_wxgui.Panel(self.nbook), "L-R")
        self.nbook.AddPage(grc_wxgui.Panel(self.nbook), "RDS spekter")
        self.nbook.AddPage(grc_wxgui.Panel(self.nbook), "RDS scope")
        self.Add(self.nbook)
        _frekvenca_sizer = wx.BoxSizer(wx.VERTICAL)
        self._frekvenca_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_frekvenca_sizer,
        	value=self.frekvenca,
        	callback=self.set_frekvenca,
        	label='Frekvenca',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._frekvenca_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_frekvenca_sizer,
        	value=self.frekvenca,
        	callback=self.set_frekvenca,
        	minimum=80000000,
        	maximum=110000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_frekvenca_sizer)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_f(
        	self.nbook.GetPage(2).GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=1.0,
        	sample_rate=140000,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Waterfall Plot',
        )
        self.nbook.GetPage(2).Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_c(
        	self.nbook.GetPage(6).GetWin(),
        	title='Scope Plot',
        	sample_rate=2375 * 4,
        	v_scale=0.0004,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=True,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.nbook.GetPage(6).Add(self.wxgui_scopesink2_1.win)
        self.wxgui_fftsink2_3 = fftsink2.fft_sink_c(
        	self.nbook.GetPage(5).GetWin(),
        	baseband_freq=57000,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=-70,
        	ref_scale=2.0,
        	sample_rate=19000,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=0.1333,
        	title='FFT Plot',
        	peak_hold=False,
        )
        self.nbook.GetPage(5).Add(self.wxgui_fftsink2_3.win)
        self.wxgui_fftsink2_2 = fftsink2.fft_sink_c(
        	self.nbook.GetPage(0).GetWin(),
        	baseband_freq=frekvenca,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.1333,
        	title='SDR sprejem',
        	peak_hold=False,
        )
        self.nbook.GetPage(0).Add(self.wxgui_fftsink2_2.win)
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_f(
        	self.nbook.GetPage(3).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=sampleOut,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.1333,
        	title='L+R',
        	peak_hold=False,
        )
        self.nbook.GetPage(3).Add(self.wxgui_fftsink2_1.win)
        self.wxgui_fftsink2_0_0_0_1 = fftsink2.fft_sink_f(
        	self.nbook.GetPage(4).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=30000,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.1333,
        	title='L-R',
        	peak_hold=False,
        )
        self.nbook.GetPage(4).Add(self.wxgui_fftsink2_0_0_0_1.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.nbook.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=140000,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.1333,
        	title='MPX spectrum',
        	peak_hold=False,
        	win=window.hamming,
        )
        self.nbook.GetPage(1).Add(self.wxgui_fftsink2_0.win)
        self.root_raised_cosine_filter_0 = filter.fir_filter_ccf(2, firdes.root_raised_cosine(
        	1, 19000, 2375, .35, 100))
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=140,
                decimation=280,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=sampleOut/1000,
                decimation=40,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=sampleOut/1000,
                decimation=int(quadrature/1000),
                taps=None,
                fractional_bw=None,
        )
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  19000/quadrature,
                  taps=None,
        	  flt_size=32)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(0)

        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(frekvenca, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(2, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.low_pass_filter_0 = filter.fir_filter_ccf(10, firdes.low_pass(
        	1, samp_rate, 75000, 25000, firdes.WIN_HAMMING, 6.76))
        self.gr_rds_parser_0 = rds.parser(True, False, 0)
        self.gr_rds_panel_0 = rds.rdsPanel(frekvenca, self.GetWin())
        self.Add(self.gr_rds_panel_0.panel)
        self.gr_rds_decoder_0 = rds.decoder(False, False)
        self.freq_xlating_fir_filter_xxx_2 = filter.freq_xlating_fir_filter_fcf(5, (firdes.low_pass(1.0,200000,13e3,3e3,firdes.WIN_HAMMING)), 38000, 200000)
        self.digital_psk_demod_0 = digital.psk.psk_demod(
          constellation_points=2,
          differential=False,
          samples_per_symbol=4,
          excess_bw=0.35,
          phase_bw=6.28/100.0,
          timing_bw=6.28/100.0,
          mod_code="gray",
          verbose=False,
          log=False,
          )
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_char*1, 2)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_sink_0 = audio.sink(sampleOut, 'hw:0,0', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=quadrature,
        	audio_decimation=1,
        )
        self.analog_fm_deemph_0_0_0 = analog.fm_deemph(fs=sampleOut, tau=75e-6)
        self.analog_fm_deemph_0_0 = analog.fm_deemph(fs=sampleOut, tau=75e-6)
        self.aa = filter.freq_xlating_fir_filter_fcc(1, (filter.firdes.low_pass_2(1, samp_rate/10, 2000, 500, 60) ), 57000, quadrature)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.gr_rds_decoder_0, 'out'), (self.gr_rds_parser_0, 'in'))
        self.msg_connect((self.gr_rds_parser_0, 'out'), (self.gr_rds_panel_0, 'in'))
        self.connect((self.aa, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.analog_fm_deemph_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.analog_fm_deemph_0_0_0, 0), (self.audio_sink_0, 1))
        self.connect((self.analog_wfm_rcv_0, 0), (self.aa, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.freq_xlating_fir_filter_xxx_2, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.analog_fm_deemph_0_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_keep_one_in_n_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.analog_fm_deemph_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.gr_rds_decoder_0, 0))
        self.connect((self.digital_psk_demod_0, 0), (self.blocks_keep_one_in_n_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_2, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_2, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.wxgui_fftsink2_3, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.wxgui_fftsink2_1, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.wxgui_fftsink2_0_0_0_1, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.wxgui_waterfallsink2_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.digital_psk_demod_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.wxgui_scopesink2_1, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_quadrature(self.samp_rate/10)
        self.wxgui_fftsink2_2.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 75000, 25000, firdes.WIN_HAMMING, 6.76))
        self.aa.set_taps((filter.firdes.low_pass_2(1, self.samp_rate/10, 2000, 500, 60) ))

    def get_sampleOut(self):
        return self.sampleOut

    def set_sampleOut(self, sampleOut):
        self.sampleOut = sampleOut
        self.wxgui_fftsink2_1.set_sample_rate(self.sampleOut)

    def get_quadrature(self):
        return self.quadrature

    def set_quadrature(self, quadrature):
        self.quadrature = quadrature
        self.pfb_arb_resampler_xxx_0.set_rate(19000/self.quadrature)

    def get_frekvenca(self):
        return self.frekvenca

    def set_frekvenca(self, frekvenca):
        self.frekvenca = frekvenca
        self._frekvenca_slider.set_value(self.frekvenca)
        self._frekvenca_text_box.set_value(self.frekvenca)
        self.wxgui_fftsink2_2.set_baseband_freq(self.frekvenca)
        self.osmosdr_source_0.set_center_freq(self.frekvenca, 0)
        self.gr_rds_panel_0.set_frequency(self.frekvenca);


def main(top_block_cls=RPi4_FM_S_RDS, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
