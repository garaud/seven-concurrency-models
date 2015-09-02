// Simple 'hello' thread example.
// Mainly inspired from official book at
// http://doc.rust-lang.org/book/concurrency.html

use std::thread;

fn main() {
    println!("Hello from main");
    thread::spawn(|| {
        println!("Hello from new thread");
    });
}
