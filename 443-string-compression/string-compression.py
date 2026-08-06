class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            char = chars[read]
            read_next = read
            
            while read_next < n and chars[read_next] == char:
                read_next += 1
                
            count = read_next - read
            
            chars[write] = char
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                    
            read = read_next
            
        return write
        