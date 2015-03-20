from collections import defaultdict

def dijkstra(nodi,archi,iniziale):
    distanza = {iniziale: 0}
    path = {}
    
    while nodi:
    # PREPARAZIONE
        # Trovo nodo con distanza minima
        nodo_min = None
        for nodo in nodi:
            if nodo in distanza:
                if nodo_min is None: nodo_min = nodo
                elif distanza[nodo] < distanza[nodo_min]: nodo_min = nodo
        if nodo_min is None: break
        print("Elimino "+nodo_min, nodi)
        nodi.remove(nodo_min)
        distanza_min = distanza[nodo_min]
        # Calcolo mappa archi uscenti da min -> distanza da min
        distanze_da_min=defaultdict(list)
        for arco in archi.keys():
            if arco[0] == nodo_min: distanze_da_min[arco[1]]=archi[arco]
            if arco[1] == nodo_min: distanze_da_min[arco[0]]=archi[arco]
        print(distanze_da_min)
        #Algoritmo di Dijkstra
        for destinazione in distanze_da_min:
            # Calcolo la distanza della destinazione passando da nodo_min
            nuova_distanza = distanza_min + distanze_da_min[destinazione]
            # Se migliore della precedente sostituisco distanza e prossimo
            if destinazione not in distanza or nuova_distanza < distanza[destinazione]:
                distanza[destinazione] = nuova_distanza
                path[destinazione] = nodo_min
        #Tabella di routing
        tabella=defaultdict(list)
        for destinazione in distanza.keys():
            if destinazione != iniziale:
                tabella[destinazione]=(path[destinazione],distanza[destinazione])
    return tabella

# 4 nodi: provare a disegnare la rete
l = dijkstra(
set(['a','b','c','d']),
{('a','b'):1,
 ('b','c'):2,
 ('a','d'):3,
},
 'a')
print(l)
