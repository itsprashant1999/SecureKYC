const video = document.getElementById('video');
const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const statusDiv = document.getElementById('status');

let stream = null;

startButton.addEventListener('click', async () => {
    try {
        stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
        startButton.disabled = true;
        stopButton.disabled = false;
        statusDiv.textContent = 'Video started. Processing...';

        // Here you would add code to send video frames to the backend for processing.
        // Example: sendFrameToBackend(video);

    } catch (err) {
        console.error('Error accessing webcam:', err);
        statusDiv.textContent = 'Error accessing webcam.';
    }
});

stopButton.addEventListener('click', () => {
    if (stream) {
        const tracks = stream.getTracks();
        tracks.forEach(track => track.stop());
        video.srcObject = null;
        startButton.disabled = false;
        stopButton.disabled = true;
        statusDiv.textContent = 'Video stopped.';
    }
});

// Example function to send video frames to the backend
// async function sendFrameToBackend(video) {
//     // Capture a frame from the video
//     const canvas = document.createElement('canvas');
//     canvas.width = video.videoWidth;
//     canvas.height = video.videoHeight;
//     const context = canvas.getContext('2d');
//     context.drawImage(video, 0, 0, canvas.width, canvas.height);
//     const frame = canvas.toDataURL('image/png');

//     // Send the frame to the backend
//     const response = await fetch('/process-frame', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ frame })
//     });
//     const data = await response.json();
//     statusDiv.textContent = data.status;
// }
