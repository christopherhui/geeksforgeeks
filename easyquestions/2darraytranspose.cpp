using namespace std;

int main() {
	int t, arr[100][100]; cin >> t;
	for (int i = 0; i < t; i++) {
	    int n; cin >> n;
	    for (int j = 0; j < n; j++) {
	        for (int l = 0; l < n; l++) {
	            cin >> arr[l][j];
	        }
	    }
	    for (int b = 0; b < n; b++) {
	        for (int c = 0; c < n; c++) {
	            cout << arr[b][c] << " ";
	        }
	    }
	    cout << endl;
	}
	return 0;
}
