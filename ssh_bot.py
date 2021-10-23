import optparse
import pexpect

def parser():

    # ssh -l [user] [host] -p [password]

    parser = optparse.OptionParser('%prog ' + '[host]')
    parser.add_option('-u','--user',dest='user',type='string', help='specify the user')
    parser.add_option('-p','--password',dest='password',type='string',help='specify password')
    parser.add_option('-c','--command',dest='command',type='string',help='specify the command')
    (options,args) = parser.parse_args()

    if(options.user == None):

        return parser.print_help()

    
    if(options.password == None):

        return parser.print_help()


    if(options.command == None):

        return parser.print_help()


    if( len(args) == 0 ):

        return parser.print_help()


    return {

        'user':options.user,
        'password':options.password,
        'command':options.command,
        'arg':args[0]
    }


PROMPT = ['\#','\>>>','\>','\$']

def connect(user,host,password):

    ssh_newkey = 'Are you sure you want to continue connecting'
    connection = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connection)
    ret = child.expect([pexpect.TIMEOUT,ssh_newkey,'[p|P]assword:'])

    if(ret == 0):

        print('failed to connect')
        return
    
    if(ret == 1):

        child.sendline('Yes')
        
        ret = child.expect([pexpect.TIMEOUT,'[pP]]assword:'])

        if(ret == 0):

            print('failed to connect')
            return
    

    child.sendline(password)
    child.expect(PROMPT)
    return child



def commands(child,command):

    child.expect(PROMPT)
    
    print(child.before)



def main():

    # prams = parser()

    # user = prams['user']
    # password = prams['password']
    # host = prams['arg']
    # command = prams['command']

    child = connect('kali','127.0.0.1','kali')

    commands(child,'pwd')
    


if __name__ == '__main__' :

    main()
