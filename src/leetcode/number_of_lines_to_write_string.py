class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        a_code = ord('a')
        MAX_WIDTH = 100
        lines = 1
        last_line_width = 0
        
        for ch in s:
            ch_pos = ord(ch) - a_code
            
            if last_line_width + widths[ch_pos] <= MAX_WIDTH:
                last_line_width += widths[ch_pos]
            else:
                lines += 1
                last_line_width = widths[ch_pos]
                
        return [lines, last_line_width]