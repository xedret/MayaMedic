# MayaMedic
Automatic Autodesk / Maya virus check and removal

## Overview
After the recent infection with a virus that affects Autodesk's Maya Maya and its files, we ([Boxel Studio LLC](https://boxelstudio.com)), decided to create a small script that helps artists, programmers and other fellow members of the entertainment / animation industry to get rid of this virus.

Once you open an infected Maya scene that has it, every scene saved afterwards will be infected by it. It also saves 1 or 2 files in your scripts directory that makes it so the next time you open Maya, then it will be infecting every Maya scene as soon as you open it.

### Usage

First clone or download this repository, navigate to the project directory and execute the mayamedic.py file in the terminal:
```
$ python mayamedic.py
```

For unattended execution you may use the -s | --silent flag, this will execute the code without the prompts and just remove the malicious scripts:
```
$ python mayamedic.py --silent
```

If you want to directly scan files or directories without the prompts you can use -t | --target :
```
$ python mayamedic.py --target c:\path\to\file\or\directory\
```

If you just wish to test if your computer is infected without cleaning anything, you can run the -d | --dry flag:
```
$ python mayamedic.py --dry
```

Additional help is available through the --help flag:"
```
$ python mayamedic.py --help
```

The script will scan for malicious scripts, rename them (if any) so they become unusable and un-referenceable, and finally allow you to drag and drop .ma files for scanning and cleaning.

if the virus is found, a new clean file will be created in the same directory with the same name while the infected file will have the '_infected' suffix.

Credits
=======
  - Scripting
    * [Dexter Scott Belmont (Chief Information Security Officer @ Boxel Studio)](https://github.com/xedret)

  - Testing
    * Yiris Hallal (Head of Production @ Boxel Studio LLC)
    * [Benito Carbajal (Jr Developer @ Boxel Studio LLC)](https://github.com/bennycarbajal)
    