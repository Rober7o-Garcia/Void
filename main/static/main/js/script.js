    const realInput = document.getElementById('file-input');
    const customBtn = document.getElementById('custom-button');

    customBtn.addEventListener('click', function() {
        realInput.click();
    });

    realInput.addEventListener('change', function() {
        if (realInput.files.length > 0) {
            customBtn.innerText = "Archivo: " + realInput.files[0].name;
            customBtn.style.backgroundColor = "#28a745";
        }
    });