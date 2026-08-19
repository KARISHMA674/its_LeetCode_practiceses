class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        current_line = []
        current_letters = 0

        for word in words:
            
            if current_letters + len(current_line) + len(word) > maxWidth:
               
                total_spaces = maxWidth - current_letters
                num_gaps = len(current_line) - 1

                if num_gaps == 0:
                    
                    result.append(current_line[0] + ' ' * total_spaces)
                else:
                    
                    space_between = total_spaces // num_gaps
                    extra_spaces = total_spaces % num_gaps

                    line_str = ""
                    for i in range(num_gaps):
                        line_str += current_line[i]
                       
                        line_str += ' ' * (space_between + (1 if i < extra_spaces else 0))
                    line_str += current_line[-1]
                    result.append(line_str)

                current_line = []
                current_letters = 0

            current_line.append(word)
            current_letters += len(word)

        
        last_line_str = " ".join(current_line)
        last_line_str += ' ' * (maxWidth - len(last_line_str))
        result.append(last_line_str)

        return result
        