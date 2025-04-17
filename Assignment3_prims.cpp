
#include<iostream>
using namespace std;


#define inf 999
class Graph
{
	int** graph;

	int n;
public:
	Graph()
	{
		cout << "Enter number of vertices:";
		cin >> n;
		graph = new int* [n];
		int i;
		for (i = 0; i < n; i++)
		{
			graph[i] = new int[n];
		}
		for (i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				graph[i][j] = 0;
			}
		}



	}


	void readEdges()
    {
        int u , v , w;
        while(1)
        {
            cin>>u>>v>>w;
            if(u== -1)break;
            graph[u][v]= w;
            graph[v][u] = w;
        }
    }
	
	void read_matrix()
	{
		int i, j;
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				cin >> graph[i][j];
			}
		}
	}
	void prims()
	{
		int i, j;
		int** cost;
		cost = new int* [n];
		for (i = 0; i < n; i++)
		{
			cost[i] = new int[n];
		}
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < n; j++)
			{
				if (graph[i][j] == 0)
				{
					cost[i][j] = inf;
				}
				else
				{
					cost[i][j] = graph[i][j];
				}
			}
		}

		int ne = n - 1;
		int* visited, * distance, * from;
		visited = new int[n];
		distance = new int[n];
		from = new int[n];
		int source;
		cout << "Enter source:";
		cin >> source;
		for (i = 0; i < n; i++)
		{
			visited[i] = 0;
			distance[i] = cost[source][i];
			from[i] = source;
		}
		visited[source] = 1;
		distance[source] = 0;
		int u, v;
		int mincost = 0;
		while (ne > 0)
		{
			int mindist = inf;
			for (i = 0; i < n; i++)
			{
				if (visited[i] == 0)
				{
					if (distance[i] < mindist)
					{
						mindist = distance[i];
						v = i;
					}
				}
			}

			visited[v] = 1;
			u = from[v];
			cout << "Add edge:" << u << "," << v << endl;
			mincost += cost[u][v];
			for (i = 0; i < n; i++)
			{
				if (visited[i] == 0)
				{
					if (distance[i] > cost[v][i])
					{
						distance[i] =  cost[v][i];
						from[i] = v;
					}
				}
			}
			ne--;
		}

		
		cout<<endl<< "mincost=" << mincost << endl;
	}

};
int main()
{
	Graph g;
	g.read_matrix();
	g.prims();
}

