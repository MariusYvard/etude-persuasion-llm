# Algorithme Tinder et modèle d'exposition

Sert à deux choses : ne pas tirer les personas uniformément si l'on veut de la fidélité, et savoir ce que pèse réellement le message une fois l'exposition contrôlée.

## Trois niveaux de preuve, à ne jamais confondre

- **Niveau A** Documentation officielle Tinder : page d'aide, blog d'ingénierie lifeattinder.com, ancien Tinder Tech Blog sur Medium, dépôts SEC de Match Group.
- **Niveau B** Brevets. Ils décrivent des inventions revendiquées entre 2007 et 2024. **Rien n'indique que ce qui figure dans la description tourne en production.**
- **Niveau C** Presse et praticiens growth. Une seule source de presse est retenue comme solide ici, l'article Fast Company de 2016, parce qu'il rapporte des propos directs de dirigeants nommés avec démonstration en interne.

## Architecture réelle, ce que Tinder a publié

Source : https://lifeattinder.com/blog/tinders-migration-to-elasticsearch-8

Le moteur est un **Elasticsearch avec plugin de scoring propriétaire en Java**. Plus de 90 % du trafic de recommandation passe par un seul cluster. Deux étages :

1. **Filtrage** : « Users are matched by location, age, interests and other preferences »
2. **Classement** : « Advanced ranking using our custom Tinder ES plugin », avec « 100+ scoring scripts »

Modèles de classement cités avec leurs effets mesurés en interne :
- Expérience Two-Tower P(Match) : « +6.5% match rate increase and a +22% match volume lift »
- Expérience Two-Tower P(Like) : « +3.8% Swipe Right Rate increase »

La migration ES8 débloque la recherche vectorielle kNN et « Profile embeddings similarity search ».

**Lecture centrale.** Le modèle d'exposition est une recherche géo-filtrée suivie d'un re-ranking par modèles à deux tours prédisant P(Like) et P(Match) sur une **paire**. Il n'existe pas, dans cette publication, de score unique et global attaché à un utilisateur. **Niveau A.**

## Le geosharding domine tout le reste

Série en trois parties, Tinder Tech Blog, mai à août 2019.
https://medium.com/tinder-engineering/geosharded-recommendations-part-1-sharding-approach-d5d54e0ec77a

- Contrainte structurante citée : « Tinder's recommendation use cases are location-based, with a **maximum distance of 100 miles** ». Ajout : « most users' preferences are within a 50-mile range ».
- Découpage par bibliothèque S2 de Google, courbes de Hilbert, cellules niveau 7 (environ 45 miles) et niveau 8 (environ 22,5 miles).
- Calibrage : « 40-100 geoshards around the globe results in a good balance ».
- Les nœuds coordinateurs calculent le nombre de geoshards à interroger à partir de la position et du filtre de distance.

**Conséquence pour la simulation.** La proximité n'est pas un critère de tri, elle est inscrite dans la topologie de stockage. Un profil hors du rayon interrogé n'est pas mal classé, **il n'est physiquement pas dans les index consultés**. Le partitionnement géographique est antérieur au classement et le contraint. C'est le fait le plus solide du dossier algorithme. **Niveau A.**

## TinVec, 2017

MLconf SF 2017, Dr Steve Liu, Chief Scientist chez Tinder.

Architecture skip-gram entraînée sur les **co-swipes**, par analogie avec word2vec, **sans utiliser les attributs déclarés du profil**. Les dimensions latentes capturent implicitement activités, intérêts, environnement, trajectoire professionnelle. Recommandation par plus proches voisins d'un vecteur de préférence construit à partir des profils likés. AUC annoncé 90 %, F1 85 %.

Volumétrie annoncée à l'époque : « 1.6B+ swipes daily », 190+ pays.

**Formalise le fait que la préférence est apprise du comportement de swipe, pas du profil déclaré.** Chiffres rapportés en seconde main (page SlideShare inaccessible en direct). **Niveau A avec réserve de lecture indirecte.**

## Le score Elo

### Confirmé, 2016

Austin Carr, Fast Company, 11 janvier 2016.
https://www.fastcompany.com/3054871/whats-your-tinder-score-inside-the-apps-internal-ranking-system

Existence confirmée par le PDG **Sean Rad**, avec démonstration. Le score du journaliste lui a été révélé : **946**, qualifié de « upper end of average ». Rad : « It's not just how many people swipe right on you. It's very complicated. » Jonathan Badeen, VP Product : « a way of essentially matching people and ranking them more quickly and accurately based on who they are being matched up against. »

Principe rapporté : un score par utilisateur, mis à jour à chaque swipe reçu, le gain dépendant du score de l'émetteur. Transposition du classement d'échecs d'Arpad Elo.

**Jamais publié** : la formule, le facteur K, la valeur initiale, la fréquence de mise à jour, l'articulation avec l'ordonnancement. **Niveau ND sur tout le détail.**

### Désavoué, 2019

Page « Powering Tinder », publiée le 15 mars 2019, mise à jour 11 juillet 2022 : « Elo is old news at Tinder. It's an outdated measure and our cutting-edge technology no longer relies on it. »

Aucune justification technique, aucune date d'arrêt effectif, aucune description du remplaçant sous forme d'architecture.

**Inférence, à signaler comme telle.** Le remplaçant plausible est la chaîne filtrage géographique puis re-ranking Two-Tower. La différence de nature est importante : un Elo est un scalaire par utilisateur, transitif et comparable globalement ; un P(Match) est une prédiction sur une paire, non transitive et dépendante du spectateur. La chronologie est cohérente (TinVec 2017, geosharding 2019, Two-Tower avec ES8). **Mais aucun document Tinder ne dit « Elo a été remplacé par des modèles à deux tours ». Ne pas l'écrire comme un fait.**

### Ce qui circule sans source

Score de désirabilité global sous un autre nom, paliers ou tiers de profils, échelles chiffrées des praticiens growth, procédés de reset de compte. Absents de toute source Tinder, brevet ou document SEC. **Niveau ND.**

## Page officielle « Powering Tinder », énoncés cités

https://www.help.tinder.com/hc/en-us/articles/7606685697037

| Sujet | Citation |
|---|---|
| Activité | « We prioritize potential matches who are active, and active at the same time. » |
| Conseil | « The most important factor that can help our users improve their match potential on Tinder is… using the app. » |
| Proximité | « Proximity is a key factor » |
| Swipes | « Likes and Nopes are obviously key pieces of insight » |
| Profil | « Tinder factors in interests and lifestyle descriptions members add to their profiles. » |
| Photos | « We'll suggest profiles with similar photos to ones members have Liked before » |
| Exclusions | « Our algorithm doesn't track social status, religion or ethnicity. » |

Ce que la page ne dit pas : aucun score de désirabilité, aucune description de l'ordre de la pile, aucun poids relatif, aucune mention de Boost ni de limite de swipes.

FAQ Confidentialité, liste fermée des entrées revendiquées : « age, gender, location, interests, and your Like and Nopes ». Exclusion explicite : « Social factors such as race, ethnicity, income and religion do not play any role in our algorithm. »

## Similarité photographique : écart entre l'énoncé et l'ingénierie publiée

Tinder revendique officiellement une recommandation par similarité photographique inter-profils. Les trois billets d'ingénierie publiés sur les photos portent tous sur **les photos de l'utilisateur lui-même** (classement par modèle vision-langage pour Smart Photos, AI Photo Selector sur appareil, Photo Feedback et Smart Photo Ordering), jamais sur l'extraction d'un embedding visuel d'un profil recommandé.

Tinder dispose bien d'embeddings de profils utilisables en kNN depuis ES8, ce qui rend la revendication plausible. **La mise en œuvre technique reste non documentée. Niveau ND.**

## Brevets : famille « Matching process system and method »

Inventeurs : Sean Rad, Todd M. Carrico, Kenneth B. Hoskins, James C. Stone, Jonathan Badeen. Priorité au 19 décembre 2007.

| Numéro | Dépôt | Délivrance |
|---|---|---|
| US9733811B2 | 21 oct. 2013 | 15 août 2017 |
| US9959023B2 | 5 fév. 2016 | 1er mai 2018 |
| US10203854B2 | 3 avr. 2018 | 12 fév. 2019 |
| US11513666B2 | 5 fév. 2019 | 29 nov. 2022 |
| US11733841B2 | 14 août 2017 | 22 août 2023 |
| US12105941B2 | 23 nov. 2022 | 1er oct. 2024 |

**Point décisif sur la portée.** La revendication 1 est quasi identique dans tous les membres et se réduit à quatre étapes triviales. **Rien du contenu technique intéressant ci-dessous n'est revendiqué.** Tout figure dans la description, qui délimite le champ sans être opposable.

Contenu de la description, citations :

- **Attractivité imputée** : « Matching server 20 may be configured to monitor how frequent an entity in pool 30 has been viewed as well as how many times that entity has been part of a result list in order to impute the level of physical attractiveness. » Prévoit aussi une notation manuelle sur une échelle de 1 à 9.
- **Contournement des filtres déclarés** : « matching server 20 may ignore the restrictions if the entity has a high enough attractiveness rating ». C'est le passage le plus significatif : les préférences déclarées peuvent être écrasées par le score d'attractivité.
- **Ordonnancement lexicographique** : points attribués en puissances de deux, par exemple +2^25 si le score de lisibilité du profil dépasse celui de l'utilisateur, +2^24 si l'entité a exprimé une préférence, +2^23 pour une recommandation d'ami. Structure de tri hiérarchisé, pas une somme pondérée continue.
- **Distance arrondie** par tranches de 10 miles.
- **Lisibilité du texte de profil** par Flesch-Kincaid et Gunning Fog, présentée comme proxy d'intelligence.
- **« Fate characteristics »** : initiales communes, lieu de naissance, université, profession des parents.

**Avertissement de méthode.** Le score d'attractivité imputée décrit ici n'est pas la même chose que l'Elo décrit en 2016, même s'ils relèvent de la même famille d'idées. Aucun document Tinder ne confirme qu'un seul de ces mécanismes ait jamais été implémenté. **Niveau B, inventions revendiquées, pas production.**

Confirmation SEC, 10-K FY2025 : « We rely upon a combination of in-licensed third-party and proprietary trade secrets, including proprietary algorithms, and upon patented and patent-pending technologies… relating to our recommendation process systems ».

## Leviers payants qui altèrent l'ordre

Tous les chiffres sont des revendications marketing, **niveau C**.

| Mécanisme | Effet revendiqué | Durée |
|---|---|---|
| Boost | « up to 10x more profile views » | 30 minutes |
| Super Boost | « up to 100x more potential matches » | non indiquée |
| Priority Likes | vos likes vus « before the Likes of non-subscribers » | permanent sous Platinum |
| Super Like | profil priorisé pour le destinataire | par unité |
| Swipe Surge | « activity is up to 15x higher », passage en tête de file | durée de la surge |

Réserves publiées par Tinder : Boost « push your profile to be one of the top profiles **in your area** », ce qui confirme que le Boost opère à l'intérieur du geoshard. Priority Likes « does not guarantee that your Likes will be seen ».

**Non documenté** : si Boost modifie le score ou injecte le profil en tête de piles déjà calculées, le rayon exact, la base de calcul des multiplicateurs 10x, 100x et 15x, la durée de Super Boost.

## Limites de swipes quotidiens

L'existence d'un plafond gratuit est prouvée par la contrepartie payante, Tinder Plus permettant de « Send unlimited daily Likes ». **Le nombre exact, la fenêtre de réinitialisation, la variation par marché et les tests A/B ne sont documentés nulle part.** Les valeurs qui circulent chez les praticiens ne sont adossées à aucune source Tinder. Aucune mesure d'effet du plafond sur le comportement n'est publiée. **Niveau ND.**

## Contraintes de pile hors score et hors paiement

- **Débordement des préférences déclarées** : « We may show you potential matches that are outside of your distance and age preferences, mostly when you run out of recs within these ranges. » Réglage « Dealbreakers ». **Niveau A.**
- **Réapparition de profils déjà swipés** : deux causes seulement admises, compte supprimé puis recréé, swipe sur mauvaise connexion. Tinder ne reconnaît aucun recyclage systématique. Épuisement du vivier : **ND**.
- **Masquage du profil** : une seule cause publiée, absence de photo de visage détectable.
- **Passport** : déplace de geoshard, avec latence documentée jusqu'à 24 heures.

---

# Ce que la littérature indépendante permet de calibrer

## Bruch et Newman 2018, la référence

*Science Advances* 4(8):eaap9815, doi:10.1126/sciadv.aap9815

Plateforme **non nommée**, décrite comme « un site de rencontre populaire et gratuit », algorithme piloté par l'utilisateur ce qui réduit l'interférence du site. États-Unis, **1er au 31 janvier 2014**, quatre aires métropolitaines. Utilisateurs homosexuels et bisexuels retirés (environ 14 %).

| Ville | Hommes | Femmes | Msg. envoyés (moy. H) | Réponses reçues (H) | Réponses reçues (F) |
|---|---|---|---|---|---|
| New York | 44 009 | 50 618 | 23,3 | 15 % | 34 % |
| Boston | 9 113 | 9 355 | 14,6 | 17 % | 37 % |
| Chicago | 28 635 | 23 236 | 19,0 | 18 % | 40 % |
| Seattle | 12 721 | 9 248 | 12,4 | 20 % | 45 % |

**Total 186 935 utilisateurs actifs hétérosexuels. 1 285 568 premiers messages d'hommes, 188 774 de femmes.** Ratio du site environ 55 hommes pour 45 femmes.

Désirabilité calculée par **PageRank** sur le réseau dirigé des messages, rang normalisé de 0 à 1, séparément par ville et par genre. Les auteurs précisent ne pas supposer que les utilisateurs emploient PageRank.

Résultats calibrables :

- **Écart d'aspiration** : les deux genres contactent des partenaires en moyenne environ **25 % plus désirables qu'eux-mêmes**.
- Plus de **80 %** des premiers messages viennent des hommes, taux de réponse moyen des femmes **inférieur à 20 %**.
- **Le taux de réponse aux femmes plus désirables ne dépasse jamais 21 %.**
- Le nombre de contacts initiés décroît quand l'écart visé augmente. Ceux qui visent haut envoient moins de messages, plus longs.
- Âge : désirabilité des femmes décroissante de 18 à 60 ans ; celle des hommes **culmine vers 50 ans**.
- Éducation : pour les hommes, plus d'éducation est toujours plus désirable. Pour les femmes, le premier cycle est le plus désirable, **le troisième cycle est associé à une désirabilité moindre**, à âge contrôlé.

**Aucun coefficient de Gini n'est calculé. Aucun ajustement de loi de puissance.** La distribution est décrite comme « long-tailed » sans exposant. Individu le plus populaire des quatre villes : une femme de 30 ans à New York, **1 504 messages en un mois**.

### Le Gini de 0,58 : à écarter formellement

Le chiffre recirculé d'un Gini de 0,58 sur les likes reçus par les hommes vient d'un **billet Medium non évalué par les pairs** (« Tinder Experiments II », 2015), base **27 femmes interrogées via un faux profil**. **Ne jamais utiliser pour calibrer.**

## Segmentation en sous-marchés

Bruch et Newman 2019, *Sociological Science* 6:219-234, doi:10.15195/v6.a9

Modèle de blocs stochastiques à degrés corrigés. Chaque ville se partitionne en **quatre sous-marchés** (huit si on sépare les genres) selon l'âge et l'ethnicité. **Environ 75 % des interactions réciproques se produisent à l'intérieur d'un même sous-marché.** Le sex-ratio varie fortement entre sous-marchés.

## Taux de match sur pile de swipe

Tyson et al. 2016, ASONAM, doi:10.1109/ASONAM.2016.7752275

14 profils sondes, 480 000 profils collectés, Londres et New York. Photos exclusivement de personnes blanches, choix explicite pour « éviter les complexités introduites par l'homophilie raciale ».

- Taux de match sondes **masculines 0,6 %**, **féminines 10,5 %**
- 21 % des matchs féminins envoient le premier message contre 7 % des matchs masculins
- Délai médian avant premier message : hommes 2 minutes, femmes 38 minutes
- Longueur médiane du premier message : **hommes 12 caractères, femmes 122 caractères**. 25 % des messages d'hommes font moins de 6 caractères
- **36 % des utilisateurs ont une bio vide.** Les profils avec bio obtiennent environ quatre fois plus de matchs féminins
- Effet photo : 44 matchs avec une photo contre 238 avec trois photos

Limite déclarée par les auteurs : « nous avons traité Tinder comme une boîte noire ».

## Données comportementales françaises, Meetic 2014

Bergström 2018, *RFS* 59(3):395-422, doi:10.3917/rfs.593.0395

401 208 profils actifs, **25 millions de métadonnées de messages** (jamais le contenu).

- **90 % des premiers contacts sont initiés par des hommes**
- **77 % des réponses sont envoyées par des femmes**
- Taux de réponse : **16 % des tentatives masculines, 44 % des tentatives féminines**
- Effet d'âge sur le taux de réponse reçu : **12 % pour les 18-24 ans**, 30 % pour les 50-59 ans. **Les jeunes hommes obtiennent le plus faible taux de réponse de tout le site**
- Part des interactions initiées par la femme : **17 % chez les 18-24 ans**, 58 % chez les 60-70 ans

Falsifications mesurées : taille déclarée +2 cm, poids -2 kg pour les hommes et -5 kg pour les femmes. Pics d'années de naissance sur les chiffres ronds.

## Biais de position, réutilisable directement

Tomita, Togashi, Hashizume, Ohsaka 2023, RecSys, doi:10.1145/3604915.3608774

Modèle fondé sur la position (PBM), fonction d'examen v(k) testée sous trois formes : **v(k)=1/k**, **v(k)=1/log(1+k)**, **v(k)=1/exp(k-1)**. Service de rencontre japonais non nommé, sous-échantillons 200×200 et 1 000×1 000.

**Ces trois formes sont directement réutilisables comme hypothèses de position dans la pile simulée.**

## Ce que pèse le message, une fois l'exposition contrôlée

C'est le résultat le plus important de tout le dossier pour cette étude.

Bruch et Newman 2018, tables S3 à S6 du matériel supplémentaire. Statistiques z absolues, ville de référence Boston :

| Terme | Femmes, z | Hommes, z |
|---|---|---|
| **Écart de désirabilité** | **14,41** | **21,39** |
| Écart de désirabilité au carré | 2,24 | 6,26 |
| **Nombre de mots** | **1,26** | **1,44** |
| Nombre de mots × Seattle | 2,17 | 5,21 |

**Dans la ville de référence, le nombre de mots n'a pas d'effet statistiquement détectable sur la probabilité de réponse, ni pour les hommes ni pour les femmes.** L'écart de désirabilité porte des z de 14 à 21, soit un ordre de grandeur au-dessus.

Table S6, fraction de mots positifs (LIWC) : pour les hommes, coefficient -0,006, z = 3,83, donc **effet négatif significatif**. Les auteurs écrivent : « les messages positifs sont plutôt négativement associés aux taux de réponse pour les hommes ».

Table S3 : les deux genres écrivent des messages **jusqu'à deux fois plus longs** aux partenaires plus désirables. Les femmes augmentent leur usage de mots positifs vers les partenaires plus désirables, **les hommes le diminuent**.

**Conclusion défendable, à inscrire dans la discussion.** Une fois la position dans la hiérarchie de désirabilité contrôlée, le contenu observable du message contribue marginalement à la probabilité de réponse. Le prédicteur dominant est la position relative. Cela ne rend pas l'étude vaine, cela en déplace l'objet : la question n'est pas si les messages générés « marchent », mais ce que le modèle produit quand on lui demande de les faire marcher.

Corollaire, Bapna et al. 2016, doi:10.1287/mnsc.2015.2301 : expérience randomisée sur 100 000 nouveaux utilisateurs, 50 000 dotés de la navigation anonyme. Les utilisateurs anonymes consultent plus de profils mais **finissent avec moins de matchs**, le mécanisme causal étant le signal faible que constitue la visite de profil visible. Une part substantielle du résultat se joue **avant tout message**.

## Modèles de marché utiles

- **Kanoria et Saban 2021**, doi:10.1287/mnsc.2020.3794. Dans un marché déséquilibré, la plateforme doit forcer le côté court à initier et interdire au côté long de le faire. Cacher l'information sur la qualité améliore le bien-être. Justification théorique du design Bumble.
- **Jung et al. 2022**, doi:10.1287/isre.2021.1028. Expérience de terrain randomisée : augmenter la capacité de choix des hommes maximise l'engagement, mais **augmenter celle des femmes est le levier le plus efficace pour augmenter le nombre de matchs**. Effet de congestion asymétrique par genre.
- **Halaburda et al. 2018**, doi:10.1287/mnsc.2017.2797. Effet de choix positif contre effet de concurrence négatif du même côté du marché. Explique la coexistence de plateformes à philosophies opposées.

## Simulations existantes

**Aucun simulateur d'application de rencontre à pile de swipe, publié, calibré empiriquement et à code ouvert, n'existe.** Le plus proche est Ionescu, Hannák et Joseph 2021 (FAccT, doi:10.1145/3442188.3445904), qui déclare explicitement l'absence de calibration empirique et modélise le filtrage utilisateur, **pas la distribution d'exposition produite par un recommandeur**.

Das et Kamenica 2005 (IJCAI) simule 5 hommes et 5 femmes sous **hypothèse de classement commun**, exactement l'hypothèse que Bruch et Newman valident partiellement mais que Lewis et Xie contestent.

C'est un espace ouvert. Un simulateur calibré serait une contribution en soi.

## Biais transversal des sources, à déclarer dans toute publication

Bruch et Newman 2018 et 2019, Hitsch et al. 2010, Anderson et al. 2014, Chen et al. 2023, Jung et al. 2022, Bapna et al. 2016 reposent tous sur des **plateformes non nommées et des jeux de données propriétaires non reproductibles**. Le seul jeu public de taille comparable est **Líbímseti.cz** (Tchéquie, 220 970 utilisateurs, 17,4 millions d'interactions), plateforme web pré-swipe, un seul pays.

**Biais temporel** : les données structurantes de Bruch et Newman datent de **janvier 2014**, sur un site web à messagerie libre, antérieur à la généralisation du swipe. Transposer leur hiérarchie de désirabilité à une pile Tinder de 2026 est une extrapolation, pas une mesure.
