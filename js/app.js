import { submitTicket } from "./api.js";

const form = document.getElementById("ticketForm");
const statusDiv = document.getElementById("status");
const submitBtn = document.getElementById("submitBtn");

function setStatus(message, type) {
  statusDiv.textContent = message;
  statusDiv.className = "status";
  if (type) statusDiv.classList.add(type);
}

function setLoading(isLoading) {
  if (isLoading) {
    submitBtn.classList.add("loading");
    submitBtn.disabled = true;
  } else {
    submitBtn.classList.remove("loading");
    submitBtn.disabled = false;
  }
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const feedback = document.getElementById("feedback").value.trim();

  if (!email || !feedback) {
    setStatus("Please fill in all fields.", "error");
    return;
  }

  setStatus("");
  setLoading(true);

  try {
    await submitTicket(email, feedback);
    setStatus("✅ Ticket submitted successfully. Our team will contact you.", "success");
    form.reset();
  } catch (err) {
    console.error(err);
    setStatus("❌ Failed to submit ticket. Please try again.", "error");
  } finally {
    setLoading(false);
  }
});
