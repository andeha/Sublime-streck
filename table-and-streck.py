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
     if not view.match_selector(locations[0], "source.streck"):
       return []
      
     completions = sublime.CompletionList(
       [
          sublime.CompletionItem(
            "currency", "'CURRENCY CREATED'",
            Instant() + "CREATE CURRENCY ${1:USD} NAMED '${2:US Dollar}'",
            sublime.COMPLETION_FORMAT_SNIPPET,
            (sublime.KIND_ID_SNIPPET, "A", "legal act"),
            "Name a <i>non-initialized</i> currency and its shortform."
          ),
          sublime.CompletionItem(
            "exchange", "'RATE OF EXCHANGE SET'",
            Instant() + "EXCHANGE RATE ${1:1.40} ${2:USD} IS ${3:1.00} ${4:EUR}",
            sublime.COMPLETION_FORMAT_SNIPPET,
            (sublime.KIND_ID_SNIPPET, "A", "legal act"),
            "Update a <i>two currencies</i> relation."
          ),
          sublime.CompletionItem(
            "entity", "'ENTITY RECOGNIZED'",
            Instant() + "CREATE ENTITY ${1:identity} NAMED '${2:name}' TRADING IN ${0:USD} RESIDENT IN ${3:USA}",
            sublime.COMPLETION_FORMAT_SNIPPET,
            (sublime.KIND_ID_SNIPPET, "A", "legal act"),
            "Form a company."
          ),
          sublime.CompletionItem(
            "account", "'ACCOUNT REGISTERED'", 
            Instant() + "CREATE ACCOUNT ${1:A1920} WITH-ENTITY ${2:Company1} NAMED '${0:Kassa och bank}'",
            sublime.COMPLETION_FORMAT_SNIPPET,
            (sublime.KIND_ID_SNIPPET, "A", "legal act"),
            "Set-up a two-sided <i>zero-inited</i> timeserie.</code>."
          ),
          sublime.CompletionItem(
            "balance", "'ACCOUNT INITIALIZED'", 
            Instant() + "SET ${1:A1920} IN ${2:Company1} TO ${3:123.00 + Normal(-32.00, 5.00)}, ${0:544.44 + Uniform(10.00, 50.00)}",
            sublime.COMPLETION_FORMAT_SNIPPET,
            (sublime.KIND_ID_SNIPPET, "A", "legal act"),
            "Set a key value to a <i>stoch.</i> alt. <i>deter.</i> figure-pair."
          ),
          sublime.CompletionItem(
            "bookkeep", "'TRANSACT RECODED'",
            Instant() + "BOOKKEEP ${1:Company1} {\n"
            "  DEBET ${2:A1920} WITH ${3:10.00}\n"
            "  CREDIT ${4:A2641} WITH ${5:9.00}\n"
            "  CREDIT ${6:A2440} WITH ${7:1.00}\n"
            "} COMMENT '${0:Verificate 1}'",
            sublime.COMPLETION_FORMAT_SNIPPET,
            (sublime.KIND_ID_SNIPPET, "A", "legal act"),
            "Change to current state-of-affair in a company."
          ),
          sublime.CompletionItem(
            "function", "'FUNCTION DEFINED'",
            "FUNCTION ${1:name} ($2)\n{\n $0\n}",
            sublime.COMPLETION_FORMAT_SNIPPET,
            (sublime.KIND_ID_SNIPPET, "A", "legal act"),
            "Include a function definition and its symbol name."
          ),
          sublime.CompletionItem(
            "print", "'COPY RELEASED'",
            Instant() + "PRINT '${1:Hello world}'",
            sublime.COMPLETION_FORMAT_SNIPPET,
            (sublime.KIND_ID_SNIPPET, "A", "legal act"),
            "Output a text in your console."
          ),
          sublime.CompletionItem(
            "schedule", "'NOTIFICATION ACTIVE'",
            Instant() + "CREATE SCHEDULE ${1:DaytimeWork}\n" 
            " STARTING ${2:2022-01-18} ${3:21:13:16}\n"
            " OCCURING ${4:BI-HOURLY}\n"
            " /* ENDING 2022-01-18 21:13:26 /*\n"
            "  {\n"
            "    ${0:VAR sales = 100.00 + Normal(100.00, 25.00)\n"
            "    VAR usdAmount = Convert(sales,EUR,USD)\n"
            "    BOOKKEEP Company1 {\n"
            "    DEBET A1920 WITH 10.00 + usdAmount\n"
            "      CREDIT Company1[VATOUT] WITH 9.00 + usdAmount\n"
            "      CREDIT A2440 WITH 1.00 + usdAmount\n"
            "    } COMMENT 'Verificate ' + INSTANCE}\n"
            "  }",
            sublime.COMPLETION_FORMAT_SNIPPET,
            (sublime.KIND_ID_SNIPPET, "A", "legal act"),
            "Install a repetitious task."
          ),
       ], 0)
     
     return completions

