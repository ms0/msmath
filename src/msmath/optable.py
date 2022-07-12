# Given an operation (+ or * or x) and a finite ring,
# produce a string representation of the operation table.
# Ring elements are numbered consecutively: 0,1,...
# Optional arg native=True uses the default element format for the ring.
# The ring is expected to be a class whose instances are its elements, with
# an __init__ that produces the xth element given x, and an __iter__ that
# iterates the elements in order.
# A ring instance is expected to have an attribute x, the element number.
# Ring elements 0 and 1 are expected to be the ring identities and to compare
# equal to their respective x attribute.
# If the operation is 'x', only invertible elements are included in the table.

from itertools import count

from . conversions import stradix
from . rational import log,ceil

def hexify(r,radix=16) :
  """Given a finite field, make its __str__ output in radix radix """
  n = ceil(log(r.__len__(),radix));
  r.__str__ = lambda self: stradix(self.x,radix,n);

def optable(op,r,native=False) :
  rop = {'+':r.__add__,'*':r.__mul__,'x':r.__mul__}[op];
  elements = list(r);
  if op.lower() == 'x' :
    for x in reversed(elements) :
      for y in elements :
        if x*y == 1 :
          break;
      else :
        del elements[x.x];
  n = len(elements);
  ss = len(str(elements[-1] if native else n-1));
  formatstring = '%%%ds'%(ss+1);
  o = [formatstring%(op)+' |'];
  for j in range(n) :
    o.append(formatstring%(elements[j] if native else j));
  o.append('\n'+'-'*((n+1)*(ss+1)+2)+'\n');
  for i in range(n) :
    o.append(formatstring%(elements[i] if native else i)+' |');
    for j in range(n) :
      o.append(formatstring%(rop(elements[i],elements[j]) if native else
                             rop(elements[i],elements[j]).x));
    o.append('\n');
  return ''.join(o);
