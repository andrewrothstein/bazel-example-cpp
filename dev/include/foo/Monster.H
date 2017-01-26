#ifndef __MONSTER_H__
#define __MONSTER_H__

#include <iosfwd>

class Monster {

public:

  virtual std::ostream & awaken(std::ostream & os) const = 0;

};



#endif // __MONSTER_H__
