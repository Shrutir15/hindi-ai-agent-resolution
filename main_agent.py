import os
import time
from groq import Groq
from dotenv import load_dotenv
from tools import get_scheme_info, check_eligibility
from voice_engine import listen_hindi, speak_hindi

# Load environment variables
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Conversation memory to handle context
chat_history = []

def run_agentic_system():
    # Initial Greeting
    speak_hindi("नमस्ते, मैं आपकी कैसे सहायता कर सकता हूँ?")
    
    while True:
        # 1. VOICE INPUT
        user_input = listen_hindi()
        
        # --- NEW: STOP COMMAND LOGIC ---
        # If user says stop or goodbye, the program exits gracefully
        if user_input and any(word in user_input.lower() for word in ["बंद करो", "अलविदा", "शुक्रिया", "stop", "exit"]):
            speak_hindi("सहायता करने में ख़ुशी हुई। अपना ख्याल रखें, अलविदा!")
            print("\n[SYSTEM]: Program stopped by user.")
            break

        if not user_input:
            speak_hindi("क्षमा करें, मुझे सुनाई नहीं दिया। क्या आप फिर से बोल सकते हैं?")
            continue
        
        # Add to memory
        chat_history.append({"role": "user", "content": user_input})

        # 2. THE PLANNER-EXECUTOR-EVALUATOR BRAIN
        
        system_prompt = f"""
        आप एक 'CRED Resolve' सरकारी योजना सहायक हैं।
        
        आपको 'Planner-Executor-Evaluator' चक्र का पालन करना चाहिए:
        1. योजना (Plan): विश्लेषण करें कि उपयोगकर्ता को क्या चाहिए।
        2. निष्पादन (Execute): टूल (get_scheme_info या check_eligibility) के उपयोग पर विचार करें।
        3. मूल्यांकन (Evaluate): सुनिश्चित करें कि जवाब स्पष्ट और मददगार है।
        
        महत्वपूर्ण नियम:
        - आपकी पूरी 'Thinking' और 'Reasoning' (विचार और योजना) केवल हिंदी में होनी चाहिए।
        - यदि जानकारी अधूरी है, तो टूल का उपयोग न करें, बल्कि उपयोगकर्ता से सवाल पूछें।
        
        इतिहास (Context): {chat_history[-3:]} 
        """

        print("\n--- AGENT IS THINKING (Planner-Executor-Evaluator) ---")
        
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ]
            )
            
            agent_reply = response.choices[0].message.content
            
            
            print(f"\n--- तर्क और योजना (Reasoning & Plan) ---\n{agent_reply}")
            
           
            speak_hindi(agent_reply)
            chat_history.append({"role": "assistant", "content": agent_reply})
            
        except Exception as e:
            print(f"Error connecting to Groq: {e}")
            speak_hindi("क्षमा करें, मेरे सर्वर में कुछ समस्या है।")

if __name__ == "__main__":
    run_agentic_system()