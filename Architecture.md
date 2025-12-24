1. System Overview
"This system is a Voice-First Native Language Service Agent designed to assist users with government scheme identification. It utilizes a Planner-Executor-Evaluator loop to ensure logical consistency and native-language reasoning throughout the pipeline."


2. The Agent Lifecycle (Decision Flow)
Explain the flow step-by-step:


Step 1: Voice Input (STT): Converts Hindi audio to text.


Step 2: Planner (Llama 3.3 via Groq): The "Brain" analyzes the user's intent and current state.


Step 3: Tool Execution: If the Planner needs data, it calls specific Python tools (e.g., check_eligibility).


Step 4: Evaluator: The agent verifies if the tool output satisfies the user’s request or if more information is needed.



Step 5: Voice Output (TTS): Converts the final reasoning into Hindi speech.

3. Memory & State Management
Explain how you handle long conversations:


Context Window: The agent stores previous turns of the conversation to handle follow-up questions.


Contradiction Logic: The Planner is prompted to compare new user input against stored memory to flag inconsistencies (e.g., age vs. birth year).

4. Failure Handling Mechanisms
"To prevent system crashes or 'looping,' the agent includes:"


Ambiguity Check: If STT confidence is low, the agent asks for clarification in Hindi.




Fallback Logic: If no scheme is found, the agent suggests related categories instead of giving a hard "No".
