function toggleSidebar() {
    var sidebar = document.getElementById("sidebar");
    var content = document.getElementById("main-content");
    var burgerMenu = document.getElementById("toggle-button");

    // Toggle the sidebar width and update burger menu color
    if (sidebar.style.width === "250px") {
        // Close the sidebar
        sidebar.style.width = "0";
        content.classList.remove("shifted");
        burgerMenu.style.color = ""; // Reset color of burger menu when closed
    } else {
        // Open the sidebar
        sidebar.style.width = "250px"; 
        burgerMenu.style.color = "white"; // Set color of burger menu to white when opened
        content.classList.add("shifted"); 
    }
}

// Handle window resize event
window.addEventListener("resize", function() {
    var sidebar = document.getElementById("sidebar");
    var content = document.getElementById("main-content");
    var burgerMenu = document.getElementById("toggle-button");

    // Check if the window width is greater than 768px
    if (window.innerWidth > 768) {
        sidebar.style.width = "250px";
        content.classList.add("shifted");
        burgerMenu.style.color = "white"; // Set color of burger menu when opened
    } else {
        // If the sidebar is open, close it when resizing to smaller
        if (sidebar.style.width === "250px") {
            sidebar.style.width = "0"; 
            content.classList.remove("shifted");
            burgerMenu.style.color = ""; // Reset color of burger menu when closed
        }
    }
});
