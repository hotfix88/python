import datetime
import sublime_plugin
class AddInfowCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
                "contents":                 
                "<!""\n"
                " * Author:      fyso@163.com fengyangsgs@js.chinamobile.com""\n"
                " * DateTime:    "  "%s"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
                " * Description: Description""\n"
                ">"
            }
        )		