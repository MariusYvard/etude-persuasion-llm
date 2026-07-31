# Stratégie documentaire

Ce fichier reconstitue, après coup, la stratégie de recherche documentaire des neuf dossiers de `sources/` (01 à 09) et de `bibliographie.bib`. Il ne rejoue pas cette recherche et n'ajoute aucune source nouvelle. Il inventorie ce que les dix fichiers montrent avoir été effectivement fait, dans l'esprit d'un diagramme PRISMA adapté à une revue non systématique menée par un seul document, pas par un comité.

Méthode de reconstitution : lecture intégrale des neuf dossiers, de `bibliographie.bib` et de `protocole/preenregistrement.md` (dont les sections 4 et 11, et par nécessité de contexte les sections 1, 3, 6, 7, 10 et 12), le 31 juillet 2026. Chaque effectif cité ci-dessous a été recompté directement dans les fichiers, à la main puis par un script de contrôle pour la bibliographie. Quand un effectif ne pouvait pas être établi, cela est écrit explicitement plutôt qu'estimé. Toute affirmation de ce document est vérifiable contre le fichier qu'elle cite.

## 1. Objet et périmètre

### 1.1 Objet général de la recherche documentaire

Le préenregistrement (section 1) fixe l'objet de l'étude : mesurer ce qu'un modèle de langage produit quand on lui demande de rédiger un message d'ouverture de rencontre sous des consignes d'optimisation croissantes, face à des profils fictifs porteurs de marqueurs de vulnérabilité et rattachés à des contextes culturels contrastés. La recherche documentaire sert cet objet de deux façons : fournir les faits de calibrage (démographie, comportement, cadre légal, normes sociales) qui rendent les personas fictives plausibles et notables, et fournir la taxonomie qui sert de grille de notation aux messages produits.

Ce que la recherche documentaire ne visait pas, et le dit explicitement dans les dossiers : mesurer l'efficacité réelle des messages générés (protocole, section 1, au motif que la littérature indépendante montre que le contenu du message pèse marginalement une fois la désirabilité contrôlée, dossier 02) ; collecter des données de personnes réelles ou accéder à une plateforme de rencontre (protocole, section 10, cadre éthique : aucun compte créé, aucun profil consulté, aucune collecte automatisée) ; produire ou reproduire des scripts de manipulation prêts à l'emploi (dossier 04, en tête : "Aucun script, aucun modèle de message, aucune formulation prête à l'emploi n'est reproduit ici, et le protocole interdit d'en publier").

### 1.2 Périmètre déclaré, dossier par dossier

| Dossier | Ce qu'il cherchait | Ce qu'il excluait explicitement |
|---|---|---|
| 01, surface produit Tinder | Les champs de profil et fonctionnalités officiellement documentés par Tinder, ce qui est visible avant et après le match, la vérification d'identité | Tout ce qui n'est pas documenté officiellement par Tinder. Le dossier se clôt sur une liste explicite de douze points "à ne jamais combler par extrapolation" |
| 02, algorithme et exposition | L'architecture de recommandation publiée par Tinder (documentation, blog d'ingénierie, brevets), et la littérature académique indépendante permettant de calibrer le poids du message une fois l'exposition contrôlée | Toute affirmation sur un mécanisme d'attractivité ou de score non confirmée en production. Définit lui-même trois niveaux de preuve propres au dossier (voir section 4) |
| 03, comportement et messages | Démographie de référence, contenu et poids réel des bios, asymétries de genre, structure des messages d'ouverture, classement des marqueurs de vulnérabilité, ordres de grandeur de la fraude sentimentale | Tout panel de plus de quarante ans, écarté du protocole et signalé comme tel. Le dossier fixe lui-même son périmètre : 18 à 35 ans |
| 04, corpus de conseils et LLM | La cartographie des sources de conseil en séduction, la taxonomie des archétypes qui sert de grille de notation, l'état de l'adoption des LLM dans la rencontre et la littérature sur la détection et la confiance | Toute reproduction de script ou de formulation prête à l'emploi, interdite par le protocole |
| 05, zone Europe | Prévalence, contenu des bios, comportement mesuré, cadre légal et sécurité pour l'Europe, avec le motif documenté de la scission entre Europe du Nord-Ouest et Europe du Sud | L'Europe centrale et orientale, pour documentation quasi nulle. Toute revendication de fidélité de registre de bio pour l'italien et le portugais |
| 06, zone Amérique latine | Prévalence par pays (Brésil, Mexique, Colombie, Argentine), présentation de soi (classe sociale, religiosité), sécurité et cadre légal | Toute donnée comportementale (taux de match, de swipe, de réponse, longueur des messages), déclarée absente pour toute la zone. Toute mesure de codes régionaux internes |
| 07, zone Asie du Sud | Déséquilibre de genre, marché matrimonial parallèle, rapport entre rencontre en ligne et mariage arrangé, codes sociaux visibles dans un profil, langue, sécurité et cadre légal | L'usage rural (toutes les données opposent Tier 1 aux Tier 2 et 3, ce qui reste une segmentation urbaine). Le Pakistan, le Bangladesh et le Sri Lanka, déclarés "quasi vides" documentairement |
| 08, zone Asie du Sud-Est | Prévalence par pays, cadre religieux et normatif pays par pays, cadre répressif et statut LGBT, langue et registre, arnaques et sécurité | Le traitement de la zone comme un bloc ("règle absolue : ne jamais traiter l'Asie du Sud-Est comme un bloc"). Tout corpus de bios, absent pour les six pays couverts |
| 09, zone Asie de l'Est | Prévalence, raisons documentées de la faiblesse de Tinder face aux acteurs locaux, normes de présentation de soi (bio japonaise, certification coréenne), vérification d'identité légale, genre et sécurité | La Chine continentale comme zone de persona, Tinder n'y étant pas exploité selon les sources consultées. Toute revendication de fidélité de registre pour le coréen et le chinois traditionnel |

### 1.3 Ce que l'ensemble de la recherche documentaire ne cherchait pas

Trois exclusions transversales, données par les dossiers eux-mêmes plutôt que déduites : aucune tentative de mesurer l'efficacité réelle d'un message de rencontre (l'étude entière renonce à ce terrain, dossier 02) ; aucune recherche destinée à alimenter un outil de production de messages, le dossier 04 refusant explicitement cet usage ; aucune collecte de littérature sur des populations hors de la tranche 18 à 35 ans sauf mention explicite de l'écart (dossier 03).

## 2. Sources interrogées

Cette section recense ce que les dix fichiers montrent avoir été effectivement consulté. Elle est représentative et non exhaustive : les neuf dossiers restent le registre complet, cette liste n'en est qu'un inventaire par catégorie, avec les périodes couvertes quand les dossiers les donnent.

### 2.1 Bases et portails académiques

- **HAL** (Hyper Articles en Ligne). Interrogée sur les bios de rencontre en français, sans résultat (dossier 05).
- **CiNii** (Japon). Interrogée sur le corpus linguistique des bios japonaises de rencontre, sans résultat exploitable (dossier 09).
- **DOAJ, OpenAIRE, Crossref**. Interrogées pour une étude comparative européenne multi-pays sur les applications de rencontre. Aucune trouvée (dossier 05).
- **Naver, Daum** (portails coréens, pas des bases académiques mais interrogés comme sources de corpus). Ne renvoient que des blogs personnels sans corpus, sur le registre des bios coréennes (dossier 09, préenregistrement section 4.2).
- **KCI, RISS** (Corée), **Airiti** (Taïwan), **CNKI** (Chine). Explicitement déclarées **non interrogées** par le dossier 09, à la différence de CiNii. C'est un manque déclaré, pas un résultat de recherche négatif.
- **법제처, easylaw.go.kr** (portails juridiques coréens). Accès automatisé tenté et bloqué (dossier 09).
- **SciELO**. Consultation tentée pour vérifier un effectif d'échantillon (Araújo et Rosas 2024), en erreur 403 au moment de la lecture (dossier 06).
- **datatilsynet.no** (autorité norvégienne de protection des données). Consultation tentée, en erreur 500 (dossier 05).
- Pages de galley d'un article de l'*European Journal of Humour Research* (corpus interculturel de 455 profils). Deux URL en 404 (dossier 05).
- SlideShare (support de conférence TinVec 2017). Page inaccessible en accès direct, chiffres repris de seconde main (dossier 02).
- Les 122 références de `bibliographie.bib` sont, selon la convention énoncée en tête du fichier, celles "dont les métadonnées ont été vérifiées". Le mécanisme de vérification n'est pas détaillé au-delà de cette phrase.

### 2.2 Registres et enquêtes statistiques publiques, nationales et internationales

Regroupe ici, faute d'une frontière nette dans les dossiers entre registre administratif et enquête probabiliste publique.

- **Eurostat**, code `yth_demo_030` (âge de départ du foyer parental), année de référence 2025, source EU-LFS ; requêtes pays par pays après qu'une requête en lot ait renvoyé des appariements erronés (dossier 05, préenregistrement section 4.1). Également `demo_find` (naissances hors mariage, référence 2024), `hlth_ehis_al1e` (consommation d'alcool, référence 2019), `ilc_lvps08` (part des 25-29 ans vivant chez leurs parents, série 2007-2024, utilisée pour la Suisse).
- **Eurostat**, enquête TIC ménages, et **Eurobaromètre** : vérifiés pour une variable de prévalence de l'usage des applications de rencontre. Absente des deux (dossier 05).
- **CBOS** (Pologne), **Internetstiftelsen** (Suède), **INE** (Espagne), **ISTAT** (Italie), **SCB** (Suède) : instituts nationaux "vérifiés sans résultat" (dossier 05).
- **Office fédéral de la statistique** (Suisse), Enquête sur les familles et les générations, éditions 2018 (16 815 participants sur 36 029 invités) et 2023 (18 317 entretiens, terrain avril à juillet 2023) (dossier 05, préenregistrement section 6).
- **Pew Research Center** : États-Unis, terrain 5 au 17 juillet 2022, n = 6 034 (dossier 03) ; terrain 16 au 28 octobre 2019, n = 4 860 (préenregistrement section 7) ; Inde, terrain 17 novembre 2019 au 23 mars 2020, n = 29 999 (dossier 07).
- **SSRS Opinion Panel**, terrain 7 au 9 février 2025, n = 2 016 (dossier 03).
- **Ofcom** et Ipsos iris, données de mai 2024 (dossier 03).
- **Match Group**, dépôts 10-K (SEC), exercice 2025 (dossiers 02, 03, 09).
- **Ined**, enquête Envie, terrain novembre 2022 à juillet 2023, n = 10 021 (dossier 05). **Ined-Insee**, enquête Épic, 2013-2014, n = 7 825 (dossier 05).
- **Inserm, Santé publique France, ANRS-MIE**, enquête CSF-2023, terrain novembre 2022 à décembre 2023, n = 31 518 (dossier 05).
- **Insee**, état civil 2024 (naissances hors mariage) (préenregistrement section 7).
- **Recensement du Canada 2021** (union libre, exhaustif) et **American Community Survey 2023** (États-Unis) (préenregistrement section 7).
- **IHDS-II**, Inde, terrain 2011-2012, plus de 42 000 foyers ; **NFHS-5**, Inde, terrain 2019-2021, n = 57 693 couples et n = 272 752 pour la consommation d'alcool (dossier 07).
- **INEGI**, enquête EDER 2025, Mexique, terrain mai à septembre 2025, n = 33 000 logements (dossier 06).
- **IPSS**, 第16回出生動向基本調査, Japon, terrain 2021, 14 011 questionnaires distribués et 7 826 valides ; **こども家庭庁**, terrain 8 au 22 juillet 2024, n = 20 000 ; **リクルートブライダル総研**, terrain 24 mai au 4 juin 2024, n = 50 000 (dossier 09).
- **와이즈앱·리테일** et **와이즈앱** (Corée, audience Tinder, juillet 2025 et août 2023) ; **마크로밀 엠브레인 트렌드모니터**, terrain 28 au 30 octobre 2024, n = 1 200 ; **대학내일20대연구소**, terrain 14 au 18 février 2025, n = 500 ; **MMD研究所**, terrain 19 au 24 septembre 2025, n = 30 000 (dossier 09).
- **FTC** (données 2022, 2023, 2025) et **FBI IC3** (données 2025), signalements de fraude sentimentale (dossier 03).
- **YouGov**, Indonésie février 2025 n = 2 011, Singapour janvier 2024 n = 1 034 et février 2025 n = 1 061, Thaïlande septembre 2017 n = 2 720 ; **Populix**, Indonésie janvier 2024, n = 1 165 (dossier 08).
- **ILGA-Europe** Rainbow Map 2026 ; **FRA** LGBTIQ Survey III, 2023, n = 100 577 (dossier 05).
- **Statista Consumer Insights**, Taïwan, terrain 10 au 31 août 2024, n = 3 472, sous péage (dossier 09) ; **Statista**, classements Philippines et Malaisie, sous péage (dossier 08).
- **Similarweb**, relevé du classement Google Play, 26 juillet 2026 (dossier 05).
- **Australian Institute of Criminology**, n = 9 987 (dossier 05, cadre déclaré non transposable numériquement).
- **United States Institute of Peace**, 2025, estimation des sommes détournées par les réseaux d'escroquerie d'Asie du Sud-Est (dossier 08).
- **ISDP**, juin 2025, crimes sexuels numériques en Corée du Sud (dossier 09).

### 2.3 Textes juridiques et réglementaires

Règlement Général sur la Protection des Données, articles 7.4 et 9(1) ; Community Guidelines et Policies Tinder (dossier 01). Legge 76/2016 (Italie, union civile) ; Ν. 5089/2024 (Grèce, mariage civil, en vigueur depuis le 16 février 2024) ; Uniform Civil Code of Uttarakhand Act 2024 (Inde, cohabitation, en vigueur depuis le 27 janvier 2025) ; 23 U.S.C. § 158 (États-Unis, seuil de 21 ans) (préenregistrement section 7). Loi n° 1/2023, code pénal indonésien, articles 411 et 412, en vigueur depuis le 2 janvier 2026 ; Qanun Jinayat n° 6/2014 (Aceh) ; enactments syariah malaisiens (Selangor 1995, Melaka 1991, Territoires fédéraux 1997, Kelantan 2019 déclaré inconstitutionnel en février 2024) ; Code pénal fédéral malaisien, sections 377A, 377B, 377D ; Alcoholic Beverage Control Act B.E. 2551 (Thaïlande) ; loi vietnamienne sur le mariage et la famille de 2014 (dossier 08). 出会い系サイト規制法 (平成15年法律第83号, 2003, révisée en 2008) et son règlement d'application ; article 750 du Code civil japonais ; 大正11年法律第20号 (âge légal de consommation d'alcool) (dossier 09, préenregistrement section 7). Ley Olimpia (Mexique) ; PL 2112/2023 (Brésil, non encore adopté) ; article 171 du Code pénal brésilien (dossier 06). Règlement sur les services numériques (DSA) et règlement sur les marchés numériques (DMA) de l'Union européenne, vérifiés au 24 juillet 2026 (dossier 05).

### 2.4 Enquêtes et communiqués d'entreprise

Tinder (centre d'aide, Community Guidelines, salles de presse par pays, page "Powering Tinder", Tinder Tech Blog et lifeattinder.com) ; Hinge (Hinge Labs) ; Bumble ; Match Group (communications financières au-delà du 10-K) ; QuackQuack, Aisle, TrulyMadly, Woo (Inde) ; PoderData, Panorama Mobile Time et Opinion Box, Sensor Tower (Brésil) ; Mandarina In (Mexique, commanditée par Tinder) ; Statista Brand KPIs (Mexique) ; .CO Internet SAS et Centro Nacional de Consultoría (Colombie) ; Rizz, YourMove AI (applications tierces d'assistance à la rédaction) ; Ifop pour Tinder via Ogilvy, terrain 30 avril au 5 mai 2026, n = 1 000 (dossier 05) ; Norton, terrain 5 au 16 décembre 2024, n = 1 001 ; Singles in America (Match, Kinsey Institute, terrain Dynata), n = 5 001 (dossier 04) ; Opinium pour Tinder, terrain 6 au 18 mars 2024, n = 8 000 (dossier 06) ; Dataxet Sonar (Thaïlande, mai 2024) ; Decision Lab (Vietnam, 2022, n = 1 012) ; McAfee 2024 (Inde) ; Forbes Health, Forbes India ; GlobalWebIndex 2020 (Thaïlande) ; Nyle (Japon, terrain 8 au 13 février 2022, n = 400) ; ワクワクコミュニケーションズ (Japon, janvier 2026, n = 6 981).

### 2.5 Presse

Fast Company (Austin Carr, 11 janvier 2016, seule source où l'existence du score Elo est confirmée par le PDG de Tinder) ; TechCrunch ; Axios ; Business Standard ; Global Dating Insights ; MIT Technology Review (27 mars 2025) ; Cybernews (enquête sur la fuite FlirtAI, juillet 2025) ; Electronic Frontier Foundation (21 juillet 2025) ; Taiwan News (novembre 2022) ; couverture du Bloomberg Tech Summit (10 mai 2024) ; El Colombiano (juillet 2025, cité pour être explicitement écarté, voir section 4).

### 2.6 Autres sources : brevets, décisions de justice, organismes non gouvernementaux

Famille de brevets Rad et al., "Matching process system and method", priorité du 19 décembre 2007, six continuations jusqu'à US12105941B2 délivré le 1er octobre 2024 (dossier 02). Cour d'appel écossaise, annulation en 2020 de la condamnation d'Adnan Ahmed (dossier 04). Southern Poverty Law Center, UCLA Center for the Study of Women (qualifications institutionnelles des communautés de séduction, dossier 04). Forbrukerrådet (Norvège, plainte contre Grindr, 14 janvier 2020) ; noyb (signalement contre Bumble, 26 juin 2025) (dossier 05). Committee on the Empowerment of Women, quatrième rapport, Inde, déposé le 23 mars 2026 (dossier 07). Pakistan Telecommunication Authority (blocage de Tinder et d'autres applications, 1er septembre 2020) (dossier 07).

## 3. Équations de recherche

Aucun des dix fichiers ne conserve de requête verbatim (aucune syntaxe booléenne, aucun opérateur de champ, aucune capture d'écran de résultats de recherche). Ce qui est écrit est une description narrative : quelle base, sur quel sujet, avec quel résultat. Le tableau ci-dessous reconstitue, à partir de cette description, la logique de croisement de termes quand elle est explicite. Pour tout le reste de la bibliographie, aucune équation n'est reconstituable et ce document ne cherche pas à en fabriquer une.

### 3.1 Requêtes reconstituables

| Base | Thème | Croisement de termes décrit dans le dossier | Langue | Résultat | Source |
|---|---|---|---|---|---|
| HAL | Emoji dans les bios de rencontre | "emoji" croisé avec "rencontre" | Français | Zéro résultat pertinent | Dossier 05 |
| HAL | Corpus de profils ou d'annonces | "analyse de corpus" croisée avec "profils" ou "annonces" | Français | Zéro résultat pertinent | Dossier 05 |
| HAL | Registre des bios | Recherche en titre, "bio" croisée avec "Tinder" | Français | Zéro résultat pertinent | Dossier 05 |
| DOAJ, OpenAIRE, Crossref | Étude comparative des applications de rencontre en Europe | "étude comparative" et "applications de rencontre" et une dimension multi-pays ou européenne (langue de recherche non précisée par le dossier) | Non précisée | Aucune étude trouvée | Dossier 05 |
| CiNii | Corpus linguistique des bios japonaises | Non précisé au-delà du sujet | Japonais (base japonaise) | Rien de renvoyé | Dossier 09 |
| Naver, Daum | Registre des bios coréennes | Non précisé au-delà du sujet | Coréen | Seulement des blogs personnels sans corpus | Dossier 09, préenregistrement section 4.2 |
| 법제처, easylaw.go.kr | Régime légal coréen des applications de rencontre | Accès automatisé, terme non précisé | Coréen | Accès bloqué | Dossier 09 |

### 3.2 Ce qui n'est pas reconstituable, et où

Pour l'écrasante majorité du corpus, aucune équation, même approximative, n'est reconstituable, et ce document le déclare plutôt que d'en inventer une :

- Les **74 références transversales** de `bibliographie.bib` (sections 1 à 8 et 14, thèmes désirabilité et appariement, messages d'ouverture, bios et tromperie, psychologie et vulnérabilité, fraude sentimentale, corpus de conseils, LLM, recommandeurs) ne portent trace, dans aucun des dossiers 01 à 04, d'une base interrogée, d'un terme de recherche ni d'une date de recherche. Elles apparaissent comme déjà identifiées, citées par DOI.
- Les **23 références** des sections "Zone Asie du Sud", "Zone Asie du Sud-Est" et "Zone Asie de l'Est" de `bibliographie.bib` (dossiers 07, 08, 09) ne sont précédées d'aucune description de recherche dans ces trois dossiers, hormis les cas listés en 3.1 concernant explicitement des absences (CiNii, Naver, Daum, KCI, RISS, Airiti, CNKI).
- Aucun moteur ou base généraliste (à titre d'exemple : Google Scholar, PubMed, Scopus, Web of Science, Semantic Scholar) n'est nommé dans aucun des neuf dossiers ni dans le préenregistrement. Le mécanisme de découverte de la majorité de la bibliographie n'est donc pas documenté, ni la date à laquelle il aurait eu lieu.
- Le dossier 04 (corpus de conseils) ne décrit aucune recherche documentaire structurée pour son propre objet (Reddit, TikTok, Instagram, SEO marchand) : les effectifs d'abonnés ou de vues qu'il cite proviennent de sources déjà identifiées, sans description de la façon dont elles ont été trouvées.
- Le dossier 02 (algorithme) construit sa matière à partir de sources nommément identifiées (documentation Tinder, brevets, un article de presse) sans décrire de recherche antérieure à leur identification.

## 4. Critères d'inclusion et d'exclusion

### 4.1 Deux grilles de niveaux de preuve coexistent, avec des définitions différentes

Le corpus emploie deux grilles distinctes, toutes deux notées A, B, C, ND. Le fait qu'elles portent les mêmes lettres sans partager les mêmes critères n'est signalé nulle part dans les dossiers.

**Grille 1, définie dans le dossier 02** ("Trois niveaux de preuve, à ne jamais confondre") : Niveau A, documentation officielle Tinder (page d'aide, blog d'ingénierie, dépôts SEC) ; Niveau B, brevets ("inventions revendiquées entre 2007 et 2024. Rien n'indique que ce qui figure dans la description tourne en production") ; Niveau C, presse et praticiens growth. Cette grille est reprise implicitement dans le dossier 01 (tags A et ND par champ de profil, C pour les métriques revendiquées par Tinder sans audit).

**Grille 2, définie dans le préenregistrement, section 7** (grille du canal 2 de transposition normative) : "A échantillon probabiliste, registre administratif exhaustif, corpus annoté ou texte juridique en vigueur ; B enquête d'entreprise ou échantillon de convenance ; C presse citant des données sans méthode publiée ; ND non documenté."

Ces deux grilles divergent précisément sur la lettre B (brevets non confirmés en production dans la grille 1, enquêtes d'entreprise ou échantillons de convenance dans la grille 2) et l'application de la grille 2 elle-même n'est pas homogène : les dossiers 05, 06 et 07 notent C plusieurs enquêtes commanditées par une entreprise (Ifop pour Tinder, dossier 05 ; Mandarina In pour Tinder, dossier 06 ; QuackQuack et Tinder Inde/OnePoll, dossier 07, explicitement qualifiées "enquête de communication d'entreprise" et notées C), alors que la définition du canal 2 assigne B à ce type de source. Le dossier 09 note à l'inverse B deux enquêtes sectorielles commerciales de taille comparable (リクルートブライダル総研, n = 50 000 ; 마크로밀 엠브레인, n = 1 200). Aucun des dossiers n'explicite le critère qui distingue une enquête d'entreprise notée B d'une enquête d'entreprise notée C : la seule hypothèse qui se dégage des cas observés, sans être formulée nulle part, est que les enquêtes internes à la plateforme elle-même sans méthode publiée tendent vers C, et les enquêtes de cabinets sectoriels tiers avec effectif et terrain déclarés tendent vers B.

Un défaut de forme s'ajoutait pour la grille 2 elle-même : les tableaux "Amérique du Nord" et "Asie du Sud" ne comportaient pas de colonne Niveau, alors que les cinq autres en comportent une par ligne.

**Corrigé le 31 juillet 2026, à la suite de ce document.** Les deux tableaux ont reçu leur colonne Niveau. Surtout, le préenregistrement (section 7) énonce désormais la règle qui manquait : la grille du canal 2 est la seule qui gouverne le catalogue et l'analyse, celle du dossier 02 reste valide dans son propre périmètre, et un tableau de départage à trois cas tranche le classement des enquêtes d'entreprise entre B et C. Les constats de cette section décrivent donc l'état antérieur à cette correction.

### 4.2 Grille de niveaux de preuve, telle qu'employée dans les dossiers

| Niveau | Définition (grille du canal 2, préenregistrement section 7) | Emploi observé dans les dossiers |
|---|---|---|
| A | Échantillon probabiliste, registre administratif exhaustif, corpus annoté ou texte juridique en vigueur | Pew, Eurostat, IHDS-II, NFHS-5, recensements, Ined, Insee, IPSS, こども家庭庁, textes de loi en vigueur |
| B | Enquête d'entreprise ou échantillon de convenance | Selon les dossiers, soit des enquêtes sectorielles commerciales avec effectif et terrain déclarés (dossier 09), soit des échantillons universitaires de convenance (Castro 2020, Erevik 2020) |
| C | Presse citant des données sans méthode publiée | Communiqués d'entreprise sans audit (métriques Tinder, dossier 01), enquêtes commanditées par la plateforme elle-même (dossiers 05, 06, 07), presse spécialisée |
| ND | Non documenté | Registre des bios coréennes et taïwanaises, limite de caractères de la bio Tinder, plusieurs statistiques de sécurité par pays |

### 4.3 Critère d'âge

Le dossier 03 fixe le périmètre à 18-35 ans et déclare explicitement écarter tout panel reposant sur plus de 40 ans. Ce critère n'est cependant pas appliqué de façon stricte partout : plusieurs sources retenues débordent la tranche et le disent elles-mêmes (corpus suédois LGBTQ, âges 16 à 77 ans, moyenne 36 ans, dossier 05 ; Palumbo 2019, 30-50 ans, dossier 06 ; IHDS-II, femmes 15-49 ans, dossier 07). Dans ces cas, les dossiers signalent le débordement et restreignent la portée de la source à un mécanisme plutôt qu'à une fréquence de population, sans l'exclure entièrement.

### 4.4 Règle de récence appliquée le 30 juillet 2026

Le préenregistrement (limite 18, section 11) documente un balayage ciblé, mené le 30 juillet 2026, des collectes postérieures à juillet 2024. Ce n'est pas un filtre de recency général appliqué à toute la bibliographie : c'est une vérification de mise à jour, portant sur deux questions précises. Premièrement, si une donnée plus récente que Bruch et Newman 2018 (données de janvier 2014) avait été publiée sur la contribution du contenu du message une fois la désirabilité contrôlée : la réponse documentée est non, les trois publications de 2025-2026 qui en ont l'apparence reposant en réalité sur des données de 2016, 2017 et 2022, et aucun corpus de messages n'a été ouvert depuis Tyson et al. (2016). Deuxièmement, si une donnée comportementale postérieure à juillet 2024 existait pour l'Amérique latine, l'Asie du Sud, l'Asie du Sud-Est ou l'Europe du Sud : la réponse documentée est non pour les quatre zones.

En dehors de ce balayage ciblé, aucune règle de récence n'exclut une source de la bibliographie du seul fait de son ancienneté : des références fondatrices datent de 2007 (priorité du brevet Rad et al.), 2008 (Toma et al., corpus Match.com de Bergström), 2009 (analyse OkCupid de Christian Rudder, non publiée par les pairs mais retenue comme la source la plus citée du corpus de conseil), 2010 (Hitsch, Hortaçsu et Ariely) et 2013-2014 (Bruch et Newman). Ces choix sont assumés et déclarés comme limite plutôt que dissimulés.

### 4.5 Exclusions explicitement motivées, relevées dans les dossiers

Chaque exclusion suivante est nommée avec son motif par le dossier qui la mentionne. Il n'existe pas de dénominateur global (aucun total de sources dépistées puis écartées n'est enregistré) : ce sont des rejets ponctuels rencontrés au fil de la construction des dossiers, pas le résultat d'un tri systématique documenté.

- Coefficient de Gini de 0,58 sur les likes reçus par les hommes, issu d'un billet Medium non évalué par les pairs (base de 27 femmes via un faux profil) : "à écarter formellement", "ne jamais utiliser pour calibrer" (dossier 02).
- Chiffre de "78 % de la Gen Z en burnout applicatif" : enquêtes commanditées sans méthodologie publiée, "écartés" (dossier 03).
- TenLove, présentée par des sources tierces comme colombienne : en réalité chilienne et ciblant les plus de 50 ans, "hors périmètre" (dossier 06).
- Article d'El Colombiano de juillet 2025 sur les différences entre villes colombiennes : fondé sur une analyse produite par ChatGPT et non sur des données de plateforme, ce que l'article indique lui-même, cité comme "cas exemplaire à écarter" (dossier 06).
- Listes d'argot "geração Z" de la presse brésilienne et articles de presse espagnole sur "le langage de Tinder" : "éditoriaux, non issus de corpus... Ne pas les traiter comme sources" (dossier 06).
- Chiffres de lassitude relayés par la presse brésilienne et colombienne, en réalité issus de Forbes Health 2025 sur échantillon états-unien : "non transposables" (dossier 06).
- Item de rythme de rencontre en Inde (38 % des utilisateurs Tier 2 et 3), sorti du volet confirmatoire faute d'année de collecte et de méthodologie fiable, versé en exploratoire (préenregistrement, section 7).
- Papier Heliyon sur Bumble en Inde : porte un corrigendum publié en 2025, "ne pas le citer sans lire le corrigendum" (dossier 07). Non retiré mais fortement conditionné et absent de `bibliographie.bib`.
- Application Chatfish (détection de messages rédigés par IA) : "précision non établie" (dossier 04), mentionnée sans être retenue comme preuve de fiabilité d'une contre-mesure.

## 5. Diagramme de flux en texte

Un diagramme PRISMA classique suppose des effectifs à chaque étape (identifiés, dédupliqués, criblés, exclus avec motif, inclus). Ces effectifs intermédiaires ne sont enregistrés dans aucun des dix fichiers : il n'existe pas de trace du nombre de sources repérées avant sélection. Ce qui suit n'est donc pas ce diagramme complet, mais les seuls effectifs réellement établissables à partir des fichiers.

### 5.1 Bibliographie finale

`bibliographie.bib` contient **122 entrées** (compté directement dans le fichier, deux méthodes indépendantes, même résultat), réparties par type : 100 `@article`, 9 `@inproceedings`, 6 `@misc`, 3 `@techreport`, 2 `@book`, 1 `@incollection`, 1 `@patent`.

Répartition par les quatorze sections thématiques du fichier lui-même :

| Section du fichier | Références |
|---|---|
| 1. Désirabilité, appariement, structure de marché | 14 |
| 2. Messages d'ouverture et interaction | 5 |
| 3. Bios, présentation de soi, tromperie | 13 |
| 4. Psychologie, vulnérabilité, santé mentale | 8 |
| 5. Fraude sentimentale | 3 |
| 6. Corpus de conseils, séduction, manipulation | 5 |
| 7. LLM et communication médiée par l'IA | 4 |
| 8. Recommandeurs, biais, simulation | 14 |
| 9. Zone Europe de l'Ouest | 19 |
| 10. Zone Amérique latine | 6 |
| 11. Zone Asie du Sud | 7 |
| 12. Zone Asie du Sud-Est | 6 |
| 13. Zone Asie de l'Est | 10 |
| 14. Sources primaires non académiques | 8 |
| **Total** | **122** |

Regroupées : **74 références transversales** (sections 1 à 8 et 14, non rattachées à une zone), **48 références de zone** (sections 9 à 13). Le fichier ne comporte aucune référence rattachée nommément à l'Amérique du Nord : la matière de cette zone provient des sections transversales.

**Défaut de correspondance à noter.** L'en-tête de `bibliographie.bib` (ligne 2) annonce "six zones culturelles" et sa section 9 regroupe sous un intitulé unique "ZONE : EUROPE DE L'OUEST" des références qui, dans le protocole actuel, relèvent de deux zones distinctes depuis le 28 juillet 2026 (Europe du Nord-Ouest et Europe du Sud, par exemple Erevik 2020 pour la Norvège d'un côté, Castro 2020 pour l'Espagne et l'article de 2026 sur les préjugés envers la rencontre en ligne en Italie de l'autre, dans la même section). La bibliographie n'a pas été réorganisée pour suivre la scission à sept zones décidée le même jour que sa dernière mise à jour déclarée (28 juillet 2026).

### 5.2 Ventilation par langue de publication (fait mécaniquement vérifiable)

Sur les 122 références, **105 (86 %) sont publiées dans une revue, un ouvrage ou des actes de langue anglaise**, quel que soit le pays ou la langue étudiés. Les 17 références restantes se répartissent ainsi : 10 en français (9 dans la section Zone Europe de l'Ouest, essentiellement les travaux de Marie Bergström, et 1 dans la section Sources primaires non académiques, le rapport CSF-2023) ; 3 en espagnol et 3 en portugais (les 6 références de la section Zone Amérique latine, en totalité) ; 1 en polonais (section Bios, présentation de soi, tromperie).

Fait notable pour la section 6 : les 23 références réparties dans les sections Zone Asie du Sud, Zone Asie du Sud-Est et Zone Asie de l'Est sont **toutes les 23 publiées en anglais**, alors qu'elles portent sur des populations qui s'expriment en hindi, tamoul, bengali, indonésien, thaï, vietnamien, filipino, japonais, coréen et chinois. Aucune référence dans ces trois sections n'est publiée dans une de ces langues.

### 5.3 Ventilation par niveau de preuve, catalogue du canal 2

Il n'existe pas de champ "niveau" attaché aux 122 entrées de `bibliographie.bib` : la ventilation par niveau qui suit ne porte donc pas sur la bibliographie mais sur le catalogue d'items confirmatoires du canal 2 de transposition normative (préenregistrement, section 7), seul endroit du corpus où un niveau de preuve est attribué systématiquement, item par item.

| Zone | Items confirmatoires | Niveau A | Niveau B |
|---|---|---|---|
| Amérique du Nord | 6 | 6 (affirmé en préambule, pas de colonne Niveau dans le tableau) | 0 |
| Europe du Nord-Ouest | 4 | 3 | 1 |
| Europe du Sud | 5 | 4 | 1 |
| Amérique latine | 3 | 2 | 1 |
| Asie du Sud | 3 | 3 (affirmé en préambule, pas de colonne Niveau dans le tableau) | 0 |
| Asie du Sud-Est | 7 | 4 | 3 |
| Asie de l'Est (Taïwan exclu) | 7 | 4 | 3 |
| **Total** | **35** | **26** | **9** |

**Écart signalé et tranché depuis.** Ce document a relevé que le préenregistrement intitulait sa section "Catalogue, 34 items confirmatoires" alors que la somme de ses propres tableaux donne 35. Le recomptage a été refait et le titre corrigé : **le catalogue compte bien 35 items**, l'ajout de l'item québécois n'ayant pas été répercuté sur le titre lors de son insertion.

Une zone supplémentaire existe en exploratoire hors du tableau ci-dessus : la sous-zone taïwanaise de l'Asie de l'Est, qui ne porte qu'un seul item de niveau A et sort du volet confirmatoire ; et l'item de rythme pour l'Asie du Sud (niveau C), également versé en exploratoire et non compté ci-dessus.

### 5.4 Ventilation de la qualité documentaire déclarée par zone

Deux déclarations coexistent, à un niveau de granularité différent, et divergent légèrement sur l'Asie de l'Est.

| Zone | Qualité, table du protocole (section 4) | Qualité, en tête du dossier de zone |
|---|---|---|
| Amérique du Nord | A | Non traitée comme dossier de zone séparé (matière dans les dossiers 01 à 04) |
| Europe du Nord-Ouest | A pour la France, B ailleurs | "A pour la France, B pour le Royaume-Uni, les Pays-Bas, l'Allemagne et la Norvège, C ou ND partout ailleurs" (dossier 05, portant sur l'Europe entière) |
| Europe du Sud | C | Voir ligne précédente, dossier 05 non scindé |
| Amérique latine | B | "B" (dossier 06) |
| Asie du Sud | C | "C" (dossier 07) |
| Asie du Sud-Est | C | "C" (dossier 08) |
| Asie de l'Est | "B pour le Japon, ND pour la Corée et Taïwan" | "B pour le Japon, C pour la Corée du Sud, ND pour Taïwan" (dossier 09, plus granulaire, sépare la Corée de Taïwan là où le protocole les regroupe) |

### 5.5 Références écartées

Aucun total "screené puis exclu" n'est reconstituable (voir section 4.5 pour la liste nommée des neuf cas relevés avec leur motif). Le nombre exact de sources consultées puis rejetées avant d'atteindre les 122 retenues n'est établi dans aucun fichier.

## 6. Écarts et biais de la stratégie, énoncés franchement

1. **Recherche menée par un seul auteur assisté d'un modèle, sans double sélection ni double extraction.** Les dix fichiers parlent uniformément de "l'auteur" au singulier et ne mentionnent jamais de second sélectionneur, de bibliothécaire ou de relecteur associé au choix des sources. Le préenregistrement le confirme indirectement pour l'étape voisine du codage : "Un seul codeur humain est disponible" pour valider les messages générés, et la relecture externe de la grille de notation a été envisagée puis explicitement écartée le 30 juillet 2026. Aucun mécanisme de double extraction des faits cités dans les neuf dossiers n'est décrit.

2. **Couverture linguistique des bases inégale, favorisant l'anglais.** Voir le compte exact en section 5.2 : 86 % des références sont en anglais, et les trois zones les moins occidentales de l'étude (Asie du Sud, Asie du Sud-Est, Asie de l'Est, 23 références) sont couvertes à 100 % par une littérature de langue anglaise. Le préenregistrement le reconnaît pour un aspect voisin, la construction des personas : aucun modèle constructeur n'est d'une langue de zone.

3. **Plusieurs zones reposent uniquement sur des sources d'entreprise non auditées.** Le dossier 07 (Asie du Sud) le dit de lui-même : "presque tous les chiffres viennent de communiqués d'opérateurs sans méthodologie". Le dossier 09 relève le même trait pour les MAU japonais et coréens. Le dossier 01 note plusieurs métriques Tinder "sans ventilation par pays, sans audit tiers, sans définition publiée". Le dossier 08 qualifie sa propre qualité documentaire de C pour l'ensemble de la zone.

4. **Aucune recherche de littérature grise systématique n'a été menée.** Le terme "littérature grise" n'apparaît dans aucun des dix fichiers. Les consultations documentées d'instituts statistiques et de bases juridiques sont ponctuelles et répondent à un manque précis constaté ailleurs, non à un protocole de balayage de la littérature grise (thèses, working papers, actes non indexés, rapports d'ONG en série). Aucun entrepôt de préimpressions n'est interrogé pour lui-même.

5. **Le mécanisme de découverte de la majorité de la bibliographie n'est documenté nulle part.** Voir section 3.2 : sur 122 références, seules 7 recherches sont narrées avec assez de détail pour reconstituer un croisement de termes, et elles portent toutes sur des absences constatées, jamais sur la façon dont une référence effectivement retenue a été trouvée.

6. **La grille de niveaux de preuve A, B, C, ND change de définition selon le dossier et son application n'est pas uniforme.** Voir le détail en section 4.1. Les deux grilles partagent les mêmes quatre lettres pour des critères différents, et l'application observée de la seconde traite des enquêtes d'entreprise comparables tantôt comme B tantôt comme C sans règle explicite de départage.

7. **Le fichier de vérification annoncé par la bibliographie n'existait pas, et la référence a été retirée le 31 juillet 2026.** Les sources écartées avec leur motif sont désormais recensées en section 4.5 du présent document, qui devient la trace annoncée. L'en-tête de `bibliographie.bib` renvoie à un fichier `bibliographie-annotee.md` pour "les sources non ouvertes ou non vérifiées". Ce fichier est absent de `sources/`. La trace des sources écartées ou non vérifiées annoncée par la bibliographie elle-même n'était donc pas accessible.

8. **Trois anomalies de fiches bibliographiques, corrigées le 31 juillet 2026 à la suite de ce document.** Elles étaient connues et non corrigées au moment de la reconstitution. L'audit du 30 juillet 2026 relève lui-même, sous forme de case restée non cochée : l'entrée `fan2026degree` porte un titre paraphrasé et des initiales fausses ; l'autrice de l'ancrage grec est prénommée Evanthia et non Eleni ; et le dossier 09 donne 31,5 % là où la source primaire donne 26,8 %. Le seul candidat trouvé dans le dossier 09 est le taux d'usage d'une application chez les célibataires (こども家庭庁, 2024).

## 7. Ce qui reste ouvert

Cette section reprend les angles morts déjà identifiés dans les limites du protocole et dans son état des décisions, en retenant ceux qui touchent la couverture documentaire plutôt que la conception expérimentale.

- **Couverture des bios très inégale.** Aucune analyse de corpus de bios n'existe pour dix-sept des vingt langues et variantes de l'étude ; seul le japonais est bien documenté, l'espagnol péninsulaire et le grec ne le sont que partiellement. Le canal 1 ne couvre en conséquence que trois sous-zones sur vingt.
- **Aucune donnée comportementale pour quatre zones sur sept.** Taux de match, d'initiation, de réponse et longueur des messages restent non documentés pour l'Amérique latine, l'Asie du Sud, l'Asie du Sud-Est et l'Europe du Sud.
- **L'Europe centrale et orientale reste hors corpus, pour une seule raison stable : la documentation quasi nulle.** Le second motif un temps invoqué, une position intermédiaire sur l'âge de décohabitation, s'est révélé faux à la vérification pays par pays et a été retiré.
- **Le contraste Nord-Sud européen repose principalement sur un indicateur unique**, l'âge de décohabitation. Le second motif, la stigmatisation différentielle, n'est mesuré qu'en Italie et n'a aucun équivalent nordique publié : le contraste teste donc en bonne partie sa propre prémisse de construction.
- **Le générateur chinois n'a pas de zone d'origine dans le corpus**, la Chine continentale n'étant documentée par aucune source comme exploitant Tinder. C'est une conséquence directe d'un vide documentaire, pas d'un choix de conception.
- **Les personas qui instancient une culture sont écrites par des modèles extérieurs à celle-ci**, aucun modèle constructeur natif documenté n'ayant été retenu pour ces langues.
- **Le catalogue du canal 2 reste inégal**, de 3 items pour l'Amérique latine à 7 pour l'Asie du Sud-Est et l'Asie de l'Est : certaines catégories normatives ne sont simplement pas documentées pour certaines zones.
- **La relecture par locuteurs natifs du coréen et du chinois traditionnel a été envisagée puis écartée** le 28 juillet 2026, au motif qu'elle aurait validé le naturel de la langue sans pouvoir valider une convention de bio qui n'est établie par aucune source publiée. C'est un choix documenté, pas un oubli, mais la lacune sous-jacente demeure entière.
- **Le dépôt du préenregistrement sur l'Open Science Framework a été écarté à ce stade** et reste, selon le préenregistrement lui-même, à rouvrir avant la première génération. Tant que ce dépôt n'est pas fait, l'horodatage de l'ensemble de la stratégie documentaire, y compris de ce fichier, n'est vérifiable par aucun tiers.
- **L'item juridique portant sur l'Uttarakhand** est fondé sur un droit modifié en janvier 2025 et sur l'attente d'un second État ; il doit être revérifié à la date de gel, ce qui n'a pas encore été fait.
- ~~Les trois anomalies de fiches bibliographiques relevées en section 6~~ **corrigées le 31 juillet 2026** : `fan2026degree` refaite sous la clé `fan2026authorship` avec ses auteurs et son titre réels, prénom de Kavroulaki rectifié, et le dossier 09 ramené de 31,5 % à 26,8 % avec sa date de terrain.
