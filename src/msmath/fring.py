
""" finite ring classes """

from . conversions import xrange
from . numfuns import gcd, lam, rint, isint, getorder
from . ffield import ffield
from . rational import rational

# zm class

def rintm(x,m) :
  """if x is rational and denominator is relatively prime to m,
     return numerator*denominator**-1; else return x"""
  if isinstance(x,rational) :
    g,a,b = xgcd(m,x.denominator);
    if g == 1 :
      return x.numerator*b;
  elif isinstance(type(x),ffield) and x._p == m and x._x < m :
    return x._x;
  return x;

def __init__(self,x) :
  """Create a finite ring element x mod m"""
  m = self._m;
  x = rintm(x,m);
  if not isint(x) :
    raise TypeError('must be integer');
  self._x = x%m;
  return;

@property
def element(self) :
  """the ring element's value"""
  return self._x;

def __int__(self) :
  """the ring element as a signed value"""
  m = self._m;
  x = self._x;
  return x if 2*x < m or m == 2 else x-m;

@property
def modulus(self) :
  """the ring's modulus"""
  return self._m;

def __hash__(self) :
  return hash(int(self));

def __eq__(self,other) :
  """Test if two elements are equal"""
  return type(self) == type(other) and self._x == other._x or int(self) == other;

def __ne__(self,other) :
  """Test if two elements are unequal"""
  return not self == other;

__le__ = __ge__ = __eq__;
__lt__ = __gt__ = lambda x,y:False;

def __bool__(self) :
  return self._x != 0;

__nonzero__ = __bool__

def __str__(self) :
  """Return a string representing the ring element"""
  return '%d'%(int(self));

def __repr__(self) :
  """Return a string representing the ring element
The string is the ___str__ representation followed by percent ring modulus"""
  return str(self)+'%'+str(self._m);

def __add__(self,other) :
  """Return the sum of the two ring elements; integers are treated mod m"""
  m = self._m;
  x = self._x;
  if type(other) != type(self) :
    other = rintm(other,m);
    if not isint(other) :
      return NotImplemented;
  else :
    other = other._x;
  return type(self)((x+other)%m) if other else self;

def __pos__(self) :
  """Return the element"""
  return self;

def __neg__(self) :
  """Return the additive inverse of the element"""
  x = self._x;
  return type(self)(-x) if x else self;

def __sub__(self,other) :
  """Return the difference of the two ring elements; integers are treated mod m"""
  m = self._m;
  x = self._x;
  if type(other) != type(self) :
    other = rintm(other,m);
    if not isint(other) :
      return NotImplemented;
  else :
    other = other._x;
  return type(self)(x-other) if other else self;

def __rsub__(self,y) :
  """Return the difference of the swapped ring elements; integers are treated mod m"""
  m = self._m;
  y = rintm(y,m);
  if not isint(y) :
    return NotImplemented;
  return type(self)(y)-self if y else -self;

def __div__(self,y) :
  """Return the quotient of the two ring elements; integers are treated mod m"""
  m = self._m;
  x = self._x;
  if type(self) == type(y) :
    return y.__rdiv__(x);
  y = rintm(y,m);
  if not isint(y) :
    return NotImplemented;
  return type(self)(y).__rdiv__(x);

def __rdiv__(self,y) :    # y/self
  """Return y/self; y must be an integer and is interpreted mod m"""
  m = self._m;
  y = rintm(y,m);
  if not isint(y) :
    return NotImplemented;
  x = self._x;
  g = gcd(y,x);
  y,x = y//g,x//g;
  g,a,x = xgcd(m,x);
  if g != 1 :
    raise ZeroDivisionError;
  return type(self)(y*x%m);

def __mul__(self,y) :
  """Return the product of the two ring elements; integers are treated mod m"""
  m = self._m;
  x = self._x;
  if type(y) != type(self) :
    y = rintm(y,m);
    if not isint(y) :
      return NotImplemented;
  else :
    y = y._x;
  return type(self)(x*y%m);

def xgcd(a,b) :
  """Return g,c,d where g=ca+db is the gcd of a and b"""
  c,d,e,f = 1,0,0,1;
  while b :
    q,r= divmod(a,b);
    a,c,d,b,e,f = b,e,f,r,c-q*e,d-q*f;
  return (-a,-c,-d) if a < 0 else (a,c,d);

def __pow__(self,e) :
  """Raise the ring element to the specified power"""
  e = rint(e);
  if not isint(e) :
    raise TypeError('power must be integer');
  x = self._x;
  if x <= 1 :
    if x or e > 0 :
      return self;
    if e :
      raise ZeroDivisionError;
    return self+1;
  m = self._m;
  if e < 0 :
    g,a,x = xgcd(m,x);
    if g != 1 :
      raise ZeroDivisionError;
    e = -e;
  return type(self)(pow(x,e,m));

def _create(m,x=None) :
  """Return a zm instance or, if x present, an instance of a zm instance"""
  R = zm(m);
  return R if x is None else R(x);

def __reduce__(self) :
  """Return a tuple for pickling"""
  return (_create,(self._m,self._x));

_zm = {}; # m -> zm(m)

class zm(type) :
  """Class to create finite ring class for Z(m), with signed values
Instance variables (treat as read-only!):
  _m: modulus
Methods: __new__, __init__, __hash__, __eq__, __ne__, __lt__, __le__, __ge__, __gt__,
         __reduce__
Descriptors: m, [multiplicative] order

Each instance of the created type is an element of the ring:
Instance variable (treat as read-only!):
  _x: an integer in range [0,m)

Methods: __init__, __hash__, __repr__, __str__, __int__,
         __pos__, __neg__,
         __bool__, __nonzero__, __eq__, __ne__, __lt__, __gt__, __le__, __ge__
         __add__, __radd__, __sub__, __rsub__,
         __mul__, __rmul__, __div__, __rdiv__, __truediv__, __rtruediv__,
         __pow__, __reduce__
Descriptors: m, x, order [of element]
"""

  def __new__(cls,m) :
    if not (isint(m) and m > 1) :
      return TypeError('must be integer > 1')
    try :
      return _zm[m];
    except Exception :
      pass;
    d = dict(m=modulus,x=element,
             order = property(lambda x: getorder(m)(x._x)),
             _m=m,
             __init__=__init__,
             __repr__=__repr__,
             __str__=__str__,
             __int__=__int__,
             __hash__=__hash__,
             __eq__=__eq__,
             __ne__=__ne__,
             __lt__=__lt__,
             __le__=__le__,
             __gt__=__gt__,
             __ge__=__ge__,
             __bool__ = __bool__,
             __nonzero__=__nonzero__,
             __neg__=__neg__,
             __pos__=__pos__,
             __add__=__add__,
             __radd__=__add__,
             __sub__=__sub__,
             __rsub__=__rsub__,
             __mul__=__mul__,
             __rmul__=__mul__,
             __div__=__div__,
             __truediv__=__div__,
             __rdiv__=__rdiv__,
             __rtruediv__=__rdiv__,
             __pow__=__pow__,
             __reduce__=__reduce__,
            );

    _zm[m] = f = type.__new__(cls,'Z%d'%(m),(),d);
    return f;

  def __init__(self,*args,**kwargs) :
    return;

  def __reduce__(self) :
    """Return a tuple for pickling"""
    return (_create,(self._m,));

  def __hash__(self) :
    return hash(type(self))^hash(self._m);

  def __eq__(self,other) :
    return type(self)==type(other) and self._m==other._m;
  
  def __ne__(self,other) :
    return not self==other;

  __le__ = __eq__;
  __ge__ = __eq__;
  __lt__ = __lt__;
  __gt__ = __gt__;

  m = modulus;

  def __len__(self) :
    """Return the modulus, the size of the ring"""
    return self._m;

  def __iter__(self) :
    """Return an iterator for the elements of the ring"""
    return(self(x) for x in xrange(self._m));

  @property
  def order(self) :
    """the multiplicative order of the ring"""
    try :
      return self.__order;
    except AttributeError :
      self.__order = l = lam(self._m);
      return l;

  def foo(self,foo=None) :
    raise AttributeError("type object '%s' has no Attribute 'x'"%(self.__name__));

  x = property(foo,foo,foo);
  del foo;
