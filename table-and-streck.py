#  table-and-streck.py | for the package file 'Turbin-languages.sublime-package'.

import sublime, sublime_plugin, datetime

def Instant():
   timestamp = datetime.datetime.now()
   return timestamp.strftime("%Y-%m-%d %H:%M:%S ")

class InstantCommand(sublime_plugin.TextCommand):
   def run(self, edit):
     text = Instant()
     first_is_caret_sel = self.view.sel() # ⬷ a 'set' of regions (first,last) points.
     self.view.insert(edit,first_is_caret_sel[0].begin(),text)

class TurbinCompletionsEventListener(sublime_plugin.EventListener):
   def on_query_completions(self, view, prefix, locations):
     return sublime.CompletionList(
       [
          sublime.CompletionItem(
            "exchg", "(EXCHANGE SET)", 
            Instant() + " EXCHANGE RATE 1.40 USD IS 1.00 EUR\n",
            sublime.COMPLETION_FORMAT_SNIPPET, 
            sublime.KIND_SNIPPET
          ),
          sublime.CompletionItem(
            "account", "(ACCOUNT SET)", 
            Instant() + " SET A1920 IN Company1 TO 123.00 + Normal(-32.00, 5.00), 544.44 + Uniform(10.00, 50.00)\n",
            sublime.COMPLETION_FORMAT_SNIPPET, 
            sublime.KIND_SNIPPET
          ),
          sublime.CompletionItem(
            "func", 
            annotation="(FUNCTION DEFINED)", 
            completion="FUNCTION ${1:name} ($2)\n{\n $0\n}", 
            completion_format=sublime.COMPLETION_FORMAT_SNIPPET, 
            kind=sublime.KIND_SNIPPET
          ),
       ], 0)


