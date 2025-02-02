import numpy as np
def stat(strg):
    
    def str_to_time(strg):
        ind_score = strg.split(',')
        in_seconds = []
        for each in ind_score : 
            time_stamp = each.split('|')
            in_seconds.append(int(time_stamp[0])*3600+int(time_stamp[1])*60+int(time_stamp[2]))
            
        return in_seconds    
            
    in_seconds = str_to_time(strg)
    average = sum(in_seconds)/len(in_seconds)
    median = np.median(in_seconds)
    maximum = max(in_seconds)
    minimum = min(in_seconds)
    range = maximum - minimum

    def time_to_str(time):
        hours = time//3600
        minutes = (time%3600)//60
        seconds = time%60
        return f'{hours:02}|{minutes:02}|{seconds:02}'
    
    return time_to_str(average), time_to_str(median),  time_to_str(range)

print (stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"))