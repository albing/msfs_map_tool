import webbrowser
import wx
from SimConnect import *


class HelloFrame(wx.Frame):

    def __init__(self, *args, **kw):
        super(HelloFrame, self).__init__(*args, **kw)
        pnl = wx.Panel(self)
        bt = wx.Button(pnl, label='Where the heck am I?')
        bt.Bind(wx.EVT_BUTTON, self.get_it)
        self.CreateStatusBar()
        self.SetStatusText("Welcome to wxPython!")


    def get_it(self, *args, **kwargs):
        try:
            sm = SimConnect()
        except ConnectionError:
            self.SetStatusText("Pretty sure flight sim is closed")
            return
        if not sm:
            self.SetStatusText("Pretty sure flight sim is closed")
            return

        aq = AircraftRequests(sm, _time=500)
        latlng = (aq.get("PLANE_LATITUDE"), aq.get("PLANE_LONGITUDE"))
        if int(latlng[0] * 10) == 0 and int(latlng[0] * 10) == 0:
            self.SetStatusText("Pretty sure you're not flying right now")
            return
        webbrowser.open(f'https://www.google.com/maps/?q={latlng}')
        self.SetStatusText(latlng)


    def OnExit(self, event):
        self.Close(True)


if __name__ == '__main__':
    app = wx.App()
    frm = HelloFrame(None, title='Where the heck am I?')
    frm.Show()
    app.MainLoop()
