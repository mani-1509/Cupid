const chatBox = document.getElementById("chat-box");
const options = document.getElementById("options");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

let conversation = [];

// Add clickable options to the chat
options.querySelectorAll(".option").forEach((option) => {
  option.addEventListener("click", () => {
    const response = option.getAttribute("data-response");
    addMessage("user", response);
    sendResponse(response);
  });
});

// Send user input
sendBtn.addEventListener("click", () => {
  const response = userInput.value.trim();
  if (response) {
    addMessage("user", response);
    sendResponse(response);
    userInput.value = "";
  }
});

// Add a message to the chat box
function addMessage(role, content) {
  const message = document.createElement("div");
  message.classList.add("message", role);

  if (role === "assistant") {
    // Render Markdown for AI responses
    message.innerHTML = marked.parse(content);
  } else {
    message.textContent = content;
  }

  chatBox.appendChild(message);
  chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll
}

// Send user response to the server
async function sendResponse(response) {
  conversation.push({ role: "user", content: response });

  const res = await fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: response, conversation }),
  });

  const data = await res.json();
  conversation = data.conversation;
  addMessage("assistant", data.response);
}
