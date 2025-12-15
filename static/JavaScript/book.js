
function submit_booking_form(event) {
    let from_location = document.getElementById("from_location").value;
    let to_location = document.getElementById("to_location").value;
    let destination = document.getElementById("destination").value;
    let fullname = document.getElementById("fullname").value;
    let email = document.getElementById("email").value;
    let mobile = document.getElementById("mobile").value;
    let requirements = document.getElementById("requirements").value;

    let travelTypeCard = document.querySelector(".travel-type-card.active");
    let travel_type = travelTypeCard
        ? travelTypeCard.getAttribute("data-value")
        : "";

    let transportCard = document.querySelector(".transport-card.active");
    let transport = transportCard
        ? transportCard.querySelector("p").innerText
        : "";

    let counters = document.querySelectorAll(".traveler-box .counter");
    let travelers = {};
    counters.forEach(function (counter) {
        let label = counter.querySelector("span").innerText.toLowerCase();
        let value = counter.querySelector("input").value;
        travelers[label] = value;
    });

    let errors = [];
    if (!from_location) errors.push("From Location is required.");
    if (!to_location) errors.push("To Location is required.");
    if (!destination || destination === "Select Destination")
        errors.push("Please select a destination.");
    if (!fullname) errors.push("Full Name is required.");
    if (!email) errors.push("Email is required.");
    if (!mobile) errors.push("Mobile Number is required.");
    if (!travel_type) errors.push("Please select a travel type.");
    if (!transport) errors.push("Please select a transport type.");

    let formData = {
        from_location,
        to_location,
        destination,
        travel_type,
        transport,
        travelers,
        fullname,
        email,
        mobile,
        requirements,
    };

    // Send to API
    fetch("/booking/", {
        // <-- replace with your API endpoint
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
    }).then((response) => {
        if (response.ok) {
            alert("Booking submitted successfully!");
            document.querySelector(".booking-form").reset();
        } else {
            alert("Failed to submit booking. Status: " + response.status);
        }
    }).catch((error) => {
        console.error("Error:", error);
        alert("There was an error submitting the booking.");
        });
    }




// ========================================
// TRAVEL TYPE SELECT (Trek, Tour, Adventure, Family)
// ========================================
document.addEventListener("click", function (e) {
    if (e.target.closest(".travel-type-card")) {
        let clicked = e.target.closest(".travel-type-card");

        document.querySelectorAll(".travel-type-card")
            .forEach(c => c.classList.remove("active"));

        clicked.classList.add("active");
    }
});



// ========================================
// TRANSPORT REQUIRED SELECT (Bus, Car, Traveller)
// ========================================
document.querySelectorAll(".transport-card").forEach(card => {
    card.addEventListener("click", function () {
        document.querySelectorAll(".transport-card").forEach(c => c.classList.remove("active"));
        this.classList.add("active");
    });
});


// ========================================
// TRAVELERS COUNTER (Adults / Children / Rooms)
// ========================================
document.querySelectorAll(".counter").forEach(counterBox => {
    let input = counterBox.querySelector("input");
    let minusBtn = counterBox.querySelector(".minus");
    let plusBtn = counterBox.querySelector(".plus");

    minusBtn.addEventListener("click", function () {
        let value = parseInt(input.value);
        if (value > 0) input.value = value - 1;
    });

    plusBtn.addEventListener("click", function () {
        let value = parseInt(input.value);
        input.value = value + 1;
    });
});
