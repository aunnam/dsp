# Hint:  use Google to find python function
import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
d1a = datetime.datetime(2013,1,2)
d2a = datetime.datetime(2015,7,28)
print (d2a-d1a).days

####b)  
date_start = '12312013'  
date_stop = '05282015'
d1b = datetime.datetime(2013,12,31)
d2b = datetime.datetime(2015,5,28)
print (d2b-d1b).days  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015' 
d1c = datetime.datetime(1994,1,15)
d2c = datetime.datetime(2015,7,14)
print (d2c-d1c).days 
