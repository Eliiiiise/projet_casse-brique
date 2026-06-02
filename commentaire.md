# ce qu'on veut/doit faire
-- en pause un texte recap s'affiche genre points, nb de vie, level ->il faut juste que le score s'affiche suivant notre jeu pour l'instant c'est des com car variable pas créer

--"game over" apparait en gros avec en dessous un recap des point du level et en dessous un bouton pour rejouer -> ->il faut juste que le score,  s'affiche suivant notre jeu pour l'instant c'est des com car variable pas créer

-- faire une partie entrer nom de joueur pour le highscore

-- SCORE


# ce qu'on fait et quand psk flemme de faire des vocaux et de devoir réécouter ma voix, ou de tout essayer de se rapeller quand j'écrit le commit:
-- 18.05 Elise: 
    - j'ai fait le level 8 mais il rend pas top top de visuel 
    - j'ai fait les collisions dans le fichier et importer dans gameco
    - j'ai créer le fichier input_manager pour décharger gameco -> il sert a gérer souris, clavier, clic, interraction : donc j'ai déplacer les trucs de souris, de clavier et le bouton "jouer" dedans  et ca fonctionne
    - menu game-over créer il faut juste faire que ca note le score qu'on calculera et le niveau atteint. Et changer les couleurs du bouton rejoue. j'ai aussi fait un bouton X qui permet de quitter le jeu proprement et qui gonfle quand on passe dessus.
    - j'ai fait tout ca mais ca ne marche plus quand la balle tombe je n'ai pas de vie supp et le menu gameover ne s'affiche pas et la j'avoue qu'il est 00h30 et que mon cerfveau lache un peu totalement donc je vais ma'arréter la pour adj et voir ca demain a 13h  peut-etre avec Estiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.
    -les vies supp n'existe plus et je sais pas pk !???!!!!


-- 19.05 Elise: 
    - j'ai créer un fichier pause_menu pour que tout soit au meme endroit et pas dispatcher et donc se sera plus facil pour les modifs.j'ai fait un bouton reprendre, mais le P fonctionne tjrs pour reprendre le jeu.Je fais aussi le bouton quit ici. il a un bouton home (avec une petite maison) et il est trop beaaaauuuu!!!!!
    - le fichier menu est devenu home_menu 
    les vies et le gameover ne fonctionnent tjrs pas faut VRAIEMENT regarder ca 


-- 29.05 Elise :
    - j'ai déplacer tout les def_handle des menus dans input_manager et home et pause fonctione
    - j'ai réglé un truc les vie supp sont revenus !!!!!!!!!!!
    - erwan a reussi a nous faire apparaitre la page gameover !!!!!!!!!!!!!!!!!!!!!!! mais les boutons de la page fonctionne pas
    - le level 8 est au top
    - les boutons de du menu game over marche!!!!!!
    - les powerups on fonctionné mais dès que j'ai finis de changer tous les ball en balls, la balle a commencé a suivre le mouvement de la raquette et je sais pas pk, j'ai tout essayé meme revenir en arrière rien ne marche j'ai un video de ce que j'ai faut que je t'ai envoyé.

-- 02.02 Elise:
    - j'essaie de réparer tout ca mais le pb mtn c'est les collisions qui ne marche plus.
    - les collisions refonctionne mais la ball suis la raquette => pb d'implementation dans collisions le truc dx_mouse doit etre dans le if ball.rect.colliderect...
    - la ball ne suis plus la raquette mais a voir les powerup ne fonctionne que 2sec ou pas du tout 
    - la gestion du temps se fait dans gameco et non pas dans collisions c'est pour ca que les powerup marchaient pas
    - le powerup 5 faisait que on pouvait juste jouer avec la 1ere ball j'ai changé ca avec la ligne 30 dans collisions : if not getattr(game, "piercing", False):
    - je vais changé la couleur de la raquette quand elle s'agrandit ou rapetissit mais en fait a par le 5 aucun ne fonctionne vrm 
    - alors les couleurs sont changées et tous les powerup fonctionnent !!!!!!!!!!!!!!!!!!!!!!!!!!
    - j'ai affiché le nbr de vie durant le jeu avec des petits coeurs rose !!!!!!! et j'ai expliqué a coté comment les créer
    - sur la page pause et gameover les vies et les levels sont dynamique (ils changent au cours du jeu)
    il manque plus que les scores (qui sont pour l'instant ecrit dans les 2 page mais en com, psk les score existe pas)