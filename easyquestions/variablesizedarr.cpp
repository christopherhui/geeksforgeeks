#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, q, k, num, a, b; cin >> n >> q;
    vector<int> arr[n];
    for (int i = 0; i < n; i++) {
        cin >> k;
        for (int j = 0; j < k; j++) {
            cin >> num;
            arr[i].push_back(num);
        }
    }
    for (int x = 0; x < q; x++) {
        cin >> a >> b;
        cout << arr[a][b] << endl;
    }
    return 0;
}
