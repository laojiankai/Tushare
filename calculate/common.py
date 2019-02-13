#!/usr/bin/python
# -*- coding: UTF-8 -*-

import traceback

def getExpcetion(Exception, e):

    print 'str(Exception):\t', str(Exception)
    print 'str(e):\t\t', str(e)
    print 'repr(e):\t', repr(e)
    print 'e.message:\t', e.message
    print 'traceback.print_exc():';traceback.print_exc()
    print 'traceback.format_exc():\n%s' % traceback.format_exc()