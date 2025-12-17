function submit_contact() {

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
  }).then(response => {
    if (response.ok) {
      alert("Thankyou for contacting with Us, We will get back to you soon!");
    } else {
      alert("Failed to submit booking");
    }
  }).catch(error => {
    console.error("Error:", error);
    alert("Server error");
  });

}
