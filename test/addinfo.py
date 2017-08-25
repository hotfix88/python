
import datetime
import sublime_plugin
class AddInfoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents": 
                "#!/usr/bin/env python\n"
                "# -*- coding: utf-8 -*-\n"
                "\"\"\"\n"
                " Author:      fyso""\n"
                " DateTime:    "  "%s"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
                " Description: Description""\n"
                "\"\"\"\n"
            }
        )		
