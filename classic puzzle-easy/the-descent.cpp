//https://www.codingame.com/ide/puzzle/the-descent
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * The while loop represents the game.
 * Each iteration represents a turn of the game
 * where you are given inputs (the heights of the mountains)
 * and where you have to print an output (the index of the mountain to fire on)
 * The inputs you are given are automatically updated according to your last actions.
 **/

int main()
{
 // game loop
    while (1) {
        int max = 0;
        int imax = 0;
        
        for (int i = 0; i < 8; i++) {
            int mountainH; // represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
            cin >> mountainH; cin.ignore();
            
            if (mountainH > max) {
                max = mountainH;
                imax = i;
            }
        }

        cout << imax << endl;
    }
}
