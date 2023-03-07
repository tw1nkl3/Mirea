import random
def script(check, x, y):

    if check('level') == 1:
        if check('player', 23, y):
            if check('gold', x, y):
                return 'take'
            return 'down'
        else:
            if check('gold', x, y):
                return 'take'
            return 'right'
        
    elif check('level') == 2:
        if check('player', )
        
