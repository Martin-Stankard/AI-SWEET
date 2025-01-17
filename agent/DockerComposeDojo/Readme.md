# Design Document

## Agent Use Principle

### Initial "1000 Points" of General Software Creation

**Agent 1**: Given a 5-sentence start, "I want a webapp that..."
- Returns: A sophisticated, long-winded, technical outline.
- `docker-compose up` runs a test server or utility server, and localstack/AWS consideration early and often.
- No search; no RAG (Retrieval-Augmented Generation).

**Agent 2**: Given a shopping list of topics to cover with RAG 
- Takes the outline and looks for RAG population needs, if not explicit
- Returns:
  - A list of links to scrape.
  - PDFs, CSVs.
  - Uses search for a focused "list of stuff to search" without getting out of control.
  - in flowise
  - automate into rag upsert? ambitious atm.

**Agent 3**: Given the technical outline, create code. 
 - hands on after docker compose up, runs tests, plus demo postman automation?
 - start here...does it all
 - uses rag, 
 - creates code and directories 
 - obvious git milestones in a new branch  

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