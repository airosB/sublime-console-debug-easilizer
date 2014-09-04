import sublime, sublime_plugin

class ConsoleDebugEasilizerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        scopeName = self.view.scope_name(self.view.sel()[0].begin())
        if ('source.php' in scopeName):
            source = 'php'
        elif ('source.coffee' in scopeName):
            source = 'coffee'
        else:
            source = 'js'

        self.view.run_command('insert_debug', {'arg': source})


class InsertDebug(sublime_plugin.TextCommand):
  def run(self, edit, arg):
    if (arg == 'php'):
        for region in self.view.sel():
            self.view.insert(edit, region.end(), ');')
            self.view.insert(edit, region.begin(), 'var_dump(' )

    elif (arg == 'coffee'):
        for region in self.view.sel():
            self.view.insert(edit, region.end(), ' ')
            self.view.insert(edit, region.begin(), 'console.log ' )

    else:
        for region in self.view.sel():
            self.view.insert(edit, region.end(), ');')
            self.view.insert(edit, region.begin(), 'console.log(' )

