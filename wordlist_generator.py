from itertools import permutations
import optparse

def parser():

    parser = optparse.OptionParser('%prog ' + '[word1,word2,word3 ...]')

    options_dir = [
    
    {'shortname':'-C','longname':'--capitalize','dest':'capital','action':'store_true','default':False, 'help':'capitalize all words in the wordlist'},
    {'shortname':'-F','longname':'--firstWordCapitalizer','dest':'firstWord' , 'action': 'store_true' , 'default':False, 'help':'capitalize only first word in the wordlist' },
    {'shortname':'-A','longname':'--WholeWordCapitalizer','dest':'wholeWord' , 'action': 'store_true' , 'default':False, 'help':'capitalize every letter in the wordlist' }


    ]
    
    for option in options_dir:

        parser.add_option(option['shortname'],option['longname'],dest=option['dest'],action=option['action'],default=option['default'],help=option['help'])


    (options,args) = parser.parse_args()

    return {'args':args,'options':options}



def generator(array):


    generated_array = []

    for i in range(1,len(array)+1):

        for perm in permutations(array,i):

            generated_array.append("".join(perm))
            
    return generated_array




def capitalizer(array):

    generated_array = []

    for word in array :

        generated_array.append( word.capitalize())
    

    return generated_array



def wholeWordCapitalizer(array):

    generated_array = []

    for word in array:

        generated_array.append(word.upper())


    return generated_array



def firstWordCapitalizer(word):

    return word.capitalize()

def main():



    items = parser()
    array_of_words = items['args'][0].split(",")
    print(items['options'].firstWord)


    if(items['options'].capital):

        array_of_words = capitalizer(array_of_words)
        

    
    if(items['options'].wholeWord):

        array_of_words = wholeWordCapitalizer(array_of_words)

    for word in generator(array_of_words):

        
        if(items['options'].firstWord):

            print(firstWordCapitalizer(word))
            
        
        if(not items['options'].firstWord):

            print(word)


if __name__ == '__main__':

    main()