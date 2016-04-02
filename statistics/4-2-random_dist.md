[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> Its hard to gather much from the plot of the pdf, since their are so many data points and its all quite tight in terms of width, but the CDF shows something important. The cdf resembles a line of slope 1 running from the point (0,0) to (1,1) on the plot. This shows that as one goes from left to right on the distribution, the accumulation of values goes up at a constant rate which means that the distribution must be relatively uniform.

>> Code is below copied from chap04ex.ipynb in the code folder within the ThinkStats2 repository

```python
%matplotlib inline

import nsfg
import thinkstats2
import thinkplot

import random
t = [random.random() for _ in range(1000)]
pmf = thinkstats2.Pmf(t)
thinkplot.Pmf(pmf, linewidth=0.02, label='Random pdf')
thinkplot.Show()

cdf = thinkstats2.Cdf(t)
thinkplot.Cdf(cdf, label='Random cdf')
thinkplot.Show()

```