#  table-and-streck.py | for the package file 'Turbin-languages.sublime-package'.

import sublime, sublime_plugin, datetime

class InstantCommand(sublime_plugin.TextCommand):
   def run(self, edit):
     text = Instant()
     first_is_caret_sel = self.view.sel() # ⬷ a 'set' of regions (first,last) points.
     self.view.insert(edit,first_is_caret_sel[0].begin(),text)

def Instant():
   timestamp = datetime.datetime.now()
   return timestamp.strftime("%Y-%m-%d %H:%M:%S ")

class CompletionListener(sublime_plugin.EventListener):
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
            "func", "(FUNCTION DEFINED)", 
            "FUNCTION ${1:name} ($2)\n{\n $0\n}", 
            sublime.COMPLETION_FORMAT_SNIPPET, 
            sublime.KIND_SNIPPET
          ),
          sublime.CompletionItem(
            "caccount", "(ACCOUNT CREATED)", 
            Instant() + " CREATE ACCOUNT A1920 WITH-ENTITY Company1 NAMED 'Kassa och bank'\n",
            sublime.COMPLETION_FORMAT_SNIPPET,
            sublime.KIND_SNIPPET
          ),
          sublime.CompletionItem(
            "ccurrency", "(CURRENCY CREATED)", 
            Instant() + " CREATE CURRENCY USD NAMED 'US Dollar'\n",
            sublime.COMPLETION_FORMAT_SNIPPET,
            sublime.KIND_SNIPPET
          ),
          sublime.CompletionItem(
            "centity", "(ENTITY CREATED)", 
            Instant() + " CREATE ENTITY ${1:identity} NAMED '${2:name}' TRADING IN USD RESIDENT IN USA\n",
            sublime.COMPLETION_FORMAT_SNIPPET,
            sublime.KIND_SNIPPET
          ),
          sublime.CompletionItem(
            "bookkeep", "(RECORDED)", 
            Instant() + " BOOKKEEP Company1 {\n"
            "  DEBET A1920 WITH 10.00\n"
            "  CREDIT A2641 WITH 9.00\n"
            "  CREDIT A2440 WITH 1.00\n"
            "} COMMENT 'Verificate 1'\n",
            sublime.COMPLETION_FORMAT_SNIPPET,
            sublime.KIND_SNIPPET
          ),
          sublime.CompletionItem(
            "schedule", "(NOTIFICATION)", 
            Instant() + " CREATE SCHEDULE DaytimeWork\n" 
            " STARTING 2022-01-18 21:13:16\n"
            " OCCURING BI-HOURLY\n"
            " /* ENDING 2022-01-18 21:13:26 /*\n"
            "  {\n"
            "    VAR sales = 100.00 + Normal(100.00, 25.00)\n"
            "    VAR usdAmount = Convert(sales,EUR,USD)\n"
            "    BOOKKEEP Company1 {\n"
            "    DEBET A1920 WITH 10.00 + usdAmount\n"
            "      CREDIT Company1[VATOUT] WITH 9.00 + usdAmount\n"
            "      CREDIT A2440 WITH 1.00 + usdAmount\n"
            "    } COMMENT 'Verificate ' + INSTANCE\n"
            "  }",
            sublime.COMPLETION_FORMAT_SNIPPET,
            sublime.KIND_SNIPPET
          ),
       ], 0)
