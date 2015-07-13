#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

#sleep time
stime = 1

#add tanaka-word below
s = []
s.append(u"あぁ〜")
s.append(u"そっかそか")
s.append(u"なるほど")
s.append(u"確かに")
s.append(u"マジっすか！")
s.append(u"いやいやいや...")

try:
    while True:
        print random.choice(s)
        time.sleep(stime)
except KeyboardInterrupt:
    pass

