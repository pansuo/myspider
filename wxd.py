#!/bin/env python
import wx
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,"my frame",size=(300,300))
		panel = wx.Panel(self,-1)
		panel.Bind(wx.EVT_MOTION,self.OnMove)
		wx.StaticText(panel,-1,"Pos:",pos=(40,10))
		self.posCtrl = wx.TextCtrl(panel,-1,"",pos=(40,10))

	def OnMove(self,event):
		pos = event.GetPosition()
		self.posCtrl.SetValue("%s, %s" % (pos.x,pos.y))


if __name__ == '__main__':
#	app = wx.PySimpleApp()
#	frame = MyFrame()
#	frame.Show(True)
#	app.MainLoop()
	app = wx.PySimpleApp()
	frame = wx.Frame(None,-1,'')
	frame.SetToolTip(wx.ToolTip('this is a frame'))
	frame.SetCursor(wx.StockCursor(wx.CURSOR_MAGNIFIER))
	frame.SetPosition(wx.Point(0,0))
	frame.SetSize(wx.Size(300,300))
	frame.SetTitle('wxd.py')
	frame.Show()
	app.MainLoop()
