# Created by wofeiwo <wofeiwo#gmail.com> on 2011-09-07.
import sublime, sublime_plugin
import codecs

# Add "convert_coder_list" list in user settings,
# Or you can just modify your own charsets here.
DEFAULT_CODER = ["gb18030", "gbk", "gb2312", "big5", "utf-8", "utf-16le"]

class ConvertToUtf8Command(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view

        if view.is_loading():
            sublime.status_message("Waiting to loading.")
            return False
        
        coders = view.settings().get("convert_coder_list", DEFAULT_CODER)

        text = ""

        # Try to convert every coder in the list.
        for coder in coders:
                try:
                    theFile = codecs.open(view.file_name(),"r",coder)
                    text = theFile.read()
                    if len(text) != 0:
                        break
                except:
                    continue        
        
        # Replace all file content with new encoding data.
        view.run_command("select_all")
        view.replace(edit, view.sel()[0], text)

        # Reset cursor position.
        view.sel().clear()
        view.sel().add(sublime.Region(0))

    def is_enabled(self):
        return self.view.file_name() and len(self.view.file_name()) > 0