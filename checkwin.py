
class CheckWin():
    def __init__(self):
        pass

    def win_check(self, A, B, C, D, E, F, G, H, I):
        if C == 'X' and F == 'X' and I == 'X':
            return True
        elif B == 'X' and E == 'X' and H == 'X':
            return True
        elif A == 'X' and D == 'X' and G == 'X':
            return True
        elif A == 'X' and B == 'X' and C == 'X':
            return True
        elif D == 'X' and E == 'X' and F == 'X':
            return True
        elif G == 'X' and H == 'X' and I == 'X':
            return True
        elif A == 'X' and E == 'X' and I == 'X':
            return True
        elif C == 'X' and E == 'X' and G == 'X':
            return True

        elif C == 'O' and F == 'O' and I == 'O':
            return True
        elif B == 'O' and E == 'O' and H == 'O':
            return True
        elif A == 'O' and D == 'O' and G == 'O':
            return True
        elif A == 'O' and B == 'O' and C == 'O':
            return True
        elif D == 'O' and E == 'O' and F == 'O':
            return True
        elif G == 'O' and H == 'O' and I == 'O':
            return True
        elif A == 'O' and E == 'O' and I == 'O':
            return True
        elif C == 'O' and E == 'O' and G == 'O':
            return True