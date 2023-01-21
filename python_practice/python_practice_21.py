messages = ['hello', 'greetings', 'hello there', 'welcome home']
sent_messages = []
def show_messages(messages): 
    print(messages)
    
show_messages(messages)

def send_messages(messages, sent_messages): 
    while messages: 
        current_messages = messages.pop()
        sent_messages.append(current_messages)
    print(sent_messages)
    
def show_completed_messsages(sent_messages):
    print(f"The following messages have been sent: ")
    for m in sent_messages:
        print(f"{m.title()}")

send_messages(messages,sent_messages)
show_completed_messsages(sent_messages)

messages = ['hello', 'greetings', 'hello there', 'welcome home']
sent_messages = []

print(messages)
show_messages(messages)

"""
The messages match one another as shown in the output window 
"""

