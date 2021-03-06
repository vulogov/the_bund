BUND_GRAMMAR="""
Bund:
  functors *= Functor
;

Statement:
  Functor
;

Comment:
  /\/\/.*$/
;

Keyword:
  'let' | '.' | 'is' | 'not' | 'more' | 'less' | 'match' | 'nomatch'
;

BUND_ID:
  !Keyword ID
;

State:
  BASETYPE | Statement | Fact
;

Call:
  BUND_ID ('.' BUND_ID)*
;

Statement:
  '('
      call *= Call
      state *= State
  ')'
;

FunctorStatements:
  '('
    name=BUND_ID
    state*=State
    facts*=Fact
  ')'
;

FunctorsIfTrue:
  'f!'
    functors *= FunctorStatements
  '.'
;

FunctorsIfFalse:
  '~f'
    functors *= FunctorStatements
  '.'
;

FunctorsExecStatements:
  FunctorsIfTrue | FunctorsIfFalse
;

FunctorsMany:
  'do'
    name=BUND_ID
    do_fact=Fact
    functors *= FunctorsExecStatements
  '.'
;

FactElementStatement:
  'is' | 'not' | 'more' | 'less' | 'match' | 'nomatch'
;

FactElement:
  varname=BUND_ID
  statement=FactElementStatement
  state*=State
;

Fact:
  '{'
    fact_elements *= FactElement
  '}'
;

Queue:
  '['
    name=BUND_ID
    'of'
    type=BUND_ID
    property*=Fact
  ']' ('->')*
    facts *= Fact
  ';;'
;

StatementOrFactOrQueue:
  Statement | Fact | Queue | FunctorsIfTrue | FunctorsIfFalse | FunctorsMany
;

Functor:
  'let' name=BUND_ID '->'
      statements += StatementOrFactOrQueue
  ';;'
;
"""
