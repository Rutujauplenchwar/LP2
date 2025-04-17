import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Chatbot pairs
pairs = [
    # General Greeting and Store Introduction
    [
        r"Hi|Hello|Hey|hi|hello",
        ["Hello! Welcome to our online bookstore. How can I assist you today?", "Hey there! How may I help you today?"]
    ],
    [
        r"quit",
        ["Thank you for visiting. Goodbye!", "It was nice chatting with you. Goodbye!"]
    ],
    
    # Best-Selling Books
    [
        r"(.*) best-selling books?",
        ["Our best-selling books right now include 'The Alchemist,' '1984,' and 'Harry Potter.' Would you like to know more?", "Here are some best-sellers: 'The Catcher in the Rye,' 'The Hobbit,' and 'Pride and Prejudice.'"]
    ],
    [
        r"(.*) top-selling books?",
        ["Our top-selling books this month are 'The Great Gatsby,' 'The Hunger Games,' and 'To Kill a Mockingbird.'"]
    ],
    
    # Book Genre Questions
    [
        r"(.*) books on mystery?",
        ["Yes, we have a wide selection of mystery books like 'Sherlock Holmes' and 'The Girl with the Dragon Tattoo.' Would you like a recommendation?", "We have many mystery books, such as 'The Hound of the Baskervilles' and 'Gone Girl.'"]
    ],
    [
        r"(.*) fiction books?",
        ["We offer a great collection of fiction books. You can check out 'The Great Gatsby' or '1984.' Do you have a specific author or genre in mind?", "Our fiction section has popular books like 'Pride and Prejudice' and 'The Catcher in the Rye.' Would you like a recommendation?"]
    ],
    [
        r"(.*) science fiction books?",
        ["We offer some exciting science fiction books like 'Dune,' 'The Martian,' and 'Neuromancer.' What are you looking for specifically?", "We have many great science fiction novels, such as 'Foundation' and 'Brave New World.'"]
    ],
    [
        r"(.*) romance books?",
        ["We have a large collection of romance books, including 'Pride and Prejudice' and 'The Fault in Our Stars.' Would you like suggestions?", "We offer many great romance novels like 'The Notebook' and 'Me Before You.'"]
    ],
    
    # Book Availability
    [
        r"(.*) is [A-Za-z ]+ available?",
        ["Yes, we have '%1' in stock. Would you like to place an order?", "I believe we have '%1' in stock! Would you like to check out the details?"]
    ],
    
    # Book Price
    [
        r"(.*) price of [A-Za-z ]+?",
        ["The price of '%1' is $9.99. Would you like to know more about it?", "The price of '%1' is $15.00. Would you like to proceed with an order?"]
    ],
    
    # Book Recommendations
    [
        r"(.*) recommend a book in [A-Za-z ]+?",
        ["I recommend 'The Catcher in the Rye' for a classic fiction experience. Would you like to know more?", "If you enjoy mystery, I recommend 'The Girl with the Dragon Tattoo.' How does that sound?"]
    ],
    [
        r"(.*) recommend a good [A-Za-z]+ book?",
        ["If you're looking for a great [genre] book, I suggest 'The Hobbit' or 'The Hunger Games.'", "For [genre] books, '1984' and 'Brave New World' are fantastic options."]
    ],
    
    # Author-Specific Questions
    [
        r"(.*) books by [A-Za-z ]+?",
        ["We have books by J.K. Rowling, such as 'Harry Potter and the Sorcerer's Stone.' Would you like to explore more?", "We carry works by George Orwell, including '1984' and 'Animal Farm.'"]
    ],
    
    # New Arrivals
    [
        r"(.*) new arrivals?",
        ["Our newest arrivals include 'The Midnight Library' and 'The Invisible Life of Addie LaRue.' Would you like to check them out?", "We have fresh arrivals like 'The Vanishing Half' and 'Project Hail Mary.'"]
    ],
    
    # Ordering Books
    [
        r"(.*) order a book?",
        ["You can order any book directly through our website. Would you like to add a specific book to your cart?", "To order a book, simply visit our website and follow the checkout process. Let me know if you need help!"]
    ],
    
    # Payment Methods
    [
        r"(.*) payment methods?",
        ["We accept credit cards, PayPal, and other secure payment methods. Would you like help with the checkout?", "We support payments via credit card, debit card, and PayPal. Let me know if you need assistance."]
    ],
    
    # Tracking Orders
    [
        r"(.*) track my order?",
        ["You can track your order by visiting the 'My Orders' section of our website. Let me know if you need more help!", "To track your order, go to the 'Track Order' page on our website and enter your order number."]
    ],
    
    # Return and Refund Policy
    [
        r"(.*) return policy?",
        ["Our return policy allows returns within 30 days of purchase. For more details, visit our Returns page or let me know how I can assist you.", "We accept returns within 30 days of purchase. You can return books in new condition."]
    ],
    
    # Discount and Offers
    [
        r"(.*) discount available?",
        ["We have a limited-time 10% discount on all books! Use code 'READ10' at checkout.", "We have a seasonal sale with discounts of up to 20%. Would you like to browse the sale items?"]
    ],
    
    # Book Formats (E-books, Audiobooks)
    [
        r"(.*) e-books?",
        ["Yes, we have a wide collection of e-books. Would you like to know about the best e-books we offer?", "We offer many books in e-book format. You can download them directly after purchase."]
    ],
    [
        r"(.*) audiobooks?",
        ["We have a collection of audiobooks available. Would you like a recommendation?", "Yes, we also sell audiobooks. You can listen to them directly through our website."]
    ],
    
    # Customer Service
    [
        r"(.*) customer service?",
        ["You can reach our customer service by emailing support@bookstore.com or visiting our Help Center. How can I assist you today?", "For customer service, feel free to contact us at support@bookstore.com or use the live chat on our website."]
    ],
    
    # Gift Cards
    [
        r"(.*) gift cards?",
        ["We offer gift cards in various denominations. Would you like to purchase one for someone special?", "Yes, we have gift cards! You can buy them directly on our website."]
    ],
    
    # Subscription / Book Club
    [
        r"(.*) book club?",
        ["We offer a book club subscription! You'll get monthly book recommendations and discounts. Would you like to subscribe?", "Join our book club and receive monthly book picks and exclusive discounts! Let me know if you're interested."]
    ]
]



def chatbot_response(user_input):
    chatbot = Chat(pairs, reflections)
    response = chatbot.respond(user_input)
    return response if response else "I'm sorry, I didn't understand that. Could you ask something else?"

# Function to handle user interaction
def on_send_click():
    user_input = user_input_box.get()
    if user_input.lower() == "quit":
        window.quit()
        return
    
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n", 'user')
    response = chatbot_response(user_input)
    chat_window.insert(tk.END, f"Chatbot: {response}\n\n", 'bot')
    user_input_box.delete(0, tk.END)
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)

# Create the main window
window = tk.Tk()
window.title("Online Bookstore Chatbot")

# Set the background color and window size
window.config(bg='#f0f0f0')

# Make the window responsive
window.grid_rowconfigure(0, weight=1, minsize=100)  # Header row (with welcome message)
window.grid_rowconfigure(1, weight=6)  # Chat window
window.grid_rowconfigure(2, weight=1, minsize=50)  # Input row (for text entry and button)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=0)

# Create a welcome label at the top
header_label = tk.Label(window, text="Welcome to the Online Bookstore!", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white", anchor="w", padx=10)
header_label.grid(row=0, column=0, columnspan=2, sticky="w", pady=(10, 0))

# Create a scrollable chat window with customized colors and fonts
chat_window = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED, bg="#f8f8f8", fg="#333", font=("Arial", 12))
chat_window.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Add custom tags for user and bot messages
chat_window.tag_configure("user", foreground="blue", font=("Arial", 12, "bold"))
chat_window.tag_configure("bot", foreground="green", font=("Arial", 12, "italic"))

# Create a text box for user input
user_input_box = tk.Entry(window, width=40, font=("Arial", 12), bd=2, relief="solid", fg="#555", bg="#e0e0e0")
user_input_box.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Create a send button with a modern look
send_button = tk.Button(window, text="Send", width=20, height=2, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), command=on_send_click)
send_button.grid(row=2, column=1, padx=10, pady=10)

# Make the input and send button row responsive
window.grid_columnconfigure(0, weight=1)  # Allow the input box to expand
window.grid_columnconfigure(1, weight=0)  # Keep the send button fixed width

# Start the Tkinter main loop
window.mainloop()