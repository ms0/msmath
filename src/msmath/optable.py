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

from . ffield import *    # for creating finite fields
from . fring import *     # for creating finite rings

def hexify(r,radix=16) :
  """Given a finite field, make its __str__ output in radix radix """
  n = ceil(log(r.__len__(),radix));
  r.__str__ = lambda self: stradix(self.x,radix,n);

def optable(op,r,native=False) :
  """Given op and ring, return a string showing the op table"""
  rop = {'+':r.__add__,'*':r.__mul__,'x':r.__mul__}[op];
  elements = list(r);
  excluded = set();
  if op.lower() == 'x' :
    for x in reversed(elements) :
      for y in elements :
        if x*y == 1 :
          break;
      else :
        excluded.add(x);
  n = len(elements);
  ss = len(str(elements[-1] if native else n-1));
  formatstring = '%%%ds'%(ss+1);
  o = [formatstring%(op)+' |'];
  for j in range(n) :
    if elements[j] in excluded : continue;
    o.append(formatstring%(elements[j] if native else j));
  o.append('\n'+'-'*((n+1)*(ss+1)+2)+'\n');
  for i in range(n) :
    if elements[i] in excluded : continue;
    o.append(formatstring%(elements[i] if native else i)+' |');
    for j in range(n) :
      if elements[j] in excluded : continue;
      o.append(formatstring%(rop(elements[i],elements[j]) if native else
                             rop(elements[i],elements[j]).x));
    o.append('\n');
  return ''.join(o);

def htmloptable(op,r,native=False) :
  """Given op and ring, return as a string an HTML table element for the op table"""
  rop = {'+':r.__add__,'*':r.__mul__,'x':r.__mul__}[op];
  sop = {'+':'+','*':'&times;','x':'&times;'}[op];
  elements = list(r);
  excluded = set();
  if op.lower() == 'x' :
    for x in reversed(elements) :
      for y in elements :
        if x*y == 1 :
          break;
      else :
        excluded.add(x);
  n = len(elements);
  o = ["<table class='optable'><tr><th>"+sop+"</th>"];
  for j in range(n) :
    if elements[j] in excluded : continue;
    o.append("<th>"+str(elements[j] if native else j)+"</th>");
  o.append("</tr>");
  for i in range(n) :
    if elements[i] in excluded : continue;
    o.append("<tr><th>"+str(elements[i] if native else i)+"</th>");
    for j in range(n) :
      if elements[j] in excluded : continue;
      o.append("<td>"+str(rop(elements[i],elements[j]) if native else
                          rop(elements[i],elements[j]).x)+"</td>");
    o.append("</tr>")
  o.append("</table>");
  return ''.join(o);

# sample css for formatting html optable
css4optable = """
table.optable {
  border-collapse:collapse;
  border-spacing:12px 0;
}
table.optable tr:first-child th {
  border-bottom:1px solid black;
}
table.optable tr th:first-child {
  border-right:1px solid black;
}
table.optable th {
  font-size:8pt;
  padding:0 3px;
}
table.optable td {
  font-size:8pt;
  padding:0 3px;
}
"""
