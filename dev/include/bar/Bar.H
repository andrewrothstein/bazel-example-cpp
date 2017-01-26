#ifndef __BAR_H__
#define __BAR_H__

#include "foo/Monster.H"

class Bar
  : public Monster
{
public:

  Bar(int x) : _x(x) {}

  std::ostream & awaken(std::ostream & os) const;
  
private :

  int _x;
  
};
  

#endif // __BAR_H__
