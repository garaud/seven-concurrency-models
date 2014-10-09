

fn main() {
    println!("Hello from main");
    spawn(proc() {
        println!("Hello from new thread")
    });
}
