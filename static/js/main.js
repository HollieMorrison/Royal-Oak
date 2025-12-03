// LIVE BOOKING SUMMARY
document.addEventListener("input", function () {
    const date = document.querySelector("#id_date");
    const time = document.querySelector("#id_time");
    const party = document.querySelector("#id_party_size");

    const summary = document.querySelector("#booking-summary");
    if (summary) {
        summary.innerHTML = `
            Date: ${date?.value || "—"}<br>
            Time: ${time?.value || "—"}<br>
            Guests: ${party?.value || "—"}
        `;
    }
});

// CHARACTER COUNTER
document.addEventListener("input", function () {
    const textarea = document.querySelector("#id_special_requests");
    const counter = document.querySelector("#special-requests-counter");

    if (textarea && counter) {
        const max = 300;
        const remaining = max - textarea.value.length;
        counter.textContent = `${remaining} characters remaining`;
    }
});

// MENU CATEGORY TOGGLE
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".menu-category-title").forEach((title) => {
        title.addEventListener("click", () => {
            const content = title.nextElementSibling;
            content.style.display =
                content.style.display === "none" ? "block" : "none";
        });
    });
});
