import { useState } from "react";
import ChatUI from "./components/ChatUI";
import { sendMessage as apiSendMessage } from "./api";

export default function App() {
  const [messages, setMessages] = useState([
    { role: "bot", text: "👋 Hi! I’m your Real Estate Assistant. Ask me about properties!" },
  ]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (!input.trim()) return;

    // Add user message
    setMessages([...messages, { role: "user", text: input }]);

    try {
      const res = await apiSendMessage(input);
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: res.answer || "No response" },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "bot", text: "❌ Failed to fetch response from server." },
      ]);
    }

    setInput("");
  };

  return <ChatUI messages={messages} input={input} setInput={setInput} sendMessage={handleSend} />;
}
