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
        
        #main_sizer = wx.BoxSizer(wx.VERTICAL)
        #column_sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        ## Col 1 : 'Source:', left combobox, 'Output location'
        #c1_sizer = wx.BoxSizer(wx.VERTICAL)
        #label_source = wx.StaticText(self, label='Source:') 
        #label_out = wx.StaticText(self, label='Output location:') 
        #c1_sizer.Add(label_source, 0, wx.ALL|wx.ALIGN_LEFT, 5)
        #c1_sizer.AddStretchSpacer(prop=2)
        #c1_sizer.Add(label_out, 0, wx.ALL|wx.ALIGN_LEFT, 5)
        
        ## Col 2 : dynamic src text, 'to', dynamic output location text
        #c2_sizer = wx.BoxSizer(wx.VERTICAL)
        #self.dyn_label_source = wx.StaticText(self, 
                                              #label='Choose file to convert')

        #type_sizer = wx.BoxSizer(wx.HORIZONTAL)
        #self.left_cb = wx.ComboBox(self, size=(80,-1), 
                                   #choices=self.choices)  
        #label_to = wx.StaticText(self, label='to')        
        #self.right_cb = wx.ComboBox(self, size=(80,-1), 
                                    #choices=self.choices)   
        #type_sizer.AddMany([(self.left_cb, 1, wx.ALL|wx.CENTRE, 5),
                            #(label_to, 0, wx.ALL|wx.CENTRE, 5),
                            #(self.right_cb, 1, wx.ALL|wx.CENTRE, 5)])
        
        #self.dyn_label_out = wx.StaticText(self, label='Same directory as input file')
        #c2_sizer.AddMany([(self.dyn_label_source, 0, 
                           #wx.ALL|wx.ALIGN_LEFT, 5),
                          #(type_sizer, 0, 
                           #wx.ALL|wx.CENTRE, 5),
                          #(self.dyn_label_out, 0, 
                           #wx.ALL|wx.ALIGN_LEFT, 5)])
        
        ## Col  3 : select button, right combobox, change button
        #c3_sizer = wx.BoxSizer(wx.VERTICAL)
        #self.select_button = wx.Button(self, label='Select')
        #self.select_button.Bind(wx.EVT_BUTTON, self._on_select) 
        #self.change_button = wx.Button(self, label='Change')
        #self.change_button.Bind(wx.EVT_BUTTON, self._on_change)
        #c3_sizer.Add(self.select_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        #c3_sizer.AddStretchSpacer()
        #c3_sizer.Add(self.change_button, 0, wx.ALL|wx.ALIGN_RIGHT, 5)
        
        ## bottom : convert button, open output location button
        #bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        #self.convert_button = wx.Button(self, label='Convert')
        #self.open_button = wx.Button(self, label='Open output location')
        #self.convert_button.Bind(wx.EVT_BUTTON, self._on_convert)
        #self.open_button.Bind(wx.EVT_BUTTON, self._on_open)
        #bottom_sizer.AddMany([(self.convert_button, 0, wx.ALL|wx.EXPAND, 5),
                              #(self.open_button, 0, wx.ALL|wx.EXPAND, 5)])
        
        ## Top level sizing
        #column_sizer.AddMany([(c1_sizer, 1, 
                               #wx.ALL|wx.EXPAND, 5),
                              #(c2_sizer, 1, 
                               #wx.ALL|wx.EXPAND, 5),
                              #(c3_sizer, 1, 
                               #wx.ALL|wx.EXPAND, 5)])
        #main_sizer.AddMany([(column_sizer, 0, wx.ALL|wx.EXPAND, 5),
                            #(bottom_sizer, 0, wx.ALL|wx.ALIGN_CENTRE, 5)])
        #self.SetSizer(main_sizer)
    
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Row 1 : 'File:', dynamic text, Choose button
        row1_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_label = wx.StaticText(self, label='File:')
        self.dyn_file_label = wx.StaticText(self, label='Choose file to convert')
        self.choose_file_button = wx.Button(self, label='Choose', id=1)
        row1_sizer.AddMany([(file_label, 1, wx.ALL|wx.CENTRE, 5),
                            (self.dyn_file_label, 6, wx.ALL|wx.CENTRE, 5),
                            (self.choose_file_button, 1, wx.ALL|wx.CENTRE, 5)])
        
        # Row 2 : 'Destination:', dynamic text, Choose button
        row2_sizer = wx.BoxSizer(wx.HORIZONTAL)
        dest_label = wx.StaticText(self, label='Destination:')
        self.dyn_dest_label = wx.StaticText(self, label='Same as file to convert')
        self.choose_dest_button = wx.Button(self, label='Choose', id=2)
        row2_sizer.AddMany([(dest_label, 1, wx.ALL|wx.CENTRE, 5),
                            (self.dyn_dest_label, 6, wx.ALL|wx.CENTRE, 5),
                            (self.choose_dest_button, 1, wx.ALL|wx.CENTRE, 5)])
        
        # Row 3 : To, combobox, Convert Button, Open Directory button
        row3_sizer = wx.BoxSizer(wx.HORIZONTAL)
        to_label = wx.StaticText(self, label='Convert to:')
        self.combobox = wx.ComboBox(self, size=(80,-1), choices=self.choices)
        self.convert_button = wx.Button(self, label='Convert', id=3)
        self.open_dir_button = wx.Button(self, label='Open Directory', id=4)
        row3_sizer.AddMany([(to_label, 0, wx.ALL|wx.CENTRE, 5),
                            (self.combobox, 0, wx.ALL|wx.CENTRE, 5),
                            (self.convert_button, 0, wx.ALL|wx.CENTRE, 5),
                            (self.open_dir_button, 0, wx.ALL|wx.CENTRE, 5)])
        
        # Top-level layout        
        main_sizer.AddMany([(row1_sizer, 1, wx.ALL|wx.EXPAND, 5),
                            (row2_sizer, 1, wx.ALL|wx.EXPAND, 5),
                            (row3_sizer, 1, wx.ALL|wx.ALIGN_CENTRE, 5)])
        self.SetSizer(main_sizer)
    
    
    def _on_select(self, event):
        """ Get and store path to source file """
        dlg = wx.FileDialog(self, 'Choose source file', self.source_path,
                            "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dirname = dlg.GetDirectory()
            self.source_path = os.path.join(dirname, filename)
        self.dyn_label_source.SetLabel(self.source_path)


    def _on_change(self, event):
        """ Get and store path to output directory """
        dlg = wx.DirDialog(self, 'Choose output directory', self.source_path,
                           wx.DD_DIR_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.out_path = dlg.GetPath()
        self.dyn_label_out.SetLabel(self.out_path)


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