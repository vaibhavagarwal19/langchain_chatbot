const API_BASE = "http://localhost:8000";

export async function sendMessage(question, mode = "rag") {
  const response = await fetch(`${API_BASE}/chat`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question, mode }),
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.detail || "Failed to fetch response from server");
  }

  return await response.json();
}

export async function clearHistory() {
  const response = await fetch(`${API_BASE}/history`, {
    method: "DELETE",
  });
  return await response.json();
}

export async function healthCheck() {
  const response = await fetch(`${API_BASE}/health`);
  return await response.json();
}
