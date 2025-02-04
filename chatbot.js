// Initialize chatbot
document.addEventListener("DOMContentLoaded", function() {
  let link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = 'https://me-junaid.github.io/run-start/chatbot.css'; // Path to your CSS file
document.head.appendChild(link);

  // Create a simple chat container
  const chatContainer = document.createElement("div");
  chatContainer.setAttribute("id", "chatbot");
  document.body.appendChild(chatContainer);

  // Chatbot UI elements
  const chatBox = document.createElement("div");
  chatBox.setAttribute("id", "chat-box");
  chatContainer.appendChild(chatBox);

  const userInput = document.createElement("input");
  userInput.setAttribute("id", "user-input");
  userInput.setAttribute("placeholder", "Ask me something...");
  chatContainer.appendChild(userInput);

  const sendButton = document.createElement("button");
  sendButton.innerHTML = "Send";
  sendButton.setAttribute("id", "send-button");
  chatContainer.appendChild(sendButton);

  // Simple chatbot responses
  const responses = {
    "hello": "Hi! How can I help you today?",
    "how are you": "I'm just a chatbot, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a nice day!",
    "default": "Sorry, poddo"
  };

  // Function to display messages in the chat box
  function displayMessage(content, sender) {
    const message = document.createElement("div");
    message.classList.add(sender);
    message.innerText = content;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
  }

  // Handle user input
  sendButton.addEventListener("click", function() {
    const userText = userInput.value.trim().toLowerCase();
    if (userText) {
      displayMessage(userText, "user");

      // Respond based on user input
      let botResponse = responses[userText] || responses["default"];
      displayMessage(botResponse, "bot");

      // Clear input field after sending message
      userInput.value = "";
    }
  });

  // Optional: Send message when "Enter" is pressed
  userInput.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
      sendButton.click();
    }
  });
});
