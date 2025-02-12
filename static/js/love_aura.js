const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const captureBtn = document.getElementById("captureBtn");
const capturedImage = document.getElementById("capturedImage");
let mediaStream;

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

stopBtn.addEventListener("click", () => {
  if (mediaStream) {
    mediaStream.getTracks().forEach((track) => track.stop());
    video.srcObject = null;
    startBtn.disabled = false;
    stopBtn.disabled = true;
    captureBtn.disabled = true;
  }
});

captureBtn.addEventListener("click", () => {
  const ctx = canvas.getContext("2d");
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  const dataUrl = canvas.toDataURL("image/png");
  capturedImage.src = dataUrl;
  sendImageToBackend(dataUrl);
});

function sendImageToBackend(imageDataUrl) {
  const formData = new FormData();
  formData.append("file", dataURLtoBlob(imageDataUrl));

  fetch("/process", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById(
        "result"
      ).innerHTML = `<h2>❤️ Your Love Aura:</h2><p>${data.response}</p>`;
    })
    .catch((error) => {
      document.getElementById("result").innerText = `Error: ${error.message}`;
    });
}

function dataURLtoBlob(dataURL) {
  const byteString = atob(dataURL.split(",")[1]);
  return new Blob(
    [new Uint8Array([...byteString].map((c) => c.charCodeAt(0)))],
    { type: "image/png" }
  );
}
