class Characters(object):
    def name(self):
        print('1. Morrissey Wayout')
        print('2. Calven Helviett')
        print('3. Arthur J. Tullis')
        print('4. Don Jonas')
        who = input('> ')
        if who == '1':
            print('You chose Morrissey Wayout!')
            Introduction.expo('Morrissey', 'He like to fuck shit up')
        elif who == '2':
            print('You chose Calven Helviett!')
            name = 'Calven'
        elif who == '3':
            print('You chose Arthur J. Tullis!')
            name = 'Arthur'
        elif who == '4':
            print('You chose Don Jonas!')
            name = 'Don'
