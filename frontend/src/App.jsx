import { useState } from "react";
import ChatUI from "./components/ChatUI";
import { sendMessage as apiSendMessage } from "./api";

export default function App() {
  const [messages, setMessages] = useState([
    { role: "bot", text: "Hi! I'm your AI Assistant. Choose a mode and ask me anything!" },
  ]);
  const [input, setInput] = useState("");
  const [mode, setMode] = useState("rag"); // "rag" or "sql"
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage = input;
    setInput("");
    setMessages((prev) => [...prev, { role: "user", text: userMessage }]);
    setIsLoading(true);

    try {
      const res = await apiSendMessage(userMessage, mode);
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: res.answer || "No response" },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: "Failed to fetch response. Is the server running?" },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <ChatUI
      messages={messages}
      input={input}
      setInput={setInput}
      sendMessage={handleSend}
      mode={mode}
      setMode={setMode}
      isLoading={isLoading}
    />
  );
}
