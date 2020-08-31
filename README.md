# OLB2 Node & Presentation File Generator - WIP
use this to generate view nodes and view presentations files for a new page in CA, TX, or both states and never worry about foretting to import this or export that again!

## What you'll need
- python3
- python-dotenv (pip package)

## Get Started
- create a `.env` file
- add `GRAPH_PATH` env variable in your `.env` file as the path to the Graph directory in your OLB2 project
- `pip3 install python-dotenv`

## How to use
- run `python3 program.py`
- `page name: `
  - input name of new page
  - ie. `someOtherDiscount`
- `which flow (ie. driver, coverage, etc...): `
  - can only handle existing flow
- `which version (ie. default, excludeDriver, etc...): `
  - can only handle existing version
- `What file type? [N]ode, [P]resentation, or [B]oth: `
  - input `N` for new node files, `P` for new presentation files, or `B` for both
  - for if you only want to create one file without the other
- `What state? [CA], [TX], or [B]oth: `
  - input `CA` for California, `TX` for Texus, or `B` for both
  - for if you only want to create file at one state and not the other
- profit
- DONE SON!
### currently only update one graph at a time, change env variable to update the other graph


## Coming soon
- input error handling
  - does not handle random / invalid user inputs
- update the view node graph
  - currently require manual update to the view node graphs
- create folder structure if it does not exist
  - ie. new flow, version, etc...
