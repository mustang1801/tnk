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
s = []
s.append(u"あぁ〜")
s.append(u"そっかそか")
s.append(u"なるほど")
s.append(u"確かに")
s.append(u"マジっすか！")
s.append(u"いやいやいや...")
s.append(u"なんでやねん！")
s.append(u"やかましいわ！")



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
        time.sleep(stime)
except KeyboardInterrupt:
    pass

