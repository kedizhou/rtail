# -*- encoding: utf8 -*-
# !/usr/bin/python
# This should be run on the computer you want to output the files
# You must pass a filename and a location
# filename must be the full path from the root directory, or relative path
# from the directory the server is running
# location must be in the form of http://location:port (i.e. http:localhost:8000)
# from http://115.28.181.12/en/questions/2c84b5155323dcc56a0e097dee3eddcab6a4f053eb5a560d182b73ddc76a7021/

import xmlrpclib, time, sys, os


def tail(filename, location):
    global over
    # connect to server
    s = xmlrpclib.ServerProxy(location)

    # get starting length of file
    curSeek = s.GetSize(filename)

    # constantly check
    while 1:
        time.sleep(1)  # make sure to sleep

        # get a new length of file and check for changes
        prevSeek = curSeek

        # some times it fails if the file is being writter to,
        # we'll wait another second for it to finish
        try:
            curSeek = s.GetSize(filename)
        except:
            pass

        # if file length has changed print it
        if prevSeek != curSeek:
            print s.tail(filename, prevSeek),
        # else:
        #     print filename.replace('/data/usr/tomcat', 'see log: ', 1)
        if over == 2:
            over = 0
            return 0
            # break
            # menu()


def stopctrl():
    import signal

    def signal_handler(signal, frame):
        print('bye!')
        # sys.exit(0)
        global over
        # 在日志输出界面按ctrl+c
        if over == 1:
            over = 2
            # main()
        # 在主菜单按ctrl+c
        else:
            raise NameError, ''

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTSTP, signal.SIG_IGN)
    # print('Press Ctrl+C')
    # signal.pause()


def menu():
    print '''
    1. a
    2. b
    3. exit
    '''


def main():
    global over
    # check that we got a file passed to us
    # if len(sys.argv) != 3 or not os.path.isfile(sys.argv[1]):
    # print 'Must give a valid filename.'
    # return
    # run tail function
    # tail(sys.argv[1], sys.argv[2])
    server = 'http://10.10.10.2:8000/'
    while 1:
        menu()
        try:
            i = raw_input('input:')
            if i == '3':
                raise NameError, ''
            elif i == '1':
                over = 1
                tail('/opt/a/logs/log.dat', server)
            elif i == '2':
                over = 1
                tail('/opt/b/logs/log.dat', server)
            else:
                continue
        except Exception, e:
            sys.exit(0)


over = 0
stopctrl()
main()