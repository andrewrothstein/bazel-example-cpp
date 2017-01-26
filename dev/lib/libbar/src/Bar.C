#include <iostream>

#include "bar/Bar.H"

std::ostream &
Bar::awaken(std::ostream & os) const {
  os << "the Bar(" << _x << ") monster awakens!?!?!?" << std::endl;
  return os;
}
