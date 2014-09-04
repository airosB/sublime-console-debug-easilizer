sublime-console-debug-easilizer
===============================

**A SublimeText3 plugin**: Smarter shortcut for `console.log();` or `var_dump();` or something.

##Installation & Usage
1. Copy `ConsoleDebugEasilizer.py` to your SublimeText3's Packages directory.
1. Open *SublimeText3 > Preferences > Key Bindings - User*
1. Insert new line for the plugin. ex) `{ "keys": ["ctrl+shift+space"], "command": "console_debug_easilizer"},`
1. Select some string on any file and press the shortcut key you set above.
1. If your file is PHP, then you get `var_dump(SELECTED_STRING);`. Otherwise you get `console.log(SELECTED_STRING);`
