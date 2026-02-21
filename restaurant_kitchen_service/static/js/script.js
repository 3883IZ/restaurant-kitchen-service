// Простий тестовий скрипт
console.log("Custom JS loaded successfully!");

// 🔹 Підтвердження при виході
document.addEventListener("DOMContentLoaded", () => {
    const logoutForms = document.querySelectorAll("form[action$='logout']");
    logoutForms.forEach(form => {
        form.addEventListener("submit", (event) => {
            if (!confirm("Are you sure you want to log out?")) {
                event.preventDefault();
            }
        });
    });
});

// 🔹 Плавний скрол для внутрішніх посилань
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});

// 🔹 Ефект наведення на картки (додатковий JS-анімаційний шар)
document.querySelectorAll(".card").forEach(card => {
    card.addEventListener("mouseenter", () => {
        card.style.transform = "scale(1.03)";
        card.style.transition = "transform 0.2s ease";
    });
    card.addEventListener("mouseleave", () => {
        card.style.transform = "scale(1)";
    });
});
