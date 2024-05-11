//https://www.codingame.com/training/easy/container-terminal
//concept: stack

#include <bits/stdc++.h>
using namespace std;
int main()
{
    int         N;
    std::string ships;
    std::cin >> N;
    std::cin.ignore();

    while (N--) {
        getline(std::cin, ships);
        std::vector<std::stack<char>> stacks{};

        std::for_each(
          std::begin(ships), std::end(ships), [&stacks](const auto& c) {
              if (auto l_stack =
                    std::find_if(std::begin(stacks),
                                 std::end(stacks),
                                 [&](auto& st) { return c <= st.top(); });
                  std::end(stacks) != l_stack) {
                  l_stack->push(c);
              } else {
                  stacks.emplace_back(std::stack<char>({ c }));
              }
          });
        /*
        shows the content of vectors
        for(auto it=0;it<stacks.size();it++){
            while(!stacks[it].empty()){
                char c=stacks[it].top();
                cout<<c;
                stacks[it].pop();
            }
            cout<<endl;
        }
        cout<<endl;
        */
        cout<<stacks.size()<<endl;
    }
}
