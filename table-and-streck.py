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
            "currency", "'CURRENCY CREATED'", 
            Instant() + " CREATE CURRENCY ${1:USD} NAMED '${2:US Dollar}'",
            sublime.COMPLETION_FORMAT_SNIPPET, sublime.KIND_SNIPPET, 
            "Name a non-initialized currency and its shortform."
          ),
          sublime.CompletionItem(
            "exchange", "'EXCHANGE SET'", 
            Instant() + " EXCHANGE RATE ${1:1.40} ${2:USD} IS ${3:1.00} ${4:EUR}",
            sublime.COMPLETION_FORMAT_SNIPPET, sublime.KIND_SNIPPET, 
            "Update the relation between two currencies."
          ),
          sublime.CompletionItem(
            "entity", "'ENTITY CREATED'", 
            Instant() + " CREATE ENTITY ${1:identity} NAMED '${2:name}' TRADING IN ${3:USD} RESIDENT IN ${4:USA}",
            sublime.COMPLETION_FORMAT_SNIPPET, sublime.KIND_SNIPPET, 
            "Form a company."
          ),
          sublime.CompletionItem(
            "account", "'ACCOUNT CREATED'", 
            Instant() + " CREATE ACCOUNT ${1:A1920} WITH-ENTITY ${2:Company1} NAMED '${3:Kassa och bank}'",
            sublime.COMPLETION_FORMAT_SNIPPET, sublime.KIND_SNIPPET, 
            "Set-up a two-sided timeserie in a formed company set to '0.00, 0.00'."
          ),
          sublime.CompletionItem(
            "balance", "'ACCOUNT SET'", 
            Instant() + " SET ${1:A1920} IN ${2:Company1} TO ${3:123.00 + Normal(-32.00, 5.00)}, ${4:544.44 + Uniform(10.00, 50.00)}",
            sublime.COMPLETION_FORMAT_SNIPPET, sublime.KIND_SNIPPET, 
            "Set the value for a company key to a stochastic alternatively a "
            "deterministic two-sided figure."
          ),
          sublime.CompletionItem(
            "bookkeep", "'RECORDED'", 
            Instant() + " BOOKKEEP ${1:Company1} {\n"
            "  DEBET ${2:A1920} WITH ${3:10.00}\n"
            "  CREDIT ${4:A2641} WITH ${5:9.00}\n"
            "  CREDIT ${6:A2440} WITH ${7:1.00}\n"
            "} COMMENT '${8:Verificate 1}'",
            sublime.COMPLETION_FORMAT_SNIPPET, sublime.KIND_SNIPPET, 
            "Change to current state-of-affair in a set of timeseries."
          ),
          sublime.CompletionItem(
            "print", "'TEXT OUTPUT'",
            Instant() + " PRINT '${1:Hello world}'",
            sublime.COMPLETION_FORMAT_SNIPPET, sublime.KIND_SNIPPET, 
            "Output a text in your console."
          ),
          sublime.CompletionItem(
            "function", "'FUNCTION DEFINED'", 
            "FUNCTION ${1:name} ($2)\n{\n $0\n}", 
            sublime.COMPLETION_FORMAT_SNIPPET, sublime.KIND_SNIPPET, 
            "Include a function definition."
          ),
          sublime.CompletionItem(
            "schedule", "'NOTIFICATION'", 
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
            sublime.COMPLETION_FORMAT_SNIPPET, sublime.KIND_SNIPPET, 
            "Install a repetitious task such as changes in a set of timeseries."
          ),
       ], 0)

