class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        tmp_k = k
        dq_num = deque(num)
        k_num = deque()
        
        while tmp_k > 0:
            digit = tmp_k % 10
            tmp_k //= 10
            k_num.appendleft(digit)
            
        Solution._pad_with_zeroes(len(k_num), len(dq_num), appendFn=k_num.appendleft)
        Solution._pad_with_zeroes(len(dq_num), len(k_num), appendFn=dq_num.appendleft)
            
        remainder = 0
        i = len(dq_num) - 1
        
        while i >= 0:
            s = dq_num[i] + k_num[i] + remainder            
            dq_num[i] = s % 10
            remainder = s // 10
            i -= 1
            
        if remainder > 0:
            dq_num.appendleft(remainder)
            
        return dq_num
        
    def _pad_with_zeroes(cur_len, desired_len, appendFn):
        while cur_len < desired_len:
            appendFn(0)
            cur_len += 1