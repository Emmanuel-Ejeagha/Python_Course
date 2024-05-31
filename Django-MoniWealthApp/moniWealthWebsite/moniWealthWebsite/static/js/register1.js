"use strip";

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

const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid-feedback");
const emailField = document.querySelector("#emailField");
const emailFeedbackArea = document.querySelector(".emailFeedBackArea");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const emailSuccessOutput = document.querySelector(".emailSuccessOutput");
const submitButton = document.querySelector(".submit-btn");

// Checks the email
emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;
  emailSuccessOutput.style.display = "block";

  emailSuccessOutput.textContent = `checking ${emailVal}`;

  emailField.classList.remove("is-invalid");
  emailFeedbackArea.style.display = "none";

  if (emailVal.length > 0) {
    // API call
    fetch("/authentication/validate-email", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        emailSuccessOutput.style.display = "none";

        // Displays an error message if the user enters a symbol
        if (data.email_error) {
          emailField.classList.add("is-invalid");
          emailFeedbackArea.style.display = "block";
          emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`;
          submitButton.disabled = true;
        } else {
          submitButton.removeAttribute("disabled");
        }
      });
  }
});

usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;
  usernameSuccessOutput.style.display = "block";

  usernameSuccessOutput.textContent = `checking ${usernameVal}`;

  usernameField.classList.remove("is-invalid");
  feedBackArea.style.display = "none";

  // runs a check once a user enters an input in the text area
  if (usernameVal.length > 0) {
    // API call
    fetch("/authentication/validate-username", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        usernameSuccessOutput.style.display = "none";

        // Displays an error message if the user enters a symbol
        if (data.username_error) {
          usernameField.classList.add("is-invalid");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
          submitButton.disabled = true;
        } else {
          submitButton.removeAttribute("disabled");
        }
      });
  }
});

// SHOW and HIDE password
// document
//   .getElementById("togglePassword")
//   .addEventListener("click", function () {
//     const passwordField = document.getElementById("passwordField");
//     const type =
//       passwordField.getAttribute("type") === "password" ? "text" : "password";
//     passwordField.setAttribute("type", type);
//     this.textContent = this.textContent === "SHOW" ? "HIDE" : "SHOW";
//   });
