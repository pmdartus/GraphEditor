from shapes.line import Line

SHAPE_COMMANDS = ("C", "R", "L", "PL", "OA")


def main():
    while True:
        cmd = raw_input()
        splitted_command = cmd.split(' ')

        try:
            element = Line(splitted_command[1:])
        except Exception, e:
            print 'ERR'
            print "#", e
        else:
            print 'OK'
            print "# New Element:", element

        if cmd == 'EXIT':
            exit(0)


if __name__ == '__main__':
    main()
