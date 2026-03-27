# WAF_LAB

Mise en place de la sécurité applicative (WAF) sur deux applications Flask en utilisant Nginx et ModSecurity.

## Compétences Acquises

Ce projet démontre l'acquisition des compétences suivantes dans le domaine de la sécurité web et de la configuration de serveurs :

### Configuration Nginx
- **Serveurs virtuels** : Configuration de blocs serveur pour deux applications distinctes (app1 et app2) avec noms de domaine spécifiques.
- **Redirection HTTPS** : Mise en place automatique de redirections HTTP vers HTTPS pour sécuriser les connexions.
- **Proxy inverse** : Configuration de proxy_pass pour rediriger les requêtes vers les applications Flask locales.

### Sécurité SSL/TLS
- **Certificats SSL** : Installation et configuration de certificats Let's Encrypt (fullchain.pem et privkey.pem).
- **Protocoles et chiffrements** : Configuration des protocoles TLSv1.2 et TLSv1.3 avec des chiffrements sécurisés (ECDHE avec AES-GCM et ChaCha20-Poly1305).
- **Cache de session SSL** : Optimisation des performances avec cache partagé et timeout de session.
- **Désactivation des tickets de session** : Amélioration de la sécurité en désactivant les tickets de session SSL.

### Headers de Sécurité
- **HSTS (HTTP Strict Transport Security)** : Ajout de l'en-tête HSTS avec max-age de 1 an et includeSubDomains.
- **Masquage des tokens serveur** : Désactivation de l'exposition des informations serveur Nginx.
- **Masquage des headers personnalisés** : Utilisation de proxy_hide_header pour cacher les headers spécifiques des applications.

### Contrôle d'Accès et Authentification
- **Contrôle d'accès IP** : Restriction d'accès aux adresses IP autorisées (allow/deny).
- **Authentification de base** : Configuration commentée pour l'authentification HTTP de base avec fichier .htpasswd.

### Protection WAF (Web Application Firewall)
- **ModSecurity** : Intégration de ModSecurity pour la détection et prévention des attaques web.
- **Limitation de débit** : Configuration de limit_req pour limiter le nombre de requêtes par IP (burst=5, status 429).

### Gestion des Erreurs
- **Pages d'erreur personnalisées** : Configuration d'erreur_page pour les codes 500, 502, 503, 504.
- **Interception d'erreurs proxy** : Activation de proxy_intercept_errors pour gérer les erreurs en amont.

### Développement d'Applications
- **Flask** : Développement d'applications web simples en Python utilisant le framework Flask.
- **Headers personnalisés** : Gestion des headers de réponse dans les applications Flask.

### Analyse de Sécurité
- **SSLyze** : Utilisation de l'outil SSLyze pour analyser et scanner les configurations SSL/TLS.
- **Rapports JSON** : Génération de rapports d'analyse de sécurité au format JSON.

## Architecture

- **app1.py / app2.py** : Applications Flask simples exposant des endpoints de base.
- **nginx.conf** : Configuration Nginx avec sécurité renforcée pour app1 et protection WAF complète pour app2.
- **main.py** : Script principal du projet.
- **pyproject.toml** : Dépendances Python (Flask, SSLyze).
- **result-app1.json / result-app2.json** : Résultats des analyses SSL.

## Utilisation

1. Installer les dépendances : `pip install -e .`
2. Lancer les applications Flask : `python app1.py` ou `python app2.py`
3. Configurer Nginx avec le fichier nginx.conf
4. Analyser la sécurité SSL : Utiliser SSLyze pour générer les rapports

Ce laboratoire permet de maîtriser les fondamentaux de la sécurisation d'applications web modernes. 
