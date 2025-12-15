document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contactForm");
  
    form.addEventListener("submit", function (e) {
      e.preventDefault();
  
      // Collect form data
      const data = {
        name: document.getElementById("Name").value,
        email: document.getElementById("email_Id").value,
        phone: document.getElementById("Mob_Number").value,
        subject: document.getElementById("Subject").value,
        message: document.getElementById("Message").value
      };
  
      // Send JSON to the server
      fetch("/contact/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("API response:", data);
          alert("Booking submitted successfully!");
          form.reset(); // reset the form
        })
        .catch((error) => {
          console.error("Error:", error);
          alert("There was an error submitting the booking.");
        });
    });
  });
  