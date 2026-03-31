document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('imageInput');
    const uploadText = document.getElementById('uploadText');

    if (fileInput && uploadText) {
        fileInput.addEventListener('change', function(e) {
            if (e.target.files.length > 0) {
                const fileName = e.target.files[0].name;
                uploadText.innerHTML = `Archivo preparado: <span class="selected-file-text">${fileName}</span>`;
            } else {
                uploadText.textContent = 'Haz clic para seleccionar o arrastra una imagen aquí';
            }
        });
    }
});