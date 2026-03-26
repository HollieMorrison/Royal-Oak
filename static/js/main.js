// static/js/main.js
// Blocks past dates in the booking form.
// Live booking summary update as the user chooses date/time/party size.


document.addEventListener("DOMContentLoaded", function () {
  // ---- 1. Prevent booking dates in the past ----
  const dateInput = document.querySelector("#id_date");
  if (dateInput) {
    const today = new Date().toISOString().split("T")[0];
    dateInput.setAttribute("min", today);
  }

  // ---- 2. Live booking summary (date, time, party size) ----
  const timeInput = document.querySelector("#id_time");
  const partySizeInput = document.querySelector("#id_party_size");
  const summaryBox = document.querySelector("#booking-summary");

  function updateSummary() {
    if (!summaryBox) return;

    const dateVal = dateInput ? dateInput.value : "";
    const timeVal = timeInput ? timeInput.value : "";
    const partyVal = partySizeInput ? partySizeInput.value : "";

    if (!dateVal && !timeVal && !partyVal) {
      summaryBox.textContent =
        "Your booking details will appear here as you fill in the form.";
      return;
    }

    summaryBox.textContent = `You are booking ${
      partyVal || "?"
    } guest(s) on ${dateVal || "a chosen date"} at ${
      timeVal || "a chosen time"
    }.`;
  }

  if (dateInput) dateInput.addEventListener("change", updateSummary);
  if (timeInput) timeInput.addEventListener("change", updateSummary);
  if (partySizeInput) partySizeInput.addEventListener("input", updateSummary);

  // ---- 3. Character counter for "special requests" ----
  const notesInput = document.querySelector("#id_special_requests");
  const counter = document.querySelector("#special-requests-counter");
  const MAX_CHARS = 300;

  if (notesInput) {
    notesInput.setAttribute("maxlength", MAX_CHARS);

    const updateCounter = () => {
      if (!counter) return;
      const remaining = MAX_CHARS - notesInput.value.length;
      counter.textContent = `${remaining} characters remaining`;
    };

    notesInput.addEventListener("input", updateCounter);
    updateCounter();
  }
});
