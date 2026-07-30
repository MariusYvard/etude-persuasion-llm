# Surface produit Tinder réelle

Ce que voit un utilisateur, et à quel moment. Contraint directement le schéma de persona : un message d'ouverture est écrit à partir de ces champs et de rien d'autre.

## Champs de profil, liste officielle

Source unique exhaustive : centre d'aide, « Editing your profile ».
https://www.help.tinder.com/hc/en-us/articles/115003339043-Editing-your-profile

Champs éditables : Photos/Loops, About Me/Bio, Lifestyle Interests and other tags, Pronouns, Height, Relationship Goals, Languages, Job/Company, School, Living In/City, Gender, Sexual Orientation.

Citation exacte sur l'obligatoire : « Your name and age are the only details in your profile that you can't edit once you've created an account. » Prénom et âge sont les seuls éléments figés. **Niveau A.**

### Champ par champ

| Champ | Statut | Niveau | Note |
|---|---|---|---|
| Prénom | Imposé, non éditable | A | |
| Âge | Imposé, non éditable | A | Masquable via Tinder Plus |
| Distance | Affichée par défaut | A | Masquable via Tinder Plus |
| Photos | Optionnel | ND | **Nombre maximal non documenté par Tinder.** La valeur de 9 emplacements vient de la presse tierce |
| Bio | Optionnel | ND | **Limite de caractères non documentée.** 500 est rapporté par des tiers sans source officielle |
| Ville | Optionnel | A | Champ « Living In/City » |
| Profession | Optionnel | A | Champ « Job/Company » |
| École | Optionnel | A | Champs additionnels en College Mode |
| Taille | Optionnel | A | Ajouté à la refonte de novembre 2023 |
| Tags intérêts et lifestyle | Optionnel | A | Intérêts, animaux, habitudes de consommation d'alcool, signes astrologiques |
| Prompts | Optionnel | A | Refonte novembre 2023. Exemples officiels : « The key to my heart is », « Two truths and a lie ». **Nombre affichable et limite par réponse non documentés** |
| Badge de vérification | Conditionnel | A | Deux badges distincts, voir plus bas |
| Anthem Spotify | Ambigu | ND | N'apparaît pas dans la liste officielle actuelle. Music Mode refondu en mars 2026 |
| Lien Instagram | Supprimé | A | Retrait des identifiants sociaux en mai 2023, fermeture de l'Instagram Basic Display API le 4 décembre 2024 |

### Liens et identifiants sociaux : interdits

Community Guidelines, règle 2 : « Don't publicly broadcast your personal information or ways for people to connect with you (no public displays of things like phone numbers, emails, or social handles). »
https://policies.tinder.com/community-guidelines/intl/en/

**Conséquence directe pour le corpus** : une bio réaliste ne contient ni @, ni numéro, ni lien. **Niveau A.**

## Ce qui change après le match

**Aucune information de profil supplémentaire n'est débloquée par le match.** Le centre d'aide ne décrit nulle part de champ révélé. Le match ouvre uniquement le canal de conversation.

Citation : « Only once you've matched with someone on Tinder can you start to chat with that person. »
https://www.help.tinder.com/hc/en-us/articles/115003341583-Messaging-a-Match

**Conséquence pour le protocole** : le message d'ouverture est écrit à partir de photos, prénom, âge, distance, bio, tags et prompts. Rien d'autre. C'est la contrainte informationnelle centrale de l'étude, et elle est ce qui rend la question de la personnalisation intéressante. **Niveau A.**

Exception documentée : First Impressions permet un message de **140 caractères maximum avant le match**, inclus hebdomadairement avec Platinum.
https://www.help.tinder.com/hc/en-us/articles/360046358932-First-Impressions

## Surface de chat

- Suggestions d'ouverture natives : **non documentées officiellement.** Aucun article du centre d'aide n'en décrit. Une source spécialisée rapporte des tests non annoncés. **Niveau ND.**
- Limite de longueur en conversation : **non documentée.** Seule limite chiffrée officielle : 140 caractères pour First Impressions, donc pré-match.
- Accusés de lecture : **statut contesté.** Le paramètre existe encore dans le Safety Center, plus aucun article d'aide dédié. Deux sources spécialisées affirment une dépréciation au 7 janvier 2026, une troisième affirme le contraire. **Niveau ND, ne pas trancher.**
- Indicateurs de frappe : **non documentés.**
- Modération en ligne : « Are You Sure? » côté expéditeur et « Does This Bother You? » côté réception, élargis en février 2023, passés à une détection LLM contextuelle avec floutage automatique en mars 2026. **Niveau A.**

Ce dernier point est méthodologiquement important : la plateforme applique désormais un filtre LLM sur les messages entrants. Un message généré par LLM est donc évalué par un autre LLM avant d'atteindre le destinataire. À mentionner dans la discussion.

## Fonctionnalités IA déployées par Tinder

| Fonctionnalité | Ce qu'elle fait | Traitement | Niveau |
|---|---|---|---|
| Photo Selector | Parcourt la pellicule, propose environ 10 photos | Intégralement sur appareil, données biométriques supprimées à la sortie | A |
| Photo Insights | Descriptions courtes tirées de la pellicule | Hybride, scan local puis upload temporaire serveur | A |
| Chemistry / AI-powered matching | Questionnaire plus pellicule optionnelle, livre « Daily Drops » | Opt-in, marchés sélectionnés | A |
| Learning Mode | Ajuste les recommandations en temps réel | Mondial depuis mars 2026 | A |
| Photo Enhance | Corrige luminosité et saturation. **Ne modifie ni visages ni corps** | Marchés sélectionnés | A |

**Point capital pour le cadrage de l'étude** : aucune assistance IA à la rédaction de messages en conversation n'est documentée officiellement chez Tinder. Hinge, en revanche, a déployé « Prompt Feedback » en janvier 2025 (GPT-4o mini) puis « Convo Starters » en décembre 2025. La rédaction assistée est donc déjà un fait produit chez un concurrent direct du même groupe.
https://techcrunch.com/2025/12/08/hinges-new-ai-feature-helps-daters-start-better-convos-moving-beyond-boring-small-talk

## Vérification d'identité

Quatre dispositifs distincts, à ne pas confondre.

1. **Photo Verification**, optionnelle, selfie vidéo comparé aux photos, donne un « Photo Verified checkmark ».
2. **Photo Check**, imposée conditionnellement quand les systèmes détectent une activité inhabituelle. Non-complétion sous deux ans : désactivation du compte.
3. **Face Check**, liveness obligatoire à l'inscription. Dispositif central 2025-2026. Fournisseur de la détection de vivacité identifié par la presse biométrique comme FaceTec.
4. **Vérification d'âge**, dispositif séparé, obligatoire au Japon par une loi spécifique (voir `09-zone-asie-est.md`).

### Chronologie Face Check, vérifiée

| Date | Marché | Source |
|---|---|---|
| avant été 2025 | Colombie, Canada | Axios 30 juin 2025 |
| juin 2025 | Californie, nouveaux utilisateurs | TechCrunch |
| 18 juin 2025 | Canada, communiqué dédié | ca.tinderpressroom.com |
| 8 octobre 2025 | **Inde**, obligatoire nouveaux utilisateurs | Business Standard |
| 15 octobre 2025 | **Thaïlande**, obligatoire nouveaux utilisateurs | th.tinderpressroom.com |
| 22 octobre 2025 | Extension États-Unis. Marchés déjà actifs cités : Colombie, Canada, Australie, Inde, « several countries across Southeast Asia » | tinderpressroom.com |
| 24 novembre 2025 | Mexique et Amérique latine | mx.tinderpressroom.com |
| 25 mars 2026 | Royaume-Uni | Global Dating Insights |

**Fait notable** : l'Inde et la Thaïlande précèdent le marché américain de deux semaines. Le déploiement n'est pas centré sur l'Occident.

**Union européenne et France : non documenté.** Aucun communiqué. La FAQ dit seulement « where local regulations permit ». La salle de presse française ne mentionne Face Check dans aucun communiqué de décembre 2025 à juillet 2026.

### Rétention biométrique déclarée

Selfie vidéo supprimé après évaluation. FaceMap et FaceVector conservés pour la durée de vie du compte, supprimés sous 30 jours après clôture. Images d'audit conservées 90 jours après clôture, un an en cas de bannissement. Stockage AWS. **Base légale revendiquée : le consentement**, dont le retrait n'est possible qu'en supprimant le compte.
https://policies.tinder.com/faq-mandatory-liveness-check/intl/en/

Tension juridique à documenter : l'article 9(1) du RGPD pose une interdiction de principe du traitement biométrique aux fins d'identification unique. Un consentement dont le retrait implique la suppression du compte est difficilement « libre » au sens de l'article 7.4. **Aucune prise de position de la CNIL, de l'EDPB ni de la DPC irlandaise n'a été trouvée.** Le responsable de traitement pour l'EEE est MTCH Technology Services Limited, Dublin, donc l'autorité chef de file est irlandaise, pas française.

### Métriques revendiquées par Tinder

Baisse de plus de 60 % de l'exposition aux acteurs malveillants, baisse de plus de 40 % des signalements. Méthode : « un échantillon aléatoire pondéré de vues de profils in-app ». Pas de ventilation par pays, pas de période, pas d'audit tiers, pas de définition publiée d'acteur malveillant. **Niveau C.**

## Modes, couche de segmentation 2025-2026

Introduits le 10 septembre 2025. For You Mode (expérience classique), Double Date Mode, College Mode. Ajout le 12 mars 2026 de Music Mode et Astrology Mode, déploiement mondial.

Adoptions revendiquées : Music Mode 1 utilisateur sur 10 chez les moins de 22 ans, Astrology Mode hausse de près de 20 % des likes envoyés par les femmes. **Niveau C.**

## Points explicitement non documentés

À ne jamais combler par extrapolation dans le corpus :

- Nombre maximal de photos par profil
- Limite de caractères de la bio
- Limite de caractères par réponse de prompt, et nombre de prompts affichables
- Autorisation ou interdiction explicite des emoji en bio
- Limite de longueur des messages en conversation
- Existence d'indicateurs de frappe
- Statut actuel des accusés de lecture
- Répartition exacte entre carte visible et profil déplié
- Nombre de likes quotidiens sur le palier gratuit, et fenêtre de réinitialisation
- Durée et prix de Boost et Super Boost
- Liste nominative des sept pays où Face Check était obligatoire en octobre 2025
- Liste des marchés où Chemistry, Photo Insights et Photo Enhance sont actifs
