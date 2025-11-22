# Problem Description

The ICPC company plans to build a cluster computing system consisting ofnservers. Each server has adatabase protocol typerepresented by a positive integer. Specifically, thei-th server has a protocol typepi.
Initially, all servers are independent. The company wants to establish connections between servers so that, in the resulting network, every server can reach every other server (either directly or indirectly).
To achieve full connectivity, you may establish several connections. Each time you establish a connection, you must choose two serversuandv(u<v). The cost of establishing the connection betweenuandvis defined as thecommon protocolof the databases in the range fromutov, calculated asgcd(pu,pu+1,…,pv)∗.
Determine the minimum total cost required to fully connect allnservers so that every server is reachable from every other server.
∗gcdis the largest positive integer that divides every integer in that set without leaving a remainder.

## Input
The first line contains a single integern, representing the number of servers.
The second line containsnpositive integersp1,p2,…,pn, wherepiis the database protocol type of thei-th server.

## Output
Output a single integer in a line, representing the minimum total cost required to fully connect the cluster computing system.