class Solution:
    def isValid(self, s: str) -> bool:
        pile = []

        opens = ["(", "{", "["]
        inverse = {
            ")": "(",
            "]": "[",
            "}": "{"
        }


        for i in s:
            if i in opens:
                pile.insert(0, i)
            else :
                if len(pile) > 0 and inverse[i] == pile[0]:
                    pile.pop(0)
                else : 
                    return False
                    
        return len(pile) == 0