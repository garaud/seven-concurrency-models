// Example of shared data and race condition with a simple counter which is
// incremented by two threads.

#include <iostream>
#include <thread>

using std::cout;
using std::endl;

struct Counter {
    Counter(int init = 0) : _count(init) {};
    void increment() { ++_count; }
    int current_value() const { return _count; }
private:
    int _count;
};

void increment_loop(Counter& counter) {
    for (int i = 0; i < 5000; ++i) {
        counter.increment();
    }
}

int main() {
    Counter counter;
    std::thread thread_a(increment_loop, std::ref(counter));
    std::thread thread_b(increment_loop, std::ref(counter));
    thread_a.join(); thread_b.join();
    // Print the non deterministic value of the counter due to *race condition*.
    cout << "Counter value: " << counter.current_value() << endl;

    return 0;
}
