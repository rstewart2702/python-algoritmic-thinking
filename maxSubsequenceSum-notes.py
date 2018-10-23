"""
sc ::= sum<x : ic <= x <  jc : a[x]>

s  ::= sum<x : i  <= x <  j  : a[x]>
"""

"""
j = jc, right?

(sc + a[j] >= sc) -: sc,i,j,jc := sc + a[j] , i+1, j+1, jc+1;

(sc + a[j] <  sc) -: j, s := j+1, s + a[j];

"""
