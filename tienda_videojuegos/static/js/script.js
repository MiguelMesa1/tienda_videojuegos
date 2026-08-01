document.addEventListener("DOMContentLoaded", function () {
  const themeButtons = document.querySelectorAll("#themeToggleMobile, #themeToggleDesktop");
  const html = document.documentElement;

  if (!themeButtons.length) return;

  function aplicarTema(theme) {
    html.setAttribute("data-bs-theme", theme);
    localStorage.setItem("theme", theme);

    themeButtons.forEach(function (btn) {
      btn.innerHTML =
        theme === "dark"
          ? `<i class="fa-solid fa-sun"></i>`
          : `<i class="fa-solid fa-moon"></i>`;

      btn.className = btn.id === "themeToggleDesktop"
        ? "btn theme-btn desktop-theme-btn"
        : "btn theme-btn";

      btn.setAttribute(
        "aria-label",
        theme === "dark" ? "Cambiar a modo claro" : "Cambiar a modo oscuro"
      );
    });
  }

  const savedTheme = localStorage.getItem("theme") || "dark";
  aplicarTema(savedTheme);

  themeButtons.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const currentTheme = html.getAttribute("data-bs-theme") || "dark";
      const newTheme = currentTheme === "dark" ? "light" : "dark";

      aplicarTema(newTheme);
    });
  });
});


// Mostrar/ocultar contraseña
function togglePassword(fieldId) {
    const field = document.getElementById(fieldId);
    const icon = document.getElementById('icon-' + fieldId);
    if (field.type === "password") {
        field.type = "text";
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        field.type = "password";
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}

// Mensajes flotantes
document.addEventListener("DOMContentLoaded", function () {
    const toastElList = [].slice.call(document.querySelectorAll('.toast'));
    toastElList.forEach(function (toastEl) {
        const toast = new bootstrap.Toast(toastEl, {
            delay: 3000
        });
        toast.show();
    });
});