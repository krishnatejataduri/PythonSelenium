import wx
from wx import Font
from wx._core import FontStyle


class DebugUtil(wx.Frame):

    def __init__(self, parent,test_name,screen_name, object_or_func_name,action,error_details):
        self.selected_option = 'Retry'
        wx.Frame.__init__(self, parent, size=[500, 300])
        self.IsShownOnScreen()
        self.SetTitle(f"Error! - {test_name}")
        self.CenterOnScreen()
        self.EnableCloseButton(enable=False)
        self.SetBackgroundColour("#E6E6FA")
        panel = wx.Panel(self)

        self.screen = wx.StaticText(panel, label=f"Screen:", pos=(20, 30))
        self.screen.SetFont(Font().Bold())
        wx.StaticText(panel, label=f"{screen_name}", pos=(70, 30))

        self.object = wx.StaticText(panel, label=f"Object/Function:", pos=(20, 60))
        self.object.SetFont(Font().Bold())
        wx.StaticText(panel, label=f"{object_or_func_name}", pos=(115, 60))

        self.action = wx.StaticText(panel, label=f"Action:", pos=(20, 90))
        self.action.SetFont(Font().Bold())
        wx.StaticText(panel, label=f"{action}", pos=(65, 90))

        self.error = wx.StaticText(panel, label=f"Error Details:", pos=(20, 120))
        self.error.SetFont(Font().Bold())
        self.error_msg = wx.StaticText(panel, label=f"{error_details}", pos=(20, 140))
        self.error_msg.Wrap(450)

        RetryButton = wx.Button(panel, wx.ID_RETRY, "Retry", pos=(80, 200))
        RetryButton.SetBackgroundColour("#9ACD32")
        self.Bind(wx.EVT_BUTTON, self.OnRetry,RetryButton)

        IgnoreButton = wx.Button(panel, wx.ID_IGNORE, "Ignore", pos=(200, 200))
        IgnoreButton.SetBackgroundColour("#FF8C00")
        self.Bind(wx.EVT_BUTTON, self.OnIgnore,IgnoreButton)

        AbortButton = wx.Button(panel, wx.ID_ABORT, "Abort", pos=(320, 200))
        AbortButton.SetBackgroundColour("#FA8072")
        self.Bind(wx.EVT_BUTTON, self.OnAbort,AbortButton)

        self.Show()

    def OnRetry(self, arg2):
        self.Close()


    def OnAbort(self, arg2):
        self.selected_option = "Abort"
        self.Close()

    def OnIgnore(self, arg2):
        self.selected_option = "Ignore"
        self.Close()

def show_message(test_name,screen_name,object_or_func_name,action,error_details):
    app = wx.App(False)
    debug = DebugUtil(None,test_name,screen_name,object_or_func_name,action,error_details)
    app.MainLoop()
    return debug.selected_option

#show_message('afsfsdf','ckasdsdfmsdf','daskfmsfpoas','ejeprogemsfkl')