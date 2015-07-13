#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

#sleep time
stime = 1

#add tanaka-word below
s = [
    u"あぁ〜",
    u"そっかそか",
    u"なるほど",
    u"確かに",
    u"マジっすか！",
    u"いやいやいや...",
    u"なんでやねん！",
    u"やかましいわ！",
    ]




try:
    while True:
	print '>',
        tmp = raw_input()
        if tmp == 'おつかれ':
            print u'お疲れ様です！'
            sys.exit(0)
        if tmp == '破門':
            print u'もうちょい待ってください・・・'
        print 'tnk>'+random.choice(s)
except KeyboardInterrupt:
    pass

