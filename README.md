# Web scraping TechNews

  Tive que fazer um projeto que tinha como principal objetivo fazer consultas em notícias sobre tecnologia.

  As notícias tinham que ser obtidas através da raspagem do [_blog da Trybe_](https://blog.betrybe.com).

  <strong>🚵 Habilidades que foram trabalhadas:</strong>
  <ul>
    <li>Utilizar o terminal interativo do Python</li>
    <li>Escrever meus próprios módulos e importá-los em outros códigos</li>
    <li>Técnicas de raspagem de dados</li>
    <li>Extrair dados de conteúdo HTML</li>
    <li>Armazenar os dados obtidos em um banco de dados</li>
  </ul>

</details>



## Histórico de `Commits`
  * Para ver a evolução do codigo você pode checar o histórico de commits  
  ![Screenshot_9](https://user-images.githubusercontent.com/37710776/229648831-1d560b18-a34f-42bf-91b3-20a44ff2125f.png)
  
  
  
## Como clonar e testar o projeto em sua `maquina`

* Use o comando: `git clone git@github.com:laujuu/Web-scraping-TechNews.git`
* Entre na pasta do repositório que você acabou de clonar:
  * `cd Web-scraping-TechNews`

  2. Crie o ambiente virtual para o projeto

* `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

* `python3 -m pip install -r dev-requirements.txt`


## Como testar a aplicação

Para executar os testes certifique-se de que você está com o ambiente virtual ativado

  <strong>Executar os testes</strong>

  ```bash
python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```
