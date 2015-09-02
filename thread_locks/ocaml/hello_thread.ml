
(* #load "Thread";; *)

(* Open Core.std *)

let hello () = print_string "Hello World!\n";;
let second_hello () = print_string "Hello from new thread\n";;
let tmp = Thread.create second_hello();;
Thread.join tmp;;

hello ();;
