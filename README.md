# ecapybara-api
ecapybara-api, a Flask API using Elementary Cellular Automata for PYthon + BARA

Iterate the 256 [elementary cellular automata](https://en.wikipedia.org/wiki/Elementary_cellular_automaton)
starting from a fixed inital state (center cell 'live', all others 'dead'). Display in a web browser.

## Usage

### API mode

Run locally as an API with results displayed in the browser. Non-public/non-production uses ONLY.

### Docker method
```
docker pull nrejack/ecapybara-api:latest
docker run --rm --name ecapy -p 5000:5000 -d  nrejack/ecapybara-api:latest
```
or build locally:

```
git clone git@github.com:nrejack/ecapybara-api.git
cd ecapybara-api
docker build -t nrejack/ecapybara-api:latest .
docker run --rm --name ecapy -p 5000:5000 -d  nrejack/ecapybara-api:latest
```
Follow the "How to view" browser instructions below. Note that the container will be destroyed (--rm) when you stop it.

### pip method

```
git clone git@github.com:nrejack/ecapybara-api.git
cd ecapybara-api
python3 -m venv venv  
. venv/bin/activate  
pip install -U pip flask  
flask run
```
### How to view API output
Open a browser on the machine and navigate to http://localhost:5000. 
Select a *rule* (0 - 255) and *number of iterations* (maximum 1000), and access http://localhost:5000/rule/iterations/ in your browser.  
**Example:** Rule 30, 500 iterations: http://localhost:5000/30/500/ 

## TODO
- Larger number of steps doesn't generate expected output.
- Needs to be modularized.
- Needs unit tests.
- Needs click interface for CLI.
- Needs to write images using PILlow.
- Logging needs work.
- Streaming from API not working
- Needs some JS or other trickery to get browser window width
- Add ability to scale fundamental elements
- Add ability to 'page' back and forth between different rules in browser view
- Programmatically generate visual representation of rules
- Needs ability to start from randomized seed
- COLORS !!!
- Animation modes (fades, slow transitions)

## Mascot
The official mascot of ecapybara is the e-capybara.

![e-capybara, our mascot](img/capy.jpg)
