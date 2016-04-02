[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> Based on the code Percent of US Males between 5 10 and 6 1 is 34.2746837631 %. So about 34% of the US Male population would be eligibe to join the Blue Man Group.

>> Code is below copied from chap05ex.ipynb in the code folder within the ThinkStats2 repository

```python
from __future__ import print_function, division

import thinkstats2
import thinkplot

%matplotlib inline

import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

print('Percent of Males below 5 10:', 100*dist.cdf(177.8),'%') # 5' 10" = 177.8 cm
print('Percent of Males above 6 1:', 100*dist.cdf(185.42),'%') # 6' 1" = 185.42 cm
print('Percent of Males between 5 10 and 6 1:', 100*(dist.cdf(185.42)-dist.cdf(177.8)),'%')
```
