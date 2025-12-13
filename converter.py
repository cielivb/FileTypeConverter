""" File Converter wxPython App """

import wx
from PIL import Image



class Panel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Row 1 : 'Source:', dynamic dir label, select button
        r1_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Row 2 : combobox, arrow, combobox
        r2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Row 3 : 'Output location:', dynamic dir label, change button
        r3_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Row 4 : convert button, open output location button
        r4_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        main_sizer.AddMany([(r1_sizer, 0, wx.ALIGN_CENTRE, 5),
                            (r2_sizer, 0, wx.ALIGN_CENTRE, 5),
                            (r3_sizer, 0, wx.ALIGN_CENTRE, 5),
                            (r4_sizer, 0, wx.ALIGN_CENTRE, 5)])
        self.SetSizer(main_sizer)


class Frame(wx.Frame):
    def __init__(self, parent=None, size=(400,300), pos=(100,100)):
        wx.Frame.__init__(self, parent=parent, size=size, pos=pos)
        Panel(self)
        self.SetAutoLayout(False)
        self.Show()


def main():
    app = wx.App(False)
    frame = Frame(None)
    app.MainLoop()

if __name__ == '__main__':
    main()