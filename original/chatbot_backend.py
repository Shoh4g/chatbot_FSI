import json
from difflib import get_close_matches

def load_knowledgebase(filepath):
    with open(filepath,'r') as file:
        data = json.load(file)
    return data

def save_knowledge_base(file_path,data):
    with open(file_path, 'w') as file:
        json.dump(data,file,indent=2)
        
        
def find_best_match(user_question, questions):
    matches = get_close_matches(user_question, questions,n=1,cutoff = 0.6)
    return matches[0] if matches else None

def get_answer_for_question(question, knowledge_base, current_organization):
    for q in knowledge_base[current_organization]:
        if q['question'] == question:
            return q['answer']
        
        
def chatbot():
    knowledge_base = load_knowledgebase('knowledge_base.json')  # Assuming you have a function to load the knowledge base
    
    current_organization = None  # Initially, no organization is selected
    while True:
        if not current_organization:  # If no organization is selected
            org_input = input("Which organization do you want to know about? ")
            org_input = org_input.strip()
            
            if org_input.lower() == 'quit':
                break
            
            if org_input in knowledge_base:
                current_organization = org_input
            else:
                print("Sorry, organization not found in knowledge base. Please try again or type 'quit' to exit.")
                continue
        
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            break
        
        best_match = find_best_match(user_input, [q['question'] for q in knowledge_base[current_organization]])
        
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base,current_organization )
            print("Bot:", answer)
            
        else:
            print("Unfortunately, I am not aware of the answer. Kindly review your question.")
        
        switch_org_input = input("Would you like to switch to another organization? (yes/no): ")
        if switch_org_input.lower() == 'yes':
            current_organization = None
        elif switch_org_input.lower() == 'no':
            continue
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
            

if __name__ == '__main__':
    chatbot()

    