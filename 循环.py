#include <iostream>

using namespace std;

int main() {
    for (int i = 1; i <= 100; i++) {
        cout << i << " ";
        if (i % 10 == 0) {
            cout << endl;
        }
    }
    return 0;
}


#include <iostream>

using namespace std;

int main() {
    int i = 1;
    while (i <= 100) {
        cout << i << " ";
        if (i % 10 == 0) {
            cout << endl;
        }
        i++;
    }
    return 0;
}


#include <iostream>

using namespace std;

int main() {
    int i = 1;
    do {
        cout << i << " ";
        if (i % 10 == 0) {
            cout << endl;
        }
        i++;
    } while (i <= 100);
    return 0;
}
