
#include <iostream>
#include <thread>

using std::cout;
using std::endl;

void run() {
    cout << "Hello from new thread" << endl;
}

int main() {
    std::thread thread(run);
    cout << "Hello from main" << endl;
    thread.join();
    return 0;
}
