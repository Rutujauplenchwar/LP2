#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Node
{
public:
    int data;
    Node *left;
    Node *right;

    Node(int d)
    {
        data = d;
        left = NULL;
        right = NULL;
    }
};

bool dfsrec(Node *root, int x, vector<Node *> &visited)
{
    if (root == NULL)
    {
        return false;
    }

    cout << "Visiting the node " << root->data << endl;
    visited.push_back(root);
    if (root->data == x)
    {
        cout << "Node found " << root->data << endl;
        return true;
    }

    // checking left side

    if (find(visited.begin(), visited.end(), root->left) == visited.end())
    {
        if (dfsrec(root->left, x, visited) == true)
        {
            return true;
        }
    }

    // checking right side

    if (find(visited.begin(), visited.end(), root->right) == visited.end())
    {
        if (dfsrec(root->right, x, visited) == true)
        {
            return true;
        }
    }

    cout << "Backtraking from node " << root->data << endl;
    return false;
}

int height(Node *root)
{
    if (root == nullptr)
        return 0;
    int leftHeight = height(root->left);
    int rightHeight = height(root->right);
    return max(leftHeight, rightHeight) + 1;
}


bool printCurrentLevel(Node *root, int level, int target, bool &found)
{
    if (root == nullptr || found) 
        return false;

    if (level == 1)
    {
        cout << root->data << " ";
        if (root->data == target)
        {
            found = true; 
            return true;
        }
    }
    else if (level > 1)
    {
        if (printCurrentLevel(root->left, level - 1, target, found))
            return true;
        if (printCurrentLevel(root->right, level - 1, target, found))
            return true;
    }
    return false;
}


void bfs(Node *root, int target)
{
    int h = height(root);
    bool found = false;

    for (int i = 1; i <= h && !found; i++)
    {
        printCurrentLevel(root, i, target, found);
        cout << endl;
        if (found)
        {
            cout << "\nNode found " << target << endl;
            return;
        }
    }
    if (!found)
    {
        cout << "\nNode not found\n";
    }
}

int main()
{
    Node *root = new Node(10);
    root->left = new Node(20);
    root->right = new Node(30);
    root->left->left = new Node(40);
    root->right->left = new Node(50);
    int x;
    cout << "Enter the node to search ";
    cin >> x;
    vector<Node *> visited;
    dfsrec(root, x, visited);
    
    for (Node *temp : visited)
    {
        cout << temp->data << "  ";
    }

    cout << endl;
    cout << "BFS ==> "<<endl;
    bfs(root, x);
}



// Node* createTree() {
//     int value;
//     cout << "Enter node value (-1 for NULL): ";
//     cin >> value;

//     if (value == -1) return nullptr;

//     Node* newNode = new Node(value);
//     cout << "Enter left child of " << value << endl;
//     newNode->left = createTree();
//     cout << "Enter right child of " << value << endl;
//     newNode->right = createTree();

//     return newNode;
// }