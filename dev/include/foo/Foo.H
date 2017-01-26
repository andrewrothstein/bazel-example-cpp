#ifndef __FOO_H_
#define __FOO_H_

#include "foo/Monster.H"

class Foo
  : public Bar
{
public :

  Foo(const std::string && n) : _name(n) {}

  std::ostream & awaken(std::ostream & os) const;

private :

  std::string _name;
  
};
  
#endif // __FOO_H_
