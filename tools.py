

GOVERNMENT_SCHEMES = {
    "PM-Kisan": {
        "description": "किसानों को वित्तीय सहायता के लिए 6000 रुपये प्रति वर्ष।",
        "min_age": 18,
        "occupation": "farmer",
        "benefits": "6000 INR/year"
    },
    "Ladli Behna": {
        "description": "महिलाओं के आर्थिक सशक्तिकरण के लिए मासिक वित्तीय सहायता।",
        "min_age": 21,
        "max_age": 60,
        "gender": "female",
        "benefits": "1250 INR/month"
    }
}

def get_scheme_info(scheme_name):
    """सरकारी योजना के बारे में विस्तृत जानकारी प्राप्त करें।"""
    return GOVERNMENT_SCHEMES.get(scheme_name, "यह योजना डेटाबेस में नहीं मिली।")

def check_eligibility(age, income, occupation):
    """उपयोगकर्ता की योग्यता की जांच करें (Eligibility Engine)"""
    eligible = []
    for name, details in GOVERNMENT_SCHEMES.items():
       
        if age >= details["min_age"] and (occupation.lower() == details["occupation"]):
            eligible.append(name)
    
    if not eligible:
        return "क्षमा करें, आप वर्तमान में किसी भी योजना के लिए पात्र नहीं हैं।"
    return f"आप इन योजनाओं के लिए पात्र हैं: {', '.join(eligible)}"