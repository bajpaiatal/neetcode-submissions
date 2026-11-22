class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m>n:
            return False
        
        freq1 = [0]*26
        freq2 = [0]*26
        matches = 26
        for i in range(m):
            idx1 = ord(s1[i])-ord('a')
            idx2 = ord(s2[i])-ord('a')
            if freq1[idx1]==freq2[idx1]:
                matches -= 1
            freq1[idx1] += 1
            if freq1[idx1]==freq2[idx1]:
                matches += 1
            
            if freq1[idx2]==freq2[idx2]:
                matches -= 1
            freq2[idx2] += 1
            if freq1[idx2]==freq2[idx2]:
                matches += 1
        if matches==26:
            return True
        # print(matches)

        left, right = 0, m        
        while right<n:
            idx1 = ord(s2[left])-ord('a')
            if freq1[idx1]==freq2[idx1]:
                matches -= 1
            freq2[idx1] -= 1
            if freq1[idx1]==freq2[idx1]:
                matches += 1
            left += 1
            
            idx2 = ord(s2[right])-ord('a')
            if freq1[idx2]==freq2[idx2]:
                matches -= 1
            freq2[idx2] += 1
            if freq1[idx2]==freq2[idx2]:
                matches += 1
            right += 1
            if matches==26:
                return True
            # print(matches)
        return False