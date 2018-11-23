import main_exec
import wx

app = wx.App()
fenetre = wx.Frame(None, title="Multi-search")


def on_quit(event):
    fenetre.Close(True)


menu = wx.Menu()
quit_item = menu.Append(wx.ID_EXIT)
menuBar = wx.MenuBar()
menuBar.Append(menu, "&Fichier")
fenetre.SetMenuBar(menuBar)
fenetre.Bind(wx.EVT_MENU, on_quit, quit_item)
fenetre.Show()

app.MainLoop()
