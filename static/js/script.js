
const uploadForm = document.getElementById("uploadForm");
const imageInput = document.getElementById("imageInput");
const imagePreview = document.getElementById("imagePreview");

const loading = document.getElementById("loading");
const result = document.getElementById("result");
const prediction = document.getElementById("prediction");
const score = document.getElementById("score");
const error = document.getElementById("error");
const predictButton = document.getElementById("predictButton");


// Preview uploaded image
imageInput.addEventListener("change", function () {

    const file = imageInput.files[0];

    result.classList.add("hidden");
    error.textContent = "";

    if (file) {
        imagePreview.src = URL.createObjectURL(file);
        imagePreview.style.display = "block";
    } else {
        imagePreview.style.display = "none";
    }
});


// Send image to Flask backend
uploadForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const file = imageInput.files[0];

    if (!file) {
        error.textContent = "Please select an image.";
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    loading.classList.remove("hidden");
    result.classList.add("hidden");
    error.textContent = "";
    predictButton.disabled = true;

    try {

        const response = await fetch("/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Prediction failed.");
        }

        prediction.textContent = "Class: " + data.prediction;

        score.textContent =
            "Model score: " + data.model_score + "%";

        result.classList.remove("hidden");

    } catch (err) {

        error.textContent = err.message;

    } finally {

        loading.classList.add("hidden");
        predictButton.disabled = false;

    }

});
