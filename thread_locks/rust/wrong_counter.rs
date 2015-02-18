// Example of a wrong threaded counter.

// Reading this http://doc.rust-lang.org/book/concurrency.html, I think yon can
// not share mutable state between threads (it does not compile).

use std::thread::Thread;

// Dumb counter
struct Counter {
    value : i32
}

// Function which increments the value by one.
fn increment_loop(counter: &mut Counter) {
    for _ in 0u32..5000u32 {
        counter.value += 1
    }
}


fn main() {
    let mut counter : Counter = Counter { value: 0 };
    // First thread.
    Thread::spawn(move || {
        increment_loop(&mut counter);
    });
    // increment_loop(&mut counter);
    println!("Counter value {}", counter.value);

    // let mut x = 10;
    // x = incr(x);
    // println!("x value: {}", x);
}
