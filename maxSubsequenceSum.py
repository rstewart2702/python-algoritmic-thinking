# Given array a[0..N-1] of integer values,
# find the i <= j s.t. sum(x : i<=x<=j : a[x]) is maximum.

# Initial thought is that we could look for possible sums
# of different lengths:
#  1   N         (0,N-1)
#  2   N-1       (0,N-2) (1,N-1)
#  3   N-2       (0,N-3) (1,N-2) (2,N-1)
#  4   N-3       (0,N-4) (1,N-3) (2,N-2) (3,N-1)
#  5   N-4       (0,N-5) (1,N-4) (2,N-3) (3,N-2) (4,N-1)
#  6   N-5       (0,N-6) (1,N-5) (2,N-4) (3,N-3) (4,N-2) (5,N-1)
#  7   N-6       (0,N-7) (1,N-6) (2,N-5) (3,N-4) (4,N-3) (5,N-2) (6,N-1)
# and so on...
#
# ...down to:
# N-3  N-(N-3)=3 (0,2)   (1,3)   (2,4)   ... ... ... ... ... ... ..(N-4,N-1) (N-3,N-1)
# N-1  N-(N-2)=2 (0,1)   (1,2)   ... ... ... ... ... ... ... ... ... ... ... ... ...   (N-2,N-1)
# N    N-(N-1)=1 (0,0)   (1,1)   ... ... ... ... ... ... ... ... ... ... ... ... ...   (N-2,N-2) (N-1,N-1)
#
# Seems that we could "memorize/store" these?  Perhaps
# calculate sums for each, and as we must calculate
# the new sums, we "adjust" each by adding each a[j1] s.t. j<j1
# and by subtracting each a[i1] s.t. i1<i.
# We could adjust i and j by adding the new right-hand item, the
# "new j," and by subtracting from the sum the old i, and advancing
# i to be the "new i."  (This is very imprecise language!)
#
# If we can calculate the sums represented in each row, then we
# merely need to search for the "maximum" sum possible.  It may
# be possible to "compress" things so that we don't have to
# explicitly store everything, but storing things explicitly
# might make it easier to derive a correct program, after which
# we can figure out how to "compress" things down into a loop
# which only "caches" what is absolutely necessary.
#
# But this also seems to lead us to a O(N^2) solution,
# quadratic-time nested loops and all that.
#
# Why couldn't we build up the sub-sums in a "bottom-up" fashion?
# That might lead to a divide-and-conquer, possibly O(N * lg N) solution.
# 
# What in the world leads to a linear-time solution, if there is one?
# We must find a way to keep things as a linear time search?
