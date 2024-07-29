# Bad solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        itr = head
        local = []
        while itr:
            if itr.next in local:
                return True
            else:
                local.append(itr.next)
                itr = itr.next
        return False

# Tortoise and the hare aproach. If there is a loop the hare will eventually land where the tortoise is 
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tortoise = head
        local = []
        while hare:
            try:
                hare = hare.next.next
                tortoise = tortoise.next
            except:
                break
            if hare == tortoise:
                return True           
        return False