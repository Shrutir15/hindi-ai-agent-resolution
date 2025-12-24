Evaluation Transcript: Native Hindi Service Agent
This document provides a transcript of test cases conducted to verify the agent's reasoning, tool usage, memory, and failure handling capabilities. All interactions were performed end-to-end in Hindi.


1. Successful Interaction (Goal Completion)

Scenario: User provides clear information and the agent identifies a matching scheme.

User: "नमस्ते, मैं एक किसान हूँ और मेरी उम्र 40 साल है। क्या मेरे लिए कोई सरकारी योजना है?" (Namaste, I am a farmer and my age is 40. Is there any government scheme for me?) 


Agent Brain (Planner): User is a farmer, age 40. Need to check agricultural eligibility.



Tool Call: check_eligibility(occupation="farmer", age=40) 

Agent Output (TTS): "आपकी जानकारी के अनुसार, आप PM-Kisan योजना के लिए पात्र हैं। क्या आप आवेदन करने की प्रक्रिया जानना चाहेंगे?" (According to your info, you are eligible for PM-Kisan. Would you like to know the application process?) 

2. Failure Handling (Incomplete Information/Out of Scope)

Scenario: User asks for something the agent cannot do or provides gibberish.


User: "मुझे पिज्जा आर्डर करना है।" (I want to order a pizza.)


Agent Brain (Planner): Request is outside the scope of government welfare schemes.


Failure Recovery: "क्षमा करें, मैं केवल सरकारी और जन कल्याण योजनाओं में आपकी मदद कर सकता हूँ। क्या मैं आपकी खेती, स्वास्थ्य या पेंशन से जुड़ी किसी योजना में मदद करूँ?" (Sorry, I can only help with government and welfare schemes. Can I help with farming, health, or pension schemes?) 

3. Edge-Case: Handling Contradictions (Memory Test)

Scenario: User provides conflicting data across different turns of the conversation.


User (Turn 1): "मेरी उम्र 20 साल है।" (My age is 20.)

Agent: "ठीक है, मैंने नोट कर लिया है। आप क्या काम करते हैं?" (Got it, noted. What work do you do?)

User (Turn 2): "मैं एक रिटायर कर्मचारी हूँ, मेरा जन्म 1960 में हुआ था।" (I am a retired employee, I was born in 1960.)


Agent Brain (Planner): CONTRADICTION DETECTED. User previously said age 20, but birth year 1960 implies age 64+.

Agent Output: "क्षमा करें, आपने पहले अपनी उम्र 20 साल बताई थी, लेकिन 1960 के जन्म वर्ष के हिसाब से आपकी उम्र 64 वर्ष होनी चाहिए। क्या आप अपनी सही उम्र की पुष्टि कर सकते हैं?" (Sorry, you previously said your age is 20, but based on 1960, it should be 64. Can you confirm your correct age?) 

4. Edge-Case: Recognition Error Recovery

Scenario: The STT module fails to capture clear text.

User: "[Background Noise / Unclear Audio]"


Agent Evaluator: Input confidence low.


Agent Output: "माफ कीजिये, मैं आपकी बात ठीक से समझ नहीं पाया। क्या आप कृपया अपनी बात फिर से दोहरा सकते हैं?" (Sorry, I couldn't understand you properly. Could you please repeat yourself?)
