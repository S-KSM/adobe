## Personalization Engine Architecture

```mermaid

graph LR

A[Front-end application] -- HTTP requests/responses --> B((Personalization Engine))
B -- Data storage --> C[Adobe Experience Platform AEP]
B -- Machine learning models --> D[Adobe Sensei]
B -- Event tracking --> E[Adobe Analytics]
B -- Content delivery --> F[Adobe Experience Manager AEM]
G[Workflow management Adobe Workfront] -- Content approval and metadata updates --> F



## Personalization Engine Architecture

```mermaid
graph LR
A[Front-end application] -- HTTP requests/responses --> B((Personalization Engine))
B -- Data storage --> C[Cloud SQL]
B -- Machine learning models --> D[Cloud AI Platform]
B -- Event tracking --> E[Google Analytics]
B -- Content delivery --> F[Cloud Storage]
