
struct Counter {
    value : int
}

fn increment_loop(counter: &mut Counter) {
    for n in range(0u, 5000u) {
        counter.value += 1
    }
}

fn intincr(value: &mut int) {
    *value = *value + 1
}

fn main() {
    //let mut c : Counter = Counter { value: 0 };
    //increment_loop(&c);
    //println!("Counter value {}", c.value);

    let mut x = 10i;
    intincr(x);
    println!("x value: {}", x);
}
