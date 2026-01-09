from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #On sort le nombre équivalent à notre liste de node
        resl1 = int(self.recursive(l1))
        resl2 = int(self.recursive(l2))

        #On additionne les deux nombres et on inverse la liste
        res = list(str(resl1 + resl2))[::-1]

        #On reconstruit la liste node en sortie avec la somme
        return self.construct(res)
    
    def construct(self, l):
        if len(l) == 1:
            return ListNode(int(l[0]))

        current = l.pop(0)
        return ListNode(int(current), self.construct(l))

    def recursive(self, l):
        if l.next == None:
            return l.val
        return str(self.recursive(l.next)) + str(l.val)