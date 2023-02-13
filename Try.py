from pywinauto.application import Application
app = Application(backend="uia").connect(title_re=u".*Microsoft\u200b Edge", timeout=10)
app.window().set_focus()
