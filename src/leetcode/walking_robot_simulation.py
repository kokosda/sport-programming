class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = 0
        y = 0
        alpha = 0
        obst = dict()
        x_alpha = { -270, -90, 90, 270 }
        pos_alpha = { -270, 0, 90 }
        res = 0
        
        for o in obstacles:
            if obst.get(o[0]) is None:
                obst[o[0]] = set()
                
            obst[o[0]].add(o[1])
            
        print(obst)
        
        for c in commands:
            if c == -1:
                alpha = (alpha + 90) % 360
            elif c == -2:
                alpha = (alpha - 90) % 360
            else:
                t = c
                sign = 1 if alpha in pos_alpha else -1
                
                if alpha in x_alpha:                    
                    while t > 0:
                        if obst.get(x + sign) is None or y not in obst[x + sign]:
                            x += sign
                        else:
                            break
                        t -= 1
                else:
                    while t > 0:
                        if obst.get(x) is None or (y + sign) not in obst[x]:
                            y += sign
                        else:
                            break
                        t -= 1
                        
                res = max(res, x * x + y * y)
                
            #print(x, y, alpha)
                        
        return res            
        
"""
[4,-1,3]
[]
[4,-1,4,-2,4]
[[2,4]]
"""