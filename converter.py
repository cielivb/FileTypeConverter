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
        
        # UI initialisation ------------------------------------
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Row 1 : 'File:', dynamic text, Choose button
        self.row1_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_label = wx.StaticText(self, label='File:')
        self.dyn_file_label = wx.StaticText(self, label='Choose file to convert',
                                            style=wx.ST_ELLIPSIZE_START|
                                            wx.ALIGN_RIGHT)
        self.choose_file_button = wx.Button(self, label='Choose')
        self.row1_sizer.AddMany([(file_label, 0, wx.ALL|wx.CENTRE, 5),
                                 (self.dyn_file_label, 1, wx.ALL|wx.CENTRE, 5),
                                 (self.choose_file_button, 0, wx.ALL|wx.CENTRE, 5)])
        
        # Row 2 : 'Destination:', dynamic text, Choose button
        self.row2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        dest_label = wx.StaticText(self, label='Destination:')
        self.dyn_dest_label = wx.StaticText(self, label='Same as file to convert',
                                            style=wx.ST_ELLIPSIZE_START|
                                            wx.ALIGN_RIGHT)
        self.choose_dest_button = wx.Button(self, label='Choose')
        self.row2_sizer.AddMany([(dest_label, 0, wx.ALL|wx.CENTRE, 5),
                                 (self.dyn_dest_label, 1, wx.ALL|wx.CENTRE, 5),
                                 (self.choose_dest_button, 0, wx.ALL|wx.CENTRE, 5)])
        
        # Row 3 : To, combobox, Convert Button, Open Directory button
        row3_sizer = wx.BoxSizer(wx.HORIZONTAL)
        to_label = wx.StaticText(self, label='Convert to:')
        self.combobox = wx.ComboBox(self, size=(80,-1), choices=self.choices)
        self.convert_button = wx.Button(self, label='Convert')
        self.open_dir_button = wx.Button(self, label='Open Directory')
        row3_sizer.AddMany([(to_label, 0, wx.ALL|wx.CENTRE, 5),
                            (self.combobox, 0, wx.ALL|wx.CENTRE, 5),
                            (self.convert_button, 0, wx.ALL|wx.CENTRE, 5),
                            (self.open_dir_button, 0, wx.ALL|wx.CENTRE, 5)])
        
        # Top-level layout        
        main_sizer.AddMany([(self.row1_sizer, 1, wx.ALL|wx.EXPAND, 5),
                            (self.row2_sizer, 1, wx.ALL|wx.EXPAND, 5),
                            (row3_sizer, 1, wx.ALL|wx.ALIGN_CENTRE, 5)])
        self.SetSizer(main_sizer)
        
        # Set Bindings --------------------------------------------
        
        self.choose_file_button.Bind(wx.EVT_BUTTON, self._on_choose_source)
        self.choose_dest_button.Bind(wx.EVT_BUTTON, self._on_choose_dest)
        self.convert_button.Bind(wx.EVT_BUTTON, self._on_convert)
        self.open_dir_button.Bind(wx.EVT_BUTTON, self._on_open_dir)
    
    
    def _on_choose_source(self, event):
        """ Get and store path to source file """
        dlg = wx.FileDialog(self, 'Choose source file', self.source_path,
                            "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            self.source_path = os.path.join(dirname, filename)
        self.dyn_file_label.SetLabel(self.source_path)
        self.row1_sizer.Layout()


    def _on_choose_dest(self, event):
        """ Get and store path to output directory """
        dlg = wx.DirDialog(self, 'Choose output directory', self.source_path,
                           wx.DD_DIR_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.out_path = dlg.GetPath()
        self.dyn_dest_label.SetLabel(self.out_path)


    def _on_convert(self, event):
        print('on convert button pressed')


    def _on_open_dir(self, event):
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