
Seven Concurency Models
#######################

My playground & sandbox about the book `Seven Concurrency Models in Seven Weeks
<https://pragprog.com/book/pb7con/seven-concurrency-models-in-seven-weeks>`_ by
Paul Butcher.

Just some piece of code in C++11, Common Lisp, Clojure, Rust or Python inspired
from examples of the book. I hope to have time to write some examples in these
languages (or more)...

Directories
===========

Each directory is related to a specific chapter in the book, or a specific
example.

* ``thread_locks``: 2nd chapter *Threads and Locks*

  Example of threaded "Hello World", a wrong counter with data race (not the
  same count value when you launch the executable).

Languages
=========

C++11
-----

It's an occasion to manipulate the new multithreading features of C++11.

I generate Makefile with CMake_ and compile with GCC_ and Clang_.

Rust
----

No Makefiles, just type ``rustc file.rs``

.. _CMake: http://www.cmake.org/
.. _GCC: https://gcc.gnu.org/
.. _Clang: http://clang.llvm.org/
