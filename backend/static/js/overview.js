const URL = process.env.NODE_ENV === 'production' ? undefined : 'http://localhost:5000';
let socket = io.connect(URL)

const onLoad = () => {
	socket.onconnect(() => {
		socket.emit("connect");
	});
};

socket.on("send", (data) => {
    console.log("data has been sent and stored")
    // now put text from data into the elements
    document.getElementById('polices').innerText = data.police_officers;
    document.getElementById('fires').innerText = data.firefighters;
    document.getElementById('medics').innerText = data.paramedics;
    document.getElementById('eta').innerText = data.eta;
    document.getElementById('location').innerText = data.location;
    document.getElementById('crisis').innerText = data.crisis;
    document.getElementById('severity').innerText = data.severity;
});

const onConfirm = () => {
    socket.emit("confirm");
}

socket.emit("fetch")