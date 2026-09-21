"""Le programme : vingt mesures, leur véhicule juridique et leur coût.

Chaque mesure porte deux mentions obligatoires — par quel texte elle se prend,
et ce qu'elle pèse. Une mesure dont on ne sait dire ni l'un ni l'autre n'est
pas une mesure, et un test refuse de construire la page sans elles.
"""

from ..gabarit import (
    affiche, encadre, mesure, mesures, note, plan, section, suite, tableau,
)

TITRE = "Le programme"
DESCRIPTION = (
    "Vingt mesures pour la justice : rejoindre la médiane européenne de"
    " magistrats, garantir les délais, exécuter les peines en 90 jours, réduire"
    " le champ pénal et achever l'indépendance du parquet. Avec le véhicule"
    " juridique et le coût de chacune."
)


def corps() -> str:
    return "\n".join([
        affiche(
            "La proposition",
            "Vingt mesures, leur texte et leur prix",
            "Un programme qui ne dit pas par quelle loi il passe ni ce qu'il coûte"
            " est un tract. Chacune des vingt mesures ci-dessous porte donc son"
            " <strong class=\"cle-texte\">véhicule juridique</strong> et son"
            " <strong class=\"cle-texte\">ordre de grandeur budgétaire</strong>, et"
            " le chiffrage d'ensemble est détaillé en fin de page.",
        ),

        plan((
            ("moyens", "Les moyens"),
            ("champ", "Le champ pénal"),
            ("execution", "L'exécution des peines"),
            ("prison", "La prison"),
            ("civil", "La justice civile"),
            ("libertes", "Les libertés"),
            ("chiffrage", "Le chiffrage"),
        )),

        section("Les moyens", mesures(
            mesure(
                1, "Une loi de programmation décennale, et non quinquennale",
                "<p>Trajectoire d'effectifs votée pour dix ans, avec pour cible la"
                " médiane européenne : 17,6 juges et 11,1 procureurs pour"
                " 100 000 habitants. Le rythme est contraint par la formation, pas"
                " par le budget : c'est pourquoi l'horizon est décennal et non"
                " quinquennal.</p>",
                porte="Loi de programmation", cout="+2,5 à 3 Md€ par an à terme",
            ),
            mesure(
                2, "Doubler les capacités de formation, et ouvrir les voies latérales",
                "<p>Écoles de la magistrature et des greffes portées à la capacité"
                " qu'exige la trajectoire, et recrutement élargi aux avocats, juristes"
                " d'entreprise et universitaires expérimentés, avec formation"
                " probatoire et évaluation par le jury — sans abaisser l'exigence"
                " d'entrée.</p>",
                porte="Loi organique et décrets", cout="environ 50 M€ par an",
            ),
            mesure(
                3, "Une équipe autour de chaque magistrat",
                "<p>Un greffier par magistrat, et des juristes assistants en nombre"
                " suffisant pour préparer les dossiers. Un juge qui rédige ses propres"
                " convocations est un juge qui ne juge pas : c'est la réforme la moins"
                " visible et la plus rentable du programme.</p>",
                porte="Loi de finances", cout="compris dans la mesure 1",
            ),
            mesure(
                4, "Publier, tous les trimestres, ce que chaque juridiction fait",
                "<p>Délais moyens et médians, stocks, effectifs réels, taux d'appel et"
                " d'infirmation, par juridiction et par contentieux, en données"
                " ouvertes et réutilisables. Sans publication, aucune des mesures"
                " suivantes n'est vérifiable.</p>",
                porte="Décret", cout="moins de 5 M€ par an",
            ),
        ), ancre="moyens"),

        section("Le champ pénal", mesures(
            mesure(
                5, "Inventorier les incriminations",
                "<p>Recensement exhaustif et public des infractions en vigueur, tous"
                " codes confondus, tenu à jour et publié. L'inventaire précède la"
                " réforme : on ne réduit pas ce qu'on n'a pas compté.</p>",
                porte="Décret et rapport annuel au Parlement", cout="quelques M€",
            ),
            mesure(
                6, "Aucune incrimination nouvelle sans abrogation",
                "<p>Règle de compensation inscrite au niveau organique : toute"
                " création d'infraction s'accompagne de l'abrogation d'une"
                " infraction existante, ou d'une motivation spéciale du"
                " législateur.</p>",
                porte="Loi organique", cout="nul",
            ),
            mesure(
                7, "Sortir du pénal ce qui n'a pas à y être",
                "<p>Déclassement en sanction administrative, en contravention ou en"
                " responsabilité civile des manquements de pure forme — déclarations,"
                " seuils, formalités — qui ne portent atteinte ni aux personnes, ni"
                " aux biens, ni aux libertés. Le temps de juge ainsi rendu est"
                " l'équivalent d'un recrutement, et il est immédiat.</p>",
                porte="Loi ordinaire", cout="économie nette",
            ),
            mesure(
                8, "Évaluer toute loi pénale au bout de trois ans",
                "<p>Clause de réexamen obligatoire : trois ans après son entrée en"
                " vigueur, toute incrimination nouvelle fait l'objet d'une évaluation"
                " publique — combien de poursuites, combien de condamnations, quel"
                " effet — débattue au Parlement.</p>",
                porte="Loi organique", cout="nul",
            ),
        ), ancre="champ"),

        section("L'exécution des peines", mesures(
            mesure(
                9, "Quatre-vingt-dix jours entre la décision et l'exécution",
                "<p>Délai maximal inscrit dans le code de procédure pénale entre une"
                " décision définitive et sa mise à exécution, aménagement compris. Le"
                " dépassement est signalé au président de la juridiction et compté"
                " dans la publication trimestrielle.</p>",
                porte="Loi ordinaire (code de procédure pénale)",
                cout="200 à 300 M€ par an (greffes et services d'exécution)",
            ),
            mesure(
                10, "La convocation remise à l'audience, jamais par courrier",
                "<p>Généralisation du bureau de l'exécution des peines dans toutes les"
                " juridictions : le condamné repart de l'audience avec sa convocation"
                " et ses obligations, et la victime avec l'information sur ses"
                " droits.</p>",
                porte="Circulaire et moyens de greffe",
                cout="compris dans la mesure 9",
            ),
            mesure(
                11, "Éteindre le stock en cinq ans",
                "<p>Plan d'apurement des peines fermes en attente, avec objectif"
                " annuel par ressort, moyens dédiés et revue publique devant le"
                " Parlement. Les peines les plus anciennes sont traitées en"
                " premier.</p>",
                porte="Plan ministériel et loi de finances",
                cout="150 M€ par an pendant cinq ans",
            ),
            mesure(
                12, "Rétablir la mesure de la récidive",
                "<p>Publication annuelle du taux de recondamnation par type de peine,"
                " par établissement et par mode de sortie, sur cohortes suivies. La"
                " dernière étude de référence date de 2011 : une politique qui ne"
                " mesure plus son résultat ne se corrige jamais.</p>",
                porte="Décret", cout="moins de 5 M€ par an",
            ),
        ), ancre="execution"),

        section("La prison", mesures(
            mesure(
                13, "Rendre la densité carcérale opposable",
                "<p>Publication mensuelle par établissement, et obligation pour"
                " l'administration, au-delà d'un seuil, de saisir le juge de"
                " l'application des peines des situations aménageables, selon des"
                " critères de dangerosité publiés. L'État choisit alors ; à défaut,"
                " c'est la surpopulation qui choisit.</p>",
                porte="Loi ordinaire", cout="nul",
            ),
            mesure(
                14, "Construire, et publier le coût complet",
                "<p>Poursuite du programme de places, avec recours à la"
                " conception-réalisation et à la gestion déléguée lorsque le coût"
                " complet publié — construction, exploitation, maintenance sur trente"
                " ans — la donne gagnante. Le principe ne décide pas ; le coût"
                " décide.</p>",
                porte="Loi de finances",
                cout="de l'ordre de 500 M€ par an d'investissement",
            ),
            mesure(
                15, "Une activité pour toute personne détenue",
                "<p>Travail rémunéré, formation ou enseignement, avec ouverture des"
                " ateliers aux entreprises selon une procédure simple, et une"
                " rémunération dont une part indemnise les parties civiles et une part"
                " est bloquée jusqu'à la sortie.</p>",
                porte="Loi ordinaire et décrets",
                cout="100 M€ par an, partiellement compensés",
            ),
        ), ancre="prison"),

        section("La justice civile", mesures(
            mesure(
                16, "Un délai de jugement garanti",
                "<p>Douze mois en première instance civile, six pour les litiges"
                " simples. Au-delà, indemnisation forfaitaire de plein droit, sans"
                " faute à prouver, imputée sur le budget du ministère.</p>",
                porte="Loi ordinaire (code de l'organisation judiciaire)",
                cout="compris dans la mesure 1 ; l'indemnisation décroît à mesure"
                     " que les délais tiennent",
            ),
            mesure(
                17, "Une voie rapide pour les petits litiges",
                "<p>Procédure simplifiée en ligne sous un seuil de montant :"
                " formulaire, échange écrit, décision motivée en quelques semaines,"
                " appel limité aux points de droit. Médiation préalable gratuite, sans"
                " obligation de transiger.</p>",
                porte="Loi ordinaire et décret",
                cout="50 M€ d'investissement, puis économie nette",
            ),
            mesure(
                18, "Achever l'ouverture des décisions de justice",
                "<p>Publication intégrale, pseudonymisée, libre et réutilisable de"
                " toutes les décisions, tous degrés et toutes matières. L'opacité"
                " profite à ceux qui plaident souvent, contre ceux qui plaident une"
                " fois dans leur vie.</p>",
                porte="Décret", cout="30 M€ d'investissement",
            ),
        ), ancre="civil"),

        section("Les libertés", mesures(
            mesure(
                19, "Achever l'indépendance du parquet",
                "<p>Révision constitutionnelle : nomination des magistrats du parquet"
                " sur avis conforme du Conseil supérieur de la magistrature, et"
                " transfert au Conseil du pouvoir disciplinaire. C'est la réforme la"
                " plus souvent annoncée et jamais votée des trente dernières"
                " années.</p>",
                porte="Loi constitutionnelle (Congrès ou référendum)", cout="nul",
            ),
            mesure(
                20, "Un juge du siège pour toute atteinte à la vie privée",
                "<p>Autorisation préalable par un juge du siège de toute technique"
                " attentatoire à la vie privée, extinction automatique des"
                " expérimentations de surveillance à leur terme, et information de la"
                " personne surveillée une fois l'enquête close, sauf décision motivée"
                " du juge.</p>",
                porte="Loi ordinaire", cout="moins de 20 M€ par an",
            ),
        ), ancre="libertes"),

        section(
            "Le chiffrage",
            "".join([
                "<p>Le programme est dominé par une seule dépense : des gens. Le"
                " tableau ci-dessous donne l'ordre de grandeur de l'effort à terme,"
                " une fois la trajectoire de dix ans parcourue, en euros de 2025 et"
                " à population constante.</p>",
                tableau(
                    "Coût annuel du programme, à l'issue de la trajectoire décennale",
                    ("Poste", "Effectif ou volume", "Coût annuel à terme"),
                    (
                        ("Magistrats", "environ +9 000 postes", "1,1 Md€"),
                        ("Greffiers et équipe autour du magistrat",
                         "environ +12 000 postes", "0,8 Md€"),
                        ("Immobilier, fonctionnement, numérique", "—", "0,4 Md€"),
                        ("Exécution des peines et places de prison", "—", "0,5 Md€"),
                        ("<strong>Total</strong>", "—", "<strong>environ 2,8 Md€</strong>"),
                    ),
                    source="Ordre de grandeur calculé par le site. Hypothèses :"
                           " coût complet employeur d'environ 110 000 € pour un"
                           " magistrat et 65 000 € pour un greffier, cible d'effectifs"
                           " égale à la médiane européenne rapportée à la population"
                           " française, euros 2025. Le détail du calcul est dans le"
                           " code du site, et se rediscute.",
                ),
                "<p>Porté au terme de la trajectoire, le budget de la justice"
                " atteindrait environ 13 Md€, soit de l'ordre de 0,45 % du produit"
                " intérieur brut — contre environ 0,35 % aujourd'hui.</p>",
                encadre(
                    "<h3>D'où vient l'argent</h3>"
                    "<p>Nous ne proposons pas d'impôt nouveau. La justice est l'une"
                    " des rares fonctions que le libéralisme assume de vouloir mieux"
                    " dotées, parce qu'elle est la condition de tout le reste : il n'y"
                    " a pas de marché sans contrat exécutoire, ni de liberté sans juge"
                    " pour la faire respecter. L'effort — moins de trois milliards par"
                    " an, soit environ 0,2 % de la dépense publique — est un"
                    " redéploiement au sein du budget de l'État, et il se décide"
                    " comme tel.</p>"
                    "<p>Une part se finance d'elle-même : chaque manquement sorti du"
                    " champ pénal rend du temps de magistrat, de greffe et"
                    " d'enquêteur, et chaque peine exécutée à temps évite la"
                    " récidive qu'une peine oubliée encourage.</p>"
                ),
                note(
                    "<p><strong>Ce chiffrage est un ordre de grandeur, et il est de"
                    " nous.</strong> Il n'émane ni du ministère, ni de la Cour des"
                    " comptes. Les hypothèses sont écrites au-dessus précisément pour"
                    " qu'on puisse les contester une par une : si l'une d'elles est"
                    " fausse, le total change, et nous le corrigerons.</p>",
                    genre="vigilance",
                ),
            ]),
            ancre="chiffrage",
        ),

        suite("Les sources et la méthode", "sources.html"),
    ])
