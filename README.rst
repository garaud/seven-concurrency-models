
Seven Concurency Models
#######################

My playground & sandbox about the book `Seven Concurrency Models in Seven Weeks
<https://pragprog.com/book/pb7con/seven-concurrency-models-in-seven-weeks>`_ by
Paul Butcher.

Just some piece of code in C++11, Common Lisp, Clojure, Rust, OCaml or Python
inspired from examples of the book. I hope to have time to write some examples
in these languages (or more)...

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

On my Debian, it's GCC_ which is used by default (>=4.9). If you want to compile
with Clang_ (>=3.4), just do:

::

   CXX=clang++ cmake /path/to/7-concurrency/[chapter]/c++

in your build directory.

Python
------

Just run ``python`` or ``python3`` on Python files.

Rust
----

No Makefiles, just type ``rustc file.rs``

Common Lisp
-----------

As I use Emacs_, I install Slime_ which comes with sbcl_ (Common Lisp compiler).

In Emacs_, open a CLisp file, ``M-x slime`` and type ``(load "filename")`` in
the Slime_ prompt. You can carry out the same operation in the sbcl_ prompt.

Out of any Common Lisp REPL_, you can type:

::

  sbcl --script filename.lisp

Clojure
-------

Install Java JRE/JDK and Clojure_ >= 1.6. Most of the time, run with the
``clojure`` command as ``clojure -cp . filename.clj``. Sometine, I think that
I'll use leiningen_ (with a simple ``lein run``).


.. Some links
.. _CMake: http://www.cmake.org/
.. _GCC: https://gcc.gnu.org/
.. _Clang: http://clang.llvm.org/
.. _Emacs: http://www.gnu.org/software/emacs/
.. _Slime: https://common-lisp.net/project/slime/
.. _sbcl: http://www.sbcl.org/
.. _REPL: http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop
.. _bordeaux-threads: https://trac.common-lisp.net/bordeaux-threads/wiki/ApiDocumentation
.. _Clojure: http://clojure.org/
.. _leiningen: http://leiningen.org/
