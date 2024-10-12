# Deobuscate https://freecodingtools.org/py-obfuscator

Its a shitty attemt at obuscation i often find in shitty malware / grayware etc.

So i made a tool to decode it.

install with
```
pip install git+https://github.com/admin-else/freedecodingtoolspy
```

Arguments:
- ``-o [[FILENAME]]`` outputfile if not given will be stout.
- ``-r`` replace file with deobuscated code.
- ``-R [[FOLDER]]`` Recurifly loop throught the folder, if not provided current folder, to find .py files check if they are obuscated and then the other args apply.
- ``-h --help`` Print a help text.
