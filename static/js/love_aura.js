const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const captureBtn = document.getElementById("captureBtn");
const capturedImage = document.getElementById("capturedImage");
const resultDiv = document.getElementById("result");
const loading = document.getElementById("loading");
let mediaStream;

// Start Camera
startBtn.addEventListener("click", () => {
  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then((stream) => {
      mediaStream = stream;
      video.srcObject = stream;
      startBtn.disabled = true;
      stopBtn.disabled = false;
      captureBtn.disabled = false;
    })
    .catch((error) => {
      console.error("Error accessing camera: ", error);
    });
});

// Stop Camera
stopBtn.addEventListener("click", () => {
  if (mediaStream) {
    mediaStream.getTracks().forEach((track) => track.stop());
    video.srcObject = null;
    startBtn.disabled = false;
    stopBtn.disabled = true;
    captureBtn.disabled = true;
  }
});

// Capture Image
captureBtn.addEventListener("click", () => {
  const ctx = canvas.getContext("2d");
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  const dataUrl = canvas.toDataURL("image/png");
  capturedImage.src = dataUrl;
  sendImageToBackend(dataUrl);
});

// Send Image to Backend
function sendImageToBackend(imageDataUrl) {
  // Show loading indicator
  loading.classList.remove("hidden");

  const formData = new FormData();
  formData.append("file", dataURLtoBlob(imageDataUrl));

  fetch("/process", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      // Render Markdown Response
      const markdownContent = `
        ${data.response}
      `;
      resultDiv.innerHTML = marked.parse(markdownContent);
    })
    .catch((error) => {
      resultDiv.innerHTML = `<p class="error">Error: ${error.message}</p>`;
    })
    .finally(() => {
      // Hide loading indicator
      loading.classList.add("hidden");
    });
}

// Convert Data URL to Blob
function dataURLtoBlob(dataURL) {
  const byteString = atob(dataURL.split(",")[1]);
  return new Blob(
    [new Uint8Array([...byteString].map((c) => c.charCodeAt(0)))],
    { type: "image/png" }
  );
}
