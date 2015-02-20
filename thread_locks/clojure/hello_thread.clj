;; Simple 'hello' thread exemple.
;; Run me with 'clojure -cp . hello_thread.clj'

(defn hello
  []
  (println "Hello from new thread")
  )

(defn main
  "Main function"
  []
  (println "Hello from main")
  (.start (Thread. (hello)))
  )

(main)
