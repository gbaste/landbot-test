# Create here the DateUtils class with method split

class DateUtils:
    @staticmethod
    def split(date, separators):
        delim = list(separators[2::3])
        dates = []
        start = 0
        # loop character for delimiter
        for char in delim:
            end = date.find(char)
            if end < 0:
                end = len(date)
            if date[start:end] != '':
                dates.append(date[start:end])
            date = date[end + 1:]
        dates.append(date)
        if dates[-1] == '':
            del dates[-1]
        result = (dates, delim)
        return(result)
