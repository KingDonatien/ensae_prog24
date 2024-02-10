from grid import Grid
from graph import Graph
import copy

g = Grid(2, 3)
print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

print(file_name)

g = Grid.grid_from_file(file_name)
print(g)




















def bfs_swap(self):

    def find_perm(g1,g2):
        e1, e2 = None, None
        for i in range(self.m):
            for j in range (self.n):
                if g1[i][j] != g2[i][j] :
                    e1 = g1[i][j]
                    e2 = g2[i][j]
                    break
            if e1 is not None and e2 is not None :
                break
        return e1, e2

    gr = construct_graph(self.n,self.m)
    longueur_chemin, chemin = gr.bfs(self.state, [[i*j for j in range(1, self.n)] for i in range(1,self.m + 1)])
    
    for k in range (len(chemin)-1):
        g1, g2 = chemin[k], chemin[k+1]
        self.swap(find_perm(g1,g2))

def bfs_epure(src, dst):  # Question 8
    """
    il faut associer une clé unique à chaque grille
    """
    liste_grilles=Grid(2,3).gridlist_from_permlist()
    cle_src=liste_grilles.index(src.state)
    g=Graph([cle_src])
    liste_chemins=[[src]]
    aparcourir=[src]
    parcourus=[src]
    while aparcourir!=[]:
        s=aparcourir[0]
        aparcourir=aparcourir[1:]
        cle_s = liste_grilles.index(s.state)
        print(cle_s)
        """
        on complète les chemins en récupérant le chemin finissant par s
        """
        for chemin in liste_chemins :
            if chemin[len(chemin)-1]==s:
                chemin_a_completer=chemin
                liste_chemins.remove(chemin)
        """
        on crée la liste de toutes les grilles voisines de s
        """
        V_tmp=s.grilles_voisines()
        V=[]
        for i in range(len(V_tmp)):
            v=Grid(2,3)
            v.state=V_tmp[i]
            V.append(v)
        """
        on rajoute au graphe les voisins de s qui ne sont pas déjà parcourus ni à parcourir
        """
        for voisin_possible in V:
            if (voisin_possible not in aparcourir) and (voisin_possible not in parcourus):
                try:
                    g.graph[cle_s].append(voisin_possible)
                except:
                    g.graph[cle_s]=[voisin_possible]
                liste_chemins.append(chemin_a_completer+[voisin_possible])
                aparcourir.append(voisin_possible)
                parcourus.append(voisin_possible)
            if voisin_possible==dst:
                return (len(chemin_a_completer), chemin_a_completer+[voisin_possible])
    return None


grille_test=Grid(2,3)
grille_test.swap((1,0),(1,1))
grille_test.swap((0,0),(0,1))
grille_test.swap((1,2),(0,2))
print(bfs_epure(grille_test,Grid(2,3)))