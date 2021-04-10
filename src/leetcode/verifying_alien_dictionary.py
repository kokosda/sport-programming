class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        a_ord = ord('a')
        orders = { order[i]: chr(a_ord + i) for i in range(len(order)) }
        conv_words = []
        
        for w in words:
            cw = []
            
            for ch in w:
                cw.append(orders[ch])
                
            conv_words.append(''.join(cw))

        sorted_words = sorted(conv_words)
        
        for i in range(len(conv_words)):
            if sorted_words[i] is not conv_words[i]:
                return False
            
        return True

"""
a
ap
app
apple
pp

apple
joe
app
  ^
"""