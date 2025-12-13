""" File Converter wxPython App """

import wx
from PIL import Image



class Panel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Row 1 : 'Source:', dynamic dir label, select button
        r1_sizer = wx.BoxSizer(wx.HORIZONTAL)
        label_source = wx.StaticText(self, label='Source:')
        self.dyn_label_source = wx.StaticText(self, label='')
        self.source_button = wx.Button(self, label='Select')
        self.source_button.Bind(wx.EVT_BUTTON, self._on_select)
        r1_sizer.AddMany([(label_source, 0, wx.ALL, 5),
                          (self.dyn_label_source, 0, wx.ALL, 5),
                          (self.source_button, 0, wx.ALL, 5)])
        
        # Row 2 : combobox, arrow, combobox
        r2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.choices = ['.png', '.jpg', '.webp', '.bmp', '.pdf']
        self.left_cb = wx.ComboBox(self, size=(80,-1), 
                                   choices=self.choices)
        label_to = wx.StaticText(self, label='to')
        self.right_cb = wx.ComboBox(self, size=(80,-1), 
                                    choices=self.choices)
        r2_sizer.AddMany([(self.left_cb, 0 , wx.ALL, 5),
                          (label_to, 0, wx.ALIGN_CENTRE|wx.ALL, 5),
                          (self.right_cb, 0, wx.ALL, 5)])
        
        # Row 3 : 'Output location:', dynamic dir label, change button
        r3_sizer = wx.BoxSizer(wx.HORIZONTAL)
        label_out = wx.StaticText(self, label='Output location:')
        self.dyn_label_out = wx.StaticText(self, label='')
        self.change_button = wx.Button(self, label='Change')
        self.change_button.Bind(wx.EVT_BUTTON, self._on_change)
        r3_sizer.AddMany([(label_out, 0, wx.ALL, 5),
                          (self.dyn_label_out, 0, wx.ALL, 5),
                          (self.change_button, 0, wx.ALL, 5)])        
        
        # Row 4 : convert button, open output location button
        r4_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.convert_button = wx.Button(self, label='Convert')
        self.open_button = wx.Button(self, label='Open output location')
        self.convert_button.Bind(wx.EVT_BUTTON, self._on_convert)
        self.open_button.Bind(wx.EVT_BUTTON, self._on_open)
        r4_sizer.AddMany([(self.convert_button, 0, wx.ALL, 5),
                          (self.open_button, 0, wx.ALL, 5)])
        
        # Top level sizing
        main_sizer.AddMany([(r1_sizer, 0, wx.ALIGN_CENTRE, 5),
                            (r2_sizer, 0, wx.ALIGN_CENTRE, 5),
                            (r3_sizer, 0, wx.ALIGN_CENTRE, 5),
                            (r4_sizer, 0, wx.ALIGN_CENTRE, 5)])
        self.SetSizer(main_sizer)
    
    
    def _on_select(self, event):
        print('select source button pressed')
    
    def _on_change(self, event):
        print('change button pressed')
    
    def _on_convert(self, event):
        print('on convert button pressed')
    
    def _on_open(self, event):
        print('open output location button pressed')


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