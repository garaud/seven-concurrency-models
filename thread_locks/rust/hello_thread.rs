// Mainly inspired from official book at
// http://doc.rust-lang.org/book/concurrency.html

use std::thread::Thread;

fn main() {
    println!("Hello from main");
    Thread::scoped(|| {
        println!("Hello from new thread")
    });
}
