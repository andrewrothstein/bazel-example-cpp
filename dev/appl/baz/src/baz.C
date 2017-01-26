#include <string>

#include "foo/Foo.H"
#include "bar/Bar.H"

int
main(int argc, const char ** argv) {
  const Monster * m(argc > 1 ? new Foo("Cecelia") : new Bar(14));
  m->awaken(std::cout);
  delete m;
  return EXIT_SUCCESS;
}
  
