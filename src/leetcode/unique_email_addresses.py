class Solution:
    name_terminated = { '@', '+' }
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = 0
        addresses = set()
        
        for email in emails:
            name = self._get_name(email)
            domain = self._get_domain(email)
            unique_email = name + domain

            if unique_email in addresses:
                continue
                
            addresses.add(unique_email)
            res += 1
        
        return res
    
    def _get_name(self, email) -> str:
        res = []
        i = 0
        
        while email[i] not in Solution.name_terminated:
            if email[i] is not '.':
                res.append(email[i])                
            i += 1
        
        return ''.join(res)
    
    def _get_domain(self, email) -> str:
        at_idx = email.find('@')
        return email[at_idx:]