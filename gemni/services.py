from google.genai import types



def generate_travel_suggestions(form_data, ai_client):
    visitor_type = form_data.get('visitor_type')
    interest = form_data.get('interest')
    time = form_data.get('time')
    budget = form_data.get('budget')
    transport = form_data.get('transport')
    duration = form_data.get('duration')

    sys_instruction = f"""
    You are a travel agent who knows every tourist attraction in Lucknow, like 'Imambada', 'Roomigate', 'Gautam Buddha Park', and more.
    Based on the user's profile, suggest places to visit that suit their preferences.

    User Profile:
    Visitor Type: {visitor_type}
    Interest: {interest}
    Preferred Time: {time}
    Budget: {budget}
    Transport Mode: {transport}
    Duration of Visit: {duration}
    """

    response = ai_client.generate_content(
        model="gemini-2.0-flash", 
        config=types.GenerateContentConfig(system_instruction=sys_instruction),
        contents=["Suggest tourist spots based on the following preferences."]
    )
    return response.text

def format_response(response_text):
    formatted_response = ""
    sections = response_text.split("\n")

    for section in sections:
        section = section.strip()
        if not section:
            continue

        section = section.replace("*", "")
        
        if section.endswith(":"):
            formatted_response += f"<p><b>{section}</b></p>"
        elif section.startswith("    "):
            formatted_response += f"<p style='margin-left: 20px;'>{section.strip()}</p>"
        else:
            formatted_response += f"<p>{section}</p>"

    return formatted_response