Architecture Document: Native Hindi Voice-Agentic System
1. Objective
This document details the architecture of a voice-first, agentic AI system built to help users identify and apply for government welfare schemes in native Hindi. The system is designed with a Planner-Executor-Evaluator loop to ensure autonomous reasoning, tool usage, and robust failure handling.




2. Agent Lifecycle & Decision Flow
The system operates through a circular lifecycle to ensure the agent "reasons" before it "acts":


Step 1: Voice-First Input (STT): User audio is captured and processed through a Speech-to-Text pipeline to convert Hindi voice into text.

Step 2: Planner (Llama 3.3 Agent Brain): The agent analyzes the Hindi text and determines the user's intent. It consults the Conversation Memory to check if current details (like age or occupation) conflict with previous turns.



Step 3: Executor (Tool Usage): The agent identifies which tools are required. It triggers the Eligibility Engine or Mock APIs to retrieve real-time data on available schemes.


Step 4: Evaluator (Verification & Failure Handling): The system evaluates the tool output. If the information is incomplete or contradicts stored memory, the agent enters a failure-recovery loop to ask for clarification instead of providing a wrong answer.





Step 5: Voice Output (TTS): The final reasoned response is converted back into native Hindi speech for a seamless voice interaction.

3. Core Technical Components
 Conversation Memory & State Machine

Turn-by-Turn Memory: The agent stores all interaction history to handle follow-up questions (e.g., "What about my wife's eligibility?") without the user needing to repeat data.




Contradiction Logic: The system is programmed to identify logical errors (e.g., if a user born in 1980 says they are 20 years old), fulfilling the requirement for handling contradictions across turns.



 Tool Integration

Eligibility Engine: A custom tool that maps user demographics (age, gender, occupation, income) to a database of government schemes.


Mock API System: Simulates external government database calls to demonstrate the agent's ability to "act" autonomously.

 Failure Handling & Edge Cases

Recognition Errors: If the STT module receives low-confidence input, the agent is prompted to ask the user to repeat the request in Hindi.
4. System Diagram
Below is the visual representation of the agent lifecycle, showing the stateful loop between the User, the LLM Brain, and the supporting Tools.




Incomplete Data: If the user asks for a scheme but hasn't provided their age, the Evaluator stops the process and prompts the agent to collect the missing data points first.
