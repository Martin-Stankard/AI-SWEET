# Design Document

## Agent Use Principle

### Initial "1000 Points" of General Software Creation

**Agent 1**: Given a 5-sentence start, "I want a webapp that..."
- Returns: A sophisticated, long-winded, technical outline.
- `docker-compose up` runs a test server or utility server, and localstack/AWS consideration early and often.
- No search; no RAG (Retrieval-Augmented Generation).
- probably agentone.py here. config.json is a 1000 points start.

**Agent 2**: Given a shopping list of topics to cover with RAG 
- Takes the outline and looks for RAG population needs, if not explicit
- Returns:
  - A list of links to scrape.
  - PDFs, CSVs.
  - Uses search for a focused "list of stuff to search" without getting out of control.
  - in flowise
  - automate into rag upsert? ambitious atm.
  - probably flowise rag management 

**Agent 3**: Given the technical outline, create code. 
 - hands on after docker compose up, runs tests, plus demo postman automation?
 - start here...does it all
 - uses rag, 
 - creates code and directories 
 - obvious git milestones in a new branch
 - hopefully flowise  

Test manual here, docker compose up ==
    - unit tests run
    - postman config is ready to be used and already ran automated
    - manual local use and tests time.

**Agent 4**: Given all of the docs and a docker compose up someting, 
    - debug
    -- possibly just create a report for the next guy.
    -- think in terms of options == branches
    -- best option might be revert to x?/debug report is bad news/don't touch code here?

**Agent 5**: take agent 4 report OR new feature request
    - fix/touch code
    - new feature == auto gen tests

Test manual here, docker compose up ==
    - unit tests run
    - postman config is ready to be used and already ran automated
    - manual local use and tests time.


TODO/next level is deploy to aws. 
- move local tests to cloud
- if those are happy then move to aws
- pie in the sky at this point is a docker compose up , control app with big stuipid button DEPLOY!!!
-- have a blue green something...probably inherent to "add new feature" swiss army knife of support utility binding/pluding/pita...