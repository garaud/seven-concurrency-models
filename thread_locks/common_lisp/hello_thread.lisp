;; Simple 'hello' thread example.
;; Use sbcl threading support.

(use-package :sb-thread)
;; TODO: try to make thread with Bordeaux-threads package.
;; (import :bordeaux-threads)
;; (use-package :bordeaux-threads)

(defun hello ()
  (write-line "Hello from new thread")
  )

(defun main ()
  (write-line "Hello from main")
  (make-thread 'hello)
  )

(main)
