print("------------------Chapter 8, Exercise 8-9 & 8-10 & 8-11---------------------------")
#def show_messages(messages):
#    for message in messages:
#        print(message) 

#messages= ['BRB', 'LOL', 'Call me?', 'TTYL', 'wyd?']
#show_messages(messages)

def show_messages(messages):
    """Print all messages in list"""
    print("Showing all messages:")
    for message in messages:
        print(message) 

def send_messages(messages, sent_messages):
    """Print sent messages from list"""
    print("\nThe following messages have been sent:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages= ["Call me?","wyd?","BRB", "TTYL" ]
show_messages(messages)

sent_messages =[]
send_messages(messages, sent_messages)

print("\nArchived Messages:")
print(messages)
print(sent_messages)