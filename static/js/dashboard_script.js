// Function to toggle the sidebar
function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    var burgerMenu = document.getElementById("toggle-button");

    // Toggle the sidebar visibility using class
    if (sidebar.classList.contains("open-sidebar")) {
        // Close the sidebar
        sidebar.classList.remove("open-sidebar");
        burgerMenu.style.color = ""; // Reset color of burger menu when closed
    } else {
        // Open the sidebar
        sidebar.classList.add("open-sidebar");
        burgerMenu.style.color = "white"; // Set color of burger menu to white when opened
    }
}

// Handle window resize event
window.addEventListener("resize", function() {
    var sidebar = document.getElementById("sidebar");
    var burgerMenu = document.getElementById("toggle-button");

    // Check if the window width is greater than 768px
    if (window.innerWidth > 768) {
        sidebar.classList.add("open-sidebar");
        burgerMenu.style.color = "white"; // Set color of burger menu when opened
    } else {
        // If the sidebar is open, close it when resizing to smaller
        if (sidebar.classList.contains("open-sidebar")) {
            sidebar.classList.remove("open-sidebar");
            burgerMenu.style.color = ""; // Reset color of burger menu when closed
        }
    }
});

// Function to open the report modal
function openModal(reportUrl, reportTitle) {
    const modal = document.getElementById("modal");
    const modalTitle = document.getElementById("modal-title");
    const modalIframe = document.getElementById("modal-iframe");
    
    modalTitle.innerText = `Live Preview: ${reportTitle}`; // Set the title of the modal
    modalIframe.src = reportUrl; // Set the src of the iframe to the report URL
    modal.style.display = "flex"; // Show the modal using flex for centering
}

// Function to close the modal
function closeModal() {
    const modal = document.getElementById("modal");
    const modalIframe = document.getElementById("modal-iframe");
    modal.style.display = "none"; 
    modalIframe.src = ""; // Clear the iframe source
}

// Close the modal when clicking outside of it
window.onclick = function(event) {
    const modal = document.getElementById("modal");
    if (event.target === modal) {
        closeModal();
    }
}

// Close the sidebar when clicking outside of it
window.addEventListener('click', function(event) {
    var sidebar = document.getElementById("sidebar");
    var burgerMenu = document.getElementById("toggle-button");

    // Check if the click was outside of the sidebar and the toggle button
    if (!sidebar.contains(event.target) && !burgerMenu.contains(event.target) && sidebar.classList.contains("open-sidebar")) {
        sidebar.classList.remove("open-sidebar"); // Close the sidebar
        burgerMenu.style.color = ""; // Reset color of burger menu when closed
    }
});

// Add event listener for the toggle button
document.getElementById("toggle-button").addEventListener("click", toggleSidebar);
