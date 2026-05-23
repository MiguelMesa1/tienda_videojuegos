console.log("script.js cargado correctamente");

document.addEventListener("DOMContentLoaded", function () {
  const themeToggle = document.getElementById("themeToggle");
  const html = document.documentElement;

  if (!themeToggle) return;

  function aplicarTema(theme) {
    html.setAttribute("data-bs-theme", theme);
    localStorage.setItem("theme", theme);

    themeToggle.innerHTML =
      theme === "dark"
        ? `<i class="fa-solid fa-sun"></i>`
        : `<i class="fa-solid fa-moon"></i>`;

    themeToggle.className =
      theme === "dark"
        ? "btn btn-outline-light d-flex align-items-center justify-content-center rounded-circle shadow-sm"
        : "btn btn-outline-dark d-flex align-items-center justify-content-center rounded-circle shadow-sm";

    themeToggle.style.width = "42px";
    themeToggle.style.height = "42px";
  }

  const savedTheme = localStorage.getItem("theme") || "dark";
  aplicarTema(savedTheme);

  themeToggle.addEventListener("click", function () {
    const currentTheme = html.getAttribute("data-bs-theme") || "dark";
    const newTheme = currentTheme === "dark" ? "light" : "dark";

    aplicarTema(newTheme);
  });
});