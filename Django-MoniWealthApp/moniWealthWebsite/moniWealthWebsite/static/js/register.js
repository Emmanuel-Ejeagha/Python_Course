document.addEventListener("DOMContentLoaded", function () {
  const togglePassword = document.querySelector("#togglePassword");
  const passwordField = document.querySelector("#passwordField");

  togglePassword.addEventListener("click", function () {
    // Toggle the type attribute
    const type =
      passwordField.getAttribute("type") === "password" ? "text" : "password";
    passwordField.setAttribute("type", type);

    // Toggle the text
    this.textContent = this.textContent === "SHOW" ? "HIDE" : "SHOW";
  });

  // Additional JavaScript for form validation can be added here
});
