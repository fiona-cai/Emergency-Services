let socket = io.connect("http://127.0.0.1:5000")

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
});

const onConfirm = () => {
    socket.emit("confirm");
}

socket.emit("fetch")