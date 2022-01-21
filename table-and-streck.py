#  table-and-streck.py | to be placed in the package 'Turbin-languages'.

import sublime, sublime_plugin, datetime

class InstantCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      first_is_caret_sel = self.view.sel() # ⬷ a 'set' of regions (first,last) points.
      timestamp = datetime.datetime.now()
      text = timestamp.strftime("%Y-%m-%d %H:%M:%S ")
      self.view.insert(edit,first_is_caret_sel[0].begin(),text)


