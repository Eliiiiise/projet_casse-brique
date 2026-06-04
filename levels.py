'''
Ce module contient la configuration des briques dans des différents niveaux du jeu de casse-brique. 
Chaque niveau est représenté par une liste de chaînes de caractères, 
où chaque caractère représente une brique ou un espace vide. 
Les chiffres indiquent la résistance de la brique, 
tandis que les points (".") représentent des espaces vides où il n'y a pas de brique. 
'''
# Le but est d'augementer au fur et à mesure la difficulté du jeu en augmentant le nombre de briques, leur position, leur résistance, la vitesse de la balle, etc
# facilite l'implémentation de nouveaux niveaux plus tard

'''
niveau 1 : 3 lignes x 14 briques
niveau 2 : 4 lignes x 14 briques (une ligne de plus que le niveau 1 ou 3)
niveau 3 : en pyramide : 8 briques, puis 7 briques, puis 6, puis 5, puis 4, puis 3, puis 2, puis 1 
niveau 4 : 

Quand les niveaux sont fini on recommence au niveau 1 mais avec une duretée des briques plus forte (plus de coups pour les casser)
Proposition également pour augementer la vitesse de la balle pour que ce soit plus difficile au tour suivant etc...
'''

LEVELS = [
    # NIVEAU 1
    [
        "22222222222222",
        "22222222222222",
        "22222222222222"
    ],
    
    # NIVEAU 2
    [
        "22222222222222",
        "22222222222222",
        "22222222222222",
        "22222222222222"
    ],

    # NIVEAU 3
    [
        "......22......",
        ".....2222.....",
        "....222222....",
        "..2222222222..",
        ".222222222222.",
        "22222222222222"
    ],

    # NIVEAU 4
    [
        "2.2.2.2.2.2.2.",
        ".2.2.2.2.2.2.2",
        "2.2.2.2.2.2.2.",
        ".2.2.2.2.2.2.2",
        "2.2.2.2.2.2.2."
    ],

    #NIVEAU 5
    [

        "22222222222222",
        "222222..222222",
        "22222....22222",
        "2222..22..2222",
        "222..2222..222",
        "22..222222..22",
        "2..22222222..2" 
    ],

    #NIVEAU 6
    [

        "22222222222222",
        ".............2",
        "22222222222222",
        "2.............",
        "22222222222222",
        ".............2",
        "22222222222222"   
    ],

    #NIVEAU 7
    [
        "22222222222222",
        "2............2",
        "2..22222222..2",
        "2..2......2..2",
        "2..2..22..2..2",
        "2..2..22..2..2",
        "2..2......2..2",
        "2..22222222..2",
        "2............2",
        "22222222222222"
        
    ],

    #NIVEAU 8 (spirale)
    [
        "2222222222222.",
        "2...........2.",
        "2.222222222.2.",
        "2.2.......2.2.",
        "2.2.2...2.2.2.",
        "2.2.2.2.2.2.2.",
        "2.2.2.2.2.2.2.",
        "2.2.2.222.2.2.",
        "2.2.2.....2.2.",
        "2.2.2222222.2.",
        "2.222222222.2."
    ],

    # NIVEAU 9 (losange)
    [
        "......22......",
        ".....2222.....",
        "....222222....",
        "...22222222...",
        "..2222222222..",
        "...22222222...",
        "....222222....",
        ".....2222.....",
        "......22......"
    ],

    #NIVEAU 10 (sablier)
    [
        "22222222222222",
        ".222222222222.",
        "..2222222222..",
        "...22222222...",
        "...22222222...",
        "..2222222222..",
        ".222222222222.",
        "22222222222222"
    ]
]

#l'idée est de lire la boucle de 10 niveaux une fois puis la relire en renforçant la résistance de 1 pour chaque brique jusqu'à résistance =4

