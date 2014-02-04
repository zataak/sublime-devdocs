# Written by Vitor Britto (code@vitorbritto.com.br / vitorbritto.com.br)
# based on Stackoverflow Search Plugin by Eric Martel (emartel@gmail.com / www.ericmartel.com)

import sublime
import sublime_plugin

import subprocess
import webbrowser

from os.path import basename
from os.path import splitext

def GetLanguageFromView(view):
    language = splitext(basename(view.settings().get('syntax')))[0]
    return language if ' ' not in language else ""

def SearchFor(text):
    url = 'http://devdocs.io/#q=' + text.replace(' ', '%20')
    webbrowser.open_new_tab(url)


class DevDocsSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        for selection in self.view.sel():
            
            # if the user didn't select anything, search the word under curson
            if selection.empty():
                selection = self.view.word(selection)
                
            text = self.view.substr(selection)
            text = GetLanguageFromView(self.view) + ' ' + text
            SearchFor(text)


class DevDocsSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search DevDocs for', '',
            self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
        input = GetLanguageFromView(self.window.active_view()) + ' ' + input
        SearchFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass