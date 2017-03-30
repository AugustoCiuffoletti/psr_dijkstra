from collections import defaultdict

# Dato il grafo e la radice restituisce la tabella di routing
# per la radice
def dijkstra(nodi,archi,radice):
    raggiunti = {radice: 0}
    next_hop = {}
    
	# Svuota progressivamente l'insieme dei "nodi" aggiungendo
	# i nodi che rimuove al dizionario "raggiunti" e calcolandone la
	# distanza, inserita come "value" del dizionario, e il primo hop
	# nella route, indicandola in un altro dizionario "next_hop".
    # Il grafo e' definito dall'insieme "nodi" e dall'insieme "archi",
    # coppie di nodi collegati da un link. La radice dell'albero (cioe'
    # il nodo che esegue l'algoritmo) e' nel parametro "radice".
    
    while nodi:      # Ripete finche' l'insieme "nodi" si svuota 
    # PREPARAZIONE
        # Trovo nodo con distanza minima tra quelli raggiunti
        nodo_min = None
        for nodo in nodi:
            if nodo in raggiunti:
                if nodo_min is None: nodo_min = nodo
                elif raggiunti[nodo] < raggiunti[nodo_min]: nodo_min = nodo
        if nodo_min is None: break
        print("Elimino "+nodo_min, nodi)
        nodi.remove(nodo_min)
        distanza_min = raggiunti[nodo_min]
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
            if destinazione not in raggiunti or nuova_distanza < raggiunti[destinazione]:
                raggiunti[destinazione] = nuova_distanza
                next_hop[destinazione] = nodo_min
        #Tabella di routing
        tabella=defaultdict(list)
        for destinazione in raggiunti.keys():
            if destinazione != radice:
                tabella[destinazione]=(next_hop[destinazione],raggiunti[destinazione])
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
# 4 nodi: provare a disegnare la rete
#l = dijkstra(
#set(['a','b','c','d']),	# l'insieme dei nodi
#{('a','b'):1,				# l'insieme degli archi (coppie di nodi)
# ('b','c'):2,
# ('a','d'):3,
#},
# 'a')						# la radice
#print(l)


l = dijkstra(
set(['1','2','3','4', '5', '6']),
{('1','2'):7,
 ('1','3'):9,
 ('1','6'):14,
 ('2','3'):10,
 ('2','4'):15,
 ('3','4'):11,
 ('3','6'):2,
 ('6','5'):9,
 ('4','5'):6,
},
 '1')
print(l)
