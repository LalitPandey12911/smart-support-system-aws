import { CONFIG } from "./config.js";

export async function submitTicket(email, feedback) {
  const response = await fetch(CONFIG.API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ email, feedback })
  });

  // If API Gateway returns non-200
  if (!response.ok) {
    const text = await response.text();
    throw new Error(`API Error (${response.status}): ${text}`);
  }

  return await response.json();
}
