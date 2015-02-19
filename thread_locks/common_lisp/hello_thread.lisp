;; Simple 'hello' thread example.
;; Use bordeaux-threads threading support.

(require 'asdf)
(require 'bordeaux-threads)
(rename-package 'bordeaux-threads 'bt)


(defun hello ()
  (write-line "Hello from new thread")
  )

(defun main ()
  (write-line "Hello from main")
  (bt:make-thread 'hello)
  )

(main)
