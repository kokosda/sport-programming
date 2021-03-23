class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = dict()
        
        for cpd in cpdomains:
            count, subdomain = cpd.split(' ')
            count = int(count)
            parts = subdomain.split('.')
            prev_part = parts[-1]
            res[parts[-1]] = res.get(parts[-1], 0) + count

            for d in range(len(parts) - 2, -1, -1):
                cur_d = f'{parts[d]}.{prev_part}'
                res[cur_d] = res.get(cur_d, 0) + count
                prev_part = cur_d
                
        return [f'{res[k]} {k}' for k in res]