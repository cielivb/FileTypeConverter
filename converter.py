""" File Converter wxPython App """

import wx
import PIL
from pdf2image import convert_from_path
import os
import subprocess
import traceback


class Panel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
        
        # General initialisation --------------------------------
        
        self.choices = ['BMP', 'ICO', 'JPEG', 'PDF', 'PNG', 'TIFF', 'WEBP']
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
        
        # Main sizer layout        
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
        self.row2_sizer.Layout()


    def _get_outpath(self):
        """ Return out path to use """
        if self.out_path != '': # If outpath is specified by user
            return self.out_path
        elif self.source_path != '': # If outpath unspecified but source specified
            return os.path.dirname(self.source_path)
        return None # If both outpath and source paths are unspecified
    
    
    def _on_open_dir(self, event):
        """ Open file explorer at destination directory """
        outpath = self._get_outpath()
        if os.path.isdir(outpath):
            filebrowser_path = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
            subprocess.run([filebrowser_path, outpath])


    def _convert_pdf(self, dest_type, filename):
        """ Convert each pdf page into a separate image """
        # Create temp directory if not already present
        if not os.path.isdir(os.path.join(os.path.dirname(__file__), 'temp')):
            os.mkdir('temp')
        
        images = convert_from_path(self.source_path) # List of Pillow images
        
        name = os.path.basename(filename)
        name = name.split('.')[0] # e.g., filename.jpg -> filename
        for index, image in enumerate(images):
            
            # Add index to image filename
            pad_length = len(str(len(images)))
            padded_index = str(index).zfill(pad_length)
            temp_filename = name + '_' + padded_index + '.PNG'
            
            temp_path = os.path.join(os.path.dirname(__file__), 
                                     'temp', temp_filename)
            image.save(temp_path, format='PNG', lossless=True)
            self._convert(dest_type, filename, 
                          temp_path=temp_path, 
                          index=padded_index)


    def _convert(self, dest_type, filename, temp_path=None, index=None):
        """ Save copy of source file with user-specified extension """
        if temp_path is None:
            image = PIL.Image.open(self.source_path)
        else:
            image = PIL.Image.open(temp_path)
            filename = filename.split('.')[0] + '_' + index + '.' + dest_type
        
        # Use RGB for destination file types that do not support 
        # transparency, otherwise use RGBA.
        if dest_type == 'JPEG':
            # JPEG does not support transparency            
            if image.mode != 'RGB':
                image = image.convert('RGB')
        elif image.mode != 'RGBA': 
            image = image.convert('RGBA')

        if dest_type == 'BMP':
            # Use 32 bit BMP to preserve transparency where possible.
            # This purportedly works with BMP v4/v5 headers, and Pillow
            # handles this automatically, according to CoPilot...
            image.save(filename, format=dest_type, bits=32)
        else:
            image.save(filename, format=dest_type, lossless=True)
                
    
    def _on_convert(self, event):
        """ Setup and execute conversion, then report failure/success """
        if self.source_path != '':
            
            # Get source and destination types
            source_type = self.source_path.split(".")[-1].upper()
            dest_type = self.combobox.GetStringSelection()
            if dest_type == '': 
                return
            
            # Get new filename
            outdir = self._get_outpath()
            name = os.path.basename(self.source_path).split('.')[0]
            name = name + '.' + dest_type # Add extension
            filename = os.path.join(outdir, name)
           
            try: # Convert file
                if source_type == 'PDF':
                    # PDFs can contain multiple pages and therefore need
                    # a wrapper to process multiple images
                    self._convert_pdf(dest_type, filename)
                else:
                    self._convert(dest_type, filename)                    
                message = f'Converted {source_type} to {dest_type}'
                
            except Exception:
                traceback.print_exc()
                message = f'Failed to convert {source_type} to {dest_type}'
            finally:
                self.GetParent()._show_status_message(message)


class Frame(wx.Frame):
    def __init__(self, parent=None, size=(400,200), 
                 pos=(100,100), title='FileTypeConverter'):
        wx.Frame.__init__(self, parent=parent, size=size, pos=pos, title=title)
        
        # Set icon
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, 'assets', 'icon.ico')
        icon = wx.Icon(icon_path, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        
        # Status bar initialisation
        self.CreateStatusBar()
        self.SetStatusText('') 
        self.status_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._clear_status_message, self.status_timer)
        
        Panel(self)        
        
        self.SetAutoLayout(False)
        self.SetMinSize((400,200))
        self.Show()
    
    def _show_status_message(self, message):
        """ Display message in bottom left of status bar for 5 seconds """
        self.SetStatusText(message)
        self.status_timer.StartOnce(5000) # 5000ms = 5 seconds
    
    def _clear_status_message(self, event):
        """ Remove message from bottom left corner of status bar """
        self.SetStatusText('')


def main():
    app = wx.App(False)
    frame = Frame(None)
    app.MainLoop()

if __name__ == '__main__':
    main()