""" File Converter wxPython App """

import wx
from PIL import Image
import os



class Panel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        
        # General initialisation --------------------------------
        
        self.choices = ['.png', '.jpg', '.webp', '.bmp', '.pdf']
        self.source_path = ''
        self.out_path = ''
        self.old_file_type = ''
        self.new_file_type = ''
        
        # GUI initialisation ------------------------------------
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        column_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Col 1 : 'Source:', left combobox, 'Output location'
        c1_sizer = wx.BoxSizer(wx.VERTICAL)
        label_source = wx.StaticText(self, label='Source:') 
        label_out = wx.StaticText(self, label='Output location:') 
        c1_sizer.Add(label_source, 0, wx.ALL|wx.ALIGN_LEFT, 5)
        c1_sizer.AddStretchSpacer()
        c1_sizer.Add(label_out, 0, wx.ALL|wx.ALIGN_LEFT, 5)
        
        # Col 2 : dynamic src text, 'to', dynamic output location text
        c2_sizer = wx.BoxSizer(wx.VERTICAL)
        self.dyn_label_source = wx.StaticText(self, label='')  

        type_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.left_cb = wx.ComboBox(self, size=(80,-1), 
                                   choices=self.choices)  
        label_to = wx.StaticText(self, label='to')        
        self.right_cb = wx.ComboBox(self, size=(80,-1), 
                                    choices=self.choices)   
        type_sizer.AddMany([(self.left_cb, 1, wx.ALL|wx.CENTRE, 5),
                            (label_to, 0, wx.ALL|wx.CENTRE, 5),
                            (self.right_cb, 1, wx.ALL|wx.CENTRE, 5)])
        
        self.dyn_label_out = wx.StaticText(self, label='')
        c2_sizer.AddMany([(self.dyn_label_source, 0, wx.ALL|wx.ALIGN_LEFT, 5),
                          (type_sizer, 0, wx.ALL|wx.CENTRE, 5),
                          (self.dyn_label_out, 0, wx.ALL|wx.ALIGN_RIGHT, 5)])
        
        # Col  3 : select button, right combobox, change button
        c3_sizer = wx.BoxSizer(wx.VERTICAL)
        self.select_button = wx.Button(self, label='Select')
        self.select_button.Bind(wx.EVT_BUTTON, self._on_select) 
        self.change_button = wx.Button(self, label='Change')
        self.change_button.Bind(wx.EVT_BUTTON, self._on_change)
        c3_sizer.Add(self.select_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        c3_sizer.AddStretchSpacer()
        c3_sizer.Add(self.change_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        
        # bottom : convert button, open output location button
        bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.convert_button = wx.Button(self, label='Convert')
        self.open_button = wx.Button(self, label='Open output location')
        self.convert_button.Bind(wx.EVT_BUTTON, self._on_convert)
        self.open_button.Bind(wx.EVT_BUTTON, self._on_open)
        bottom_sizer.AddMany([(self.convert_button, 0, wx.ALL|wx.EXPAND, 5),
                              (self.open_button, 0, wx.ALL|wx.EXPAND, 5)])
        
        # Top level sizing
        column_sizer.AddMany([(c1_sizer, 1, wx.ALL|wx.EXPAND, 5),
                              (c2_sizer, 1, wx.ALL|wx.EXPAND, 5),
                              (c3_sizer, 1, wx.ALL|wx.EXPAND, 5)])
        main_sizer.AddMany([(column_sizer, 0, wx.ALL|wx.EXPAND, 5),
                            (bottom_sizer, 0, wx.ALL|wx.CENTRE, 5)])
        self.SetSizer(main_sizer)
    
    
    def _on_select(self, event):
        print('select source button pressed')
        self.source_path = ''
        dlg = wx.FileDialog(self, 'Choose source file', self.source_path,
                            "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            self.source_path = os.path.join(dirname, filename)
        print('source path chosen:', self.source_path)


    def _on_change(self, event):
        print('change button pressed')


    def _on_convert(self, event):
        print('on convert button pressed')


    def _on_open(self, event):
        print('open output location button pressed')




class Frame(wx.Frame):
    def __init__(self, parent=None, size=(550,220), 
                 pos=(100,100), title='FileTypeConverter'):
        wx.Frame.__init__(self, parent=parent, size=size, pos=pos, title=title)
        Panel(self)
        self.SetAutoLayout(False)
        self.Show()


def main():
    app = wx.App(False)
    frame = Frame(None)
    app.MainLoop()

if __name__ == '__main__':
    main()