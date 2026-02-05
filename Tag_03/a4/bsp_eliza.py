import random

patterns = [
    ("I need", ["Why do you need that?", "What would you do if you had it?"]),
    ("I feel", ["Why do you feel that way?", "Tell me more about your feelings."]),
    ("I think", ["Why do you think that?", "How does that thought make you feel?"]),
    ("", ["I understand.", "Could you explain more?", "How does that make you feel?"])
]

def generate_response(user_input):
    for pattern, responses in patterns:
        if user_input.startwith(pattern):
            response = random.choice(responses)
            return response
        
    return "I'm sorry, could you repeat that?"
import random

patterns = [
    ("I need", ["Why do you need that?", "What would you do if you had it?"]),
    ("I feel", ["Why do you feel that way?", "Tell me more about your feelings."]),
    ("I think", ["Why do you think that?", "How does that thought make you feel?"]),
    ("", ["I understand.", "Could you explain more?", "How does that make you feel?"])
]

def generate_response(user_input):
    for pattern, responses in patterns:
        if user_input.startwith(pattern):
            response = random.choice(responses)
            return response
        
    return "I'm sorry, could you repeat that?"

# MAIN 
print("ELIZA: Hi! How can I help you today?")
while True:
    user_input = input("You: ")
    response = generate_response(user_input)
    print("ELIZA:", response)