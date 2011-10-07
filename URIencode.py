# encoding: utf-8
import sublime_plugin
class UrlQuoteSelection(sublime_plugin.TextCommand):
    def run(self, edit):
        from urllib import quote_plus
        for selection in reversed(self.view.sel()):
            self.view.replace(edit, selection, quote_plus(self.view.substr(selection).encode("utf-8")))
