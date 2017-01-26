#include "foo/Foo.H"

#include <iostream>

std::ostream &
Foo::awaken(std::ostream & os) const {
  os << "who awakens the Foo(" << _name << ") monster?!?!?" << std::endl;
  return os;
}
