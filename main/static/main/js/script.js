const realInput = document.getElementById('file-input');
const customBtn = document.getElementById('custom-button');
const previewImage = document.getElementById('preview-image');

customBtn.addEventListener('click', function() {
    realInput.click();
});

realInput.addEventListener('change', function() {
    if (realInput.files.length > 0) {
        const file = realInput.files[0];

        // Cambiar texto del botón
        customBtn.innerText = "Archivo: " + file.name;
        customBtn.style.backgroundColor = "#28a745";

        // 🔥 PREVISUALIZACIÓN EN TIEMPO REAL
        const imageURL = URL.createObjectURL(file);
        previewImage.src = imageURL;
    }
});

previewImage.onload = () => {
    URL.revokeObjectURL(previewImage.src);
};