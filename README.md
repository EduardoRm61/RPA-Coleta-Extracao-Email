# RPA-Coleta-Extracao-Email

Etapas obrigatórias do projeto:
1. Escolha e uso de uma API pública
Pesquise e selecione uma API pública gratuita da lista abaixo:
OpenWeatherMap – dados climáticos:
https://openweathermap.org/api
Open Food Facts – alimentos e ingredientes
https://world.openfoodfacts.org/data
The Dog API – raças e imagens de cães
https://thedogapi.com/
The Cat API – raças e imagens de gatos
https://thecatapi.com/
Deck of Cards API – simulação de baralhos
https://deckofcardsapi.com/
Rick and Morty API – personagens e episódios
https://rickandmortyapi.com/
Advice Slip API – conselhos aleatórios
https://api.adviceslip.com/
Fun Translations API – traduções divertidas
https://funtranslations.com/api/
Chuck Norris API – piadas do Chuck Norris
https://api.chucknorris.io/

Você deverá:
- Fazer uma requisição à API utilizando a biblioteca requests;
- Coletar e estruturar dados relevantes;
- Justificar sua escolha da API no relatório.
2. Armazenamento em Banco de Dados
- Crie um banco de dados SQLite chamado projeto_rpa.db;
- Crie ao menos uma tabela para armazenar os dados obtidos da API;
- Faça a inserção dos dados via Python.
3. Processamento
- Utilize a biblioteca re para extrair ou validar padrões específicos em textos dos
dados coletados;
- Grave os resultados processados em uma nova tabela chamada:
dados_processados.
4. Envio de Relatório por E-mail Automatizado
- Crie um script Python que envie um e-mail com:
- Um resumo dos dados coletados e processados;
- O conteúdo do e-mail pode ser um relatório em texto automaticamente.
