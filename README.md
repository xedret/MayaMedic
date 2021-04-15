# MayaMedic
Automatic Autodesk / Maya virus check and removal

## Overview

After the recent infection with a virus that affects maya and its files, we (Boxel Studio LLC), decided to create a small script that helps artists, programmers and other fellow members of the entertainment / animation industry to get rid of this virus.

Once you open an infected Maya scene that has it, every scene saved afterwards will be infected by it. It also saves 1 or 2 files in your scripts directory that makes it so the next time you open Maya, then it will be infecting every Maya scene as soon as you open it.

### Usage

First clone or download this repository, navigate to the project directory and execute the mayamedic.py file in the terminal:
```
$ python mayamedic.py
```

The script will scan for malicious scripts, rename them (if any) so they become unusable and un-referenceable, and finally allow you to drag and drop .ma files for scanning and cleaning, if the virus is found, a new clean file will be created in the same directory with the 'clean' suffix.

Credits
=======
  - Scripting
    * [Dexter Scott Belmont](https://github.com/xedret)

  - Testing
    * Yiris Hallal (Head of Production @ Boxel Studio LLC)
    * [Benito Carbajal (Jr Developer @ Boxel Studio LLC)](https://github.com/bennycarbajal)
    * [Luis Bautista (Full-Stack Developer @ Boxel Studio LLC)](https://github.com/d0tb0x)