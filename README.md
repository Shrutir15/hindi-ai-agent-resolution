# Hindi AI Agent Resolution: Voice-First Government Scheme Assistant

A state-of-the-art Voice-First AI Agent designed for native Hindi speakers to discover and verify eligibility for government schemes.

##  Agentic Architecture: Planner-Executor-Evaluator
Unlike standard chatbots, this agent uses a sophisticated reasoning loop to ensure accuracy in native Hindi:
- **Planner:** The agent analyzes the user's voice input and creates a step-by-step plan in **Hindi Script** to determine eligibility.
- **Executor:** Calls custom Python tools (`tools.py`) to verify user data against scheme requirements.
- **Evaluator:** Reviews the tool output to ensure the final response is helpful and culturally appropriate.

##  Key Features
- **Native Hindi Reasoning:** All internal logic and planning are processed in Hindi to maintain context.
- **Voice-First Interface:** Integrated end-to-end Speech-to-Text and Text-to-Speech.
- **Dynamic Tool Use:** A modular eligibility engine that can be scaled to hundreds of schemes.

##  How to Run
1. **Clone the Repo:** `git clone []`
2. **Install Dependencies:** `pip install -r requirements.txt`
3. **Set API Key:** Create a `.env` file and add `GROQ_API_KEY=your_key_here`.
4. **Launch:** Run `python main_agent.py`.


