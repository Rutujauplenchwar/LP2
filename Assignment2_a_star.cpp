#include <iostream>
#include <vector>
#include <queue>
#include <functional> // Added for std::function
#include <algorithm>
using namespace std;

struct Node
{
    vector<vector<char>> data;
    int level;
    int fval;

    Node(vector<vector<char>> d, int l, int f) : data(d), level(l), fval(f) {}

    // Overload operator== to compare two Node objects based on their data
    bool operator==(const Node &other) const
    {
        return data == other.data;  // Compare the puzzle data
    }
};

class Puzzle
{
private:
    int n;
    priority_queue<Node, vector<Node>, function<bool(Node, Node)>> open;
    vector<Node> closed;

    pair<int, int> findBlank(const vector<vector<char>> &puz)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (puz[i][j] == '_')
                {
                    return {i, j};
                }
            }
        }
        return {-1, -1};
    }

    vector<vector<char>> performSwap(const vector<vector<char>> &puz, int x1, int y1, int x2, int y2)
    {
        vector<vector<char>> newPuz = puz;
        swap(newPuz[x1][y1], newPuz[x2][y2]);
        return newPuz;
    }

    vector<Node> generateChildren(Node &cur)
    {
        vector<Node> children;
        pair<int, int> blank = findBlank(cur.data);
        int x = blank.first, y = blank.second;
        vector<pair<int, int>> moves = {{x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1}};

        for (auto &move : moves)
        {
            int newX = move.first, newY = move.second;
            if (newX >= 0 && newX < n && newY >= 0 && newY < n)
            {
                vector<vector<char>> childData = performSwap(cur.data, x, y, newX, newY);
                children.push_back(Node(childData, cur.level + 1, 0));
            }
        }
        return children;
    }

    int calculateH(const vector<vector<char>> &start, const vector<vector<char>> &goal)
    {
        int h = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (start[i][j] != goal[i][j] && start[i][j] != '_')
                {
                    h++;
                }
            }
        }
        return h;
    }

    int calculateF(Node &start, const vector<vector<char>> &goal)
    {
        return calculateH(start.data, goal) + start.level;
    }

    void printPuzzle(const vector<vector<char>> &puz, int g, int h, int f)
    {
        cout << "g=" << g << ", h=" << h << ", f=" << f << endl;
        for (auto &row : puz)
        {
            for (auto &val : row)
            {
                cout << val << " ";
            }
            cout << endl;
        }
    }

public:
    Puzzle(int size) : n(size), open([](const Node &a, const Node &b)
                                     { return a.fval > b.fval; }) {}

    void process()
    {
        vector<vector<char>> start(n, vector<char>(n));
        vector<vector<char>> goal(n, vector<char>(n));

        cout << "Enter the start state matrix:" << endl;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cin >> start[i][j];
            }
        }

        cout << "Enter the goal state matrix:" << endl;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                cin >> goal[i][j];
            }
        }

        Node startNode(start, 0, 0);
        startNode.fval = calculateF(startNode, goal);
        open.push(startNode);

        cout << "\nInitial state:" << endl;
        printPuzzle(startNode.data, startNode.level, calculateH(startNode.data, goal), startNode.fval);

        while (!open.empty())
        {
            Node cur = open.top();
            open.pop();

            // Print the current state with its heuristic values
            cout << "\nExploring state with f = " << cur.fval << ":\n";
            printPuzzle(cur.data, cur.level, calculateH(cur.data, goal), cur.fval);

            if (calculateH(cur.data, goal) == 0)
            {
                cout << "Goal state reached!" << endl;
                break;
            }

            // Generate and print all children
            vector<Node> children = generateChildren(cur);
            cout << "\nGenerated child states at level " << cur.level + 1 << ":\n";
            for (auto &child : children)
            {
                child.fval = calculateF(child, goal);
                cout << "\nChild state with f = " << child.fval << ":\n";
                printPuzzle(child.data, child.level, calculateH(child.data, goal), child.fval);
            }

            // Push only the best (lowest f-value) child to the open queue
            for (auto &child : children)
            {
                if (find(closed.begin(), closed.end(), child) == closed.end())
                {
                    open.push(child);
                }
            }

            closed.push_back(cur);
        }
    }
};

int main()
{
    Puzzle puz(3);
    puz.process();
    return 0;
}
