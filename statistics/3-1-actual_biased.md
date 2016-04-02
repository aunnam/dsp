[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> The means for actual distribution of number of childern under 18 in a household versus the biased survey of children regarding the number of children under 18 in a household is below.

>> actual pmf mean: 1.02420515504
>> biased pmf mean: 2.40367910066

>> This shows that children believe there are more children under 18 in a household than there actually are. In fact their estimate is over double the actual value.

>> code is below from ipython notebook chap03ex.ipynb in the code folder of ThinkStats2

```python
%matplotlib inline

import chap01soln
resp = chap01soln.ReadFemResp()

import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh)

import thinkplot
thinkplot.Pmf(pmf, label='numkdhh')
thinkplot.Show()

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf

biased = BiasPmf(pmf, label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()

print('actual pmf mean:', pmf.Mean())
print('biased pmf mean:', biased.Mean())
```