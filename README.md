# Persuasive drift in language models: a pre-registered study

**English summary.** When a language model is asked to "write an opening message that maximises the probability of a reply", with no mention of deception, does it spontaneously produce techniques the research literature classifies as manipulative?

This repository holds the complete pre-registration, the source dossiers it was built from, and a 122-entry bibliography with verified DOIs. **The study has not been run. Nothing here reports results.**

- **Design.** 560 synthetic personas across 7 cultural zones and 14 languages, a five-level instruction gradient from neutral to explicitly optimising, three model families, blind multi-model scoring in which the generating family is always excluded from judging its own outputs.
- **Coding grid.** Derived from the published literature on seduction communities and its academic critique, not invented for this study. Only fabrication and status-devaluation count as drift markers.
- **Two secondary questions carry the safety weight.** Does drift increase against profiles encoding empirically ranked vulnerability markers, meaning the model behaves worse toward those least able to resist? And do alignment behaviours generalise outside the Anglo-American distribution the alignment data comes from?
- **Ethics.** No real platform, user, profile or message is involved at any point. All personas are fictional. No dating platform is accessed, no account created, no message sent, and no connector to one exists or will be built.

Start with `protocole/preenregistrement.md`. The documents are in French. Section headings, tables and the bibliography are navigable without it.

---
# Dérive persuasive des LLM en contexte de rencontre en ligne

Étude sur corpus de personas synthétiques. Aucune donnée de personne réelle, aucun accès à une plateforme, aucun connecteur applicatif.

## Question de recherche

Un modèle de langage à qui l'on demande d'optimiser le taux de réponse d'un message d'ouverture, sans jamais mentionner la tromperie, dérive-t-il vers des procédés documentés comme manipulatoires ? La dérive est-elle plus forte face à des profils portant des marqueurs de vulnérabilité ? Le modèle transpose-t-il des scripts anglo-saxons à des contextes culturels où ils ne s'appliquent pas ?

## Hypothèses

- **H1** Une consigne optimisant le taux de réponse, sans mention de tromperie, augmente la production de procédés de fabrication et de dévalorisation par rapport à une consigne neutre.
- **H2** L'augmentation est plus forte face aux personas encodant des marqueurs de vulnérabilité.
- **H3** Les erreurs de transposition culturelle augmentent pour les personas non anglophones.

## Plan

560 personas synthétiques. Facteurs croisés : zone culturelle (7) × marqueur de vulnérabilité (5) = 35 cellules, 16 réplicats par cellule. Covariables équilibrées non croisées : strate d'âge, genre et orientation, intention relationnelle, densité de bio, vérification, nombre de photos.

Zones : Amérique du Nord, Europe du Nord-Ouest, Europe du Sud, Amérique latine, Asie du Sud, Asie du Sud-Est, Asie de l'Est. L'Europe centrale et orientale est exclue, motif en section 4.1 du préenregistrement.

Deux étages : 70 personas d'ancrage écrites en détail (2 par cellule), 490 personas d'échelle produites sous grammaire d'attributs avec contrôles anti-gabarit (14 par cellule).

Génération dans la langue locale, 5 conditions de consigne, 3 tirages, 3 modèles de familles différentes. Notation en aveugle par instances séparées, jamais par le générateur de la sortie notée. Volume : 25 200 messages, 75 600 notations.

## Arborescence

```
protocole/     préenregistrement, grille de notation, plan d'analyse
corpus/        schéma de persona, grammaire d'attributs, corpus généré
harnais/       scripts de génération et de notation (local)
resultats/     sorties codées, analyses
sources/       bibliographie et dossiers documentaires par thème
```

## Dossiers documentaires

| Fichier | Contenu |
|---|---|
| `sources/bibliographie.bib` | BibTeX, entrées vérifiées uniquement |
| `sources/01-surface-produit-tinder.md` | Champs de profil réels, contraintes d'interface, vérification d'identité |
| `sources/02-algorithme-et-exposition.md` | Modèle d'exposition, Elo, geosharding, recommandeurs, désirabilité |
| `sources/03-comportement-et-messages.md` | Démographie, bios, asymétries de genre, messages d'ouverture, vulnérabilité |
| `sources/04-corpus-conseils-et-llm.md` | Typologie des archétypes d'ouverture, littérature critique, état des LLM dans ce domaine |
| `sources/05-zone-europe.md` | France (dossier le plus fourni), Europe du Sud, Nord, Centre-Est |
| `sources/06-zone-amerique-latine.md` | Brésil, Mexique, Colombie, Argentine |
| `sources/07-zone-asie-sud.md` | Inde principalement |
| `sources/08-zone-asie-sud-est.md` | Indonésie, Philippines, Thaïlande, Vietnam, Malaisie, Singapour |
| `sources/09-zone-asie-est.md` | Japon, Corée du Sud, Taïwan, Chine |

## Convention de fiabilité

Chaque fait porte un niveau. Les fichiers de sources l'appliquent systématiquement.

- **A** Mesure publiée, évaluée par les pairs, échantillon et année de collecte connus.
- **B** Statistique publique ou institutionnelle, ou source primaire d'entreprise à méthodologie publiée.
- **C** Affirmation d'entreprise ou de presse sans méthodologie. Utilisable comme direction, jamais comme magnitude.
- **ND** Non documenté. À ne jamais combler par extrapolation depuis une autre zone.

## Limites assumées, à reproduire dans toute publication

La qualité documentaire est très inégale entre les sept zones. Elle est assumée comme limite, pas corrigée. Deux zones sont solidement documentées, deux moyennement, trois reposent largement sur des sources d'entreprise non auditées ou sur des échantillons de convenance. Les revendications de résultat sont restreintes zone par zone par deux clauses formelles :

- **Section 4.2**, Corée du Sud et Taïwan. Le registre de bio n'y est documenté par aucune source. Ces personas participent à H1 et H2, sont exclues du codage de transposition de registre et de l'analyse primaire de H3.
- **Section 4.3**, Europe du Sud. Aucune revendication de fidélité de registre pour l'italien et le portugais. La zone repose sur les deux seuls ancrages publiés, espagnol et grec.

Aucune analyse de corpus de bios n'existe pour treize des quatorze langues de l'étude. Le japonais fait exception. La seule mesure interculturelle publiée est un corpus britannique-espagnol de 455 profils, constitué par collecte automatisée. Ce corpus n'est pas reproduit ici et sa méthode de constitution n'est pas reprise, ce qui est un coût assumé du choix méthodologique et non une lacune accidentelle.
