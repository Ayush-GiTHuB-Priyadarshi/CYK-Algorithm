import re

class CFG:
    def __init__(self, productions):
        self.productions = self.parse_productions(productions)

    def parse_productions(self, productions):
        production_dict = {}
        # Split production rules using semicolon (;)
        for production in productions.split(';'):
            head, body = production.split('->')
            head = head.strip()
            # Handle multiple right-hand side cases (separated by '|')
            bodies1 = body.split('|')
            bodies = []
            for b in bodies1:
                bodies.append(list(b.strip()))
            if head not in production_dict:
                production_dict[head] = []
            production_dict[head].extend(bodies)  # Add the bodies to the list for the current head
        return production_dict

    def cykParse(self,  w):
        n = len(w)
        
        if n == 0:
            return False
        
        T = [[set() for _ in range(n)] for _ in range(n)]

        for j in range(n):
            for lhs, rules in self.productions.items():
                for rhs in rules:
                    if len(rhs) == 1 and rhs[0] == w[j]:  
                        T[j][j].add(lhs)

        for length in range(2, n + 1):  
            for i in range(n - length + 1):
                j = i + length - 1  

                for k in range(i, j):  
                    for lhs, rules in self.productions.items():
                        for rhs in rules:
                            if len(rhs) == 2:  
                                A, B = rhs
                                if A in T[i][k] and B in T[k + 1][j]:
                                    T[i][j].add(lhs)
        return 'S' in T[0][n - 1]

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, source, target, label):
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        self.adjacency_list[source].append((target, label))

    def get_edges(self):
        return self.adjacency_list
