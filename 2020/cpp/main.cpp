#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    ifstream f("1_data.txt");

    std::vector<int> data;

    if (f.is_open()) {
        std::string line;
        while (getline(f, line)) {
            if(line != "/n") {
                if (!line.find("/n")) {
                    data.push_back(stoi(line));
                }
            }
        }
        f.close();
    } else {
        std::cout << "Error opening file." << std::endl;
    }

    return 0;
}