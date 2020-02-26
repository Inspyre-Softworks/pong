#!/usr/bin/env python3
from pathlib import Path
from os import chdir, getcwd


mycwd = Path(f'{getcwd()}')
conf  = Path(f'{mycwd}/lib/conf')
dev_key = Path(f'{conf}/dev.key')


