# Language-Agents-Playing-Language-Games
How do popular language model perform in common strategies language games against other models or even humans? Will their performance substantially improve if we incorporate ReAct, COT, and persistent memory?

## Next steps:  
Trying to build a web interface to show agents playing the game, and include an option for human players to compete with them

## Running the Demo Web UIs

Simple React interfaces are provided for Akinator and Imposter under
`Akinator/web` and `Imposter/web`. They do not require any build tools. Start a
local web server from each folder and open the page in your browser:

```bash
cd Akinator/web
python -m http.server
# then visit http://localhost:8000

cd ../../Imposter/web
python -m http.server
# then visit http://localhost:8000
```

## Games Overview

### Game 1 Akinator
- **Game Rules**  
  Akinator, following the popular website game, attempts to guess a character based on a series of yes/no/maybe questions. The LLM agent must narrow down possibilities using minimal queries.
- **Agent Behavior Design**  
  On average the Akinator agent, with employing chain of thought and tools of online search, performs 7 rounds earlier than the Akinator game.

### Game 2 Mafia （狼人杀 in Chinese）
- **Game Roles and Rules**  
  Classic social deduction game with roles like Killer, Detective, Peasants, and a Referee. This game includes complex strategies of speech, lieing (and telling lies), strategic voting and actions ..etc. Alternates between Day (discussion/voting) and Night (actions, eliminating players). -- can read full description at https://playwerewolf.co/pages/rules  
- **Agent Behavior Design**
  Instead of constraining the game, the design is mostly unconstrained with a referee agent tallying the votes, eliminating players, warning players of misbehaviour...etc.  
  Memory and scope: each agent was provided with memory relevant to their role, with in time summary, reflection, and augmentation of each rounds' new information.  
  On each voting and discussion round agents are prompted for Chain of thought and retreival + summary of their memories.  
  Detective 'detect action' and killers 'kill action' are also promopted to follow chain of thought and reflection  
  

### Game 3 Imposter （谁是卧底 in Chinese）
- **Game Roles and rules**  
  Similar to Mafia but with dynamic deduction, simpler rules, more attention paid to not making mistake in speech and cathing others' mistake, rules are found in : https://whoisspy.ai/#/
- **Agent Behavior Design**  
  Similar to Mafia, with more emphasis and reflection put on not making mistake to be caught and greater emphasis putting on recording and analyzing other agents speech
  Memory processed to include more detailed depiciton of other agents past interactions  
