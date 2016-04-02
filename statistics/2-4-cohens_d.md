[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The Cohen's d of weights between first babies and other babies within the data set is about -0.0887 . The negative sign indicates that on average first babies are lighter than other babies, but the 0.0887 difference in standard deviations is quite miniscule.

>> The Cohen's d of pregnancy lengths between first babies and other babies within the data set is about 0.0289 . The positive sign indicates that on average first babies had a longer pregnancy length than other babies, but the 0.0289 difference in standard deviations is quite miniscule just like Cohen's d for weights.

>> All the code is below and is in the file 2-4-cohens_d.py within the code folder of the ThinkStats2 repository

```python
import thinkstats2
import nsfg

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome==1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

print('Cohen diff Weight', thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb))
print('Cohen diff PregLength', thinkstats2.CohenEffectSize(firsts.prglngth, others.prglngth))

# Output: 
# Cohen diff Weight -0.08867292707260176
# Cohen diff PregLength 0.028879044654449834
```
